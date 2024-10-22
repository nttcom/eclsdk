# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""
The :class:`~ecl.session.Session` overrides
:class:`~keystoneauth1.session.Session` to provide end point filtering and
mapping KSA exceptions to SDK exceptions.

"""
import re
import json

from collections import namedtuple

from keystoneauth1 import exceptions as _exceptions
from keystoneauth1 import session as _session

from ecl import exceptions
from ecl import utils
from ecl import version as ecl_version

from ecl.baremetal import exceptions as baremetal_exp
from ecl.connectivity import exceptions as connectivity_exp
from ecl.dedicated_hypervisor import exceptions as dh_exp
from ecl.network import exceptions as network_exp
from ecl.rca import exceptions as rca_exp
from ecl.sss import exceptions as sss_exp
from ecl.storage import exceptions as storage_exp
from ecl.provider_connectivity import exceptions as icc_exp
from ecl.virtual_network_appliance import exceptions as vna_exp

from six.moves.urllib import parse

DEFAULT_USER_AGENT = "eclsdk/%s" % ecl_version.__version__
API_REQUEST_HEADER = "ecl-api-version"

Version = namedtuple("Version", ["major", "minor"])


def find_http_exception_class(e_url):
    mapper = {
        'baremetal-server': baremetal_exp.HttpException,
        'interconnectivity': connectivity_exp.HttpException,
        'dedicated-hypervisor': dh_exp.HttpException,
        'network': network_exp.HttpException,
        'rca': rca_exp.HttpException,
        'sss': sss_exp.HttpException,
        'storage': storage_exp.HttpException,
        'provider-connectivity': icc_exp.HttpException,
    }

    # to avoid matching to "network" endpoint.
    if re.search('virtual-network-appliance', e_url) is not None:
        return vna_exp.HttpException

    for pattern, exception_class in mapper.items():
        if re.search(pattern, e_url) is not None:
            return exception_class

    return exceptions.HttpException


def find_not_found_exception_class(e_url):
    mapper = {
        'baremetal-server': baremetal_exp.NotFoundException,
        'interconnectivity': connectivity_exp.NotFoundException,
        'dedicated-hypervisor': dh_exp.NotFoundException,
        'network': network_exp.NotFoundException,
        'rca': rca_exp.NotFoundException,
        'sss': sss_exp.NotFoundException,
        'storage': storage_exp.NotFoundException,
        'provider-connectivity': icc_exp.NotFoundException,
    }

    # to avoid matching to "network" endpoint.
    if re.search('virtual-network-appliance', e_url) is not None:
        return vna_exp.NotFoundException

    for pattern, exception_class in mapper.items():
        if re.search(pattern, e_url) is not None:
            return exception_class

    return exceptions.NotFoundException


def map_exceptions(func):
    def map_exceptions_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except _exceptions.HttpError as e:
            if e.http_status == 404:
                exception_class = find_not_found_exception_class(e.url)
                exp = exception_class(
                    message=e.message,
                    details=e.details,
                    response=e.response,
                    request_id=e.request_id,
                    url=e.url,
                    method=e.method,
                    http_status=e.http_status,
                    cause=e)
                raise exp
            else:
                exception_class = find_http_exception_class(e.url)
                exp = exception_class(
                    message=e.message,
                    details=e.details,
                    response=e.response,
                    request_id=e.request_id,
                    url=e.url,
                    method=e.method,
                    http_status=e.http_status,
                    cause=e)
                raise exp
        except _exceptions.ClientException as e:
            raise exceptions.SDKException(message=e.message, cause=e)

    return map_exceptions_wrapper


class Session(_session.Session):

    def __init__(self, profile, user_agent=None, **kwargs):
        """Create a new Keystone auth session with a profile.

        :param profile: If the user has any special profiles such as the
            service name, region, version or interface, they may be provided
            in the profile object.  If no profiles are provided, the
            services that appear first in the service catalog will be used.
        :param user_agent: A User-Agent header string to use for the
                           request. If not provided, a default of
                           :attr:`~ecl.session.DEFAULT_USER_AGENT`
                           is used, which contains the eclsdk version
                           When a non-None value is passed, it will be
                           prepended to the default.
        :type profile: :class:`~ecl.profile.Profile`
        """
        if user_agent is not None:
            self.user_agent = "%s %s" % (user_agent, DEFAULT_USER_AGENT)
        else:
            self.user_agent = DEFAULT_USER_AGENT

        self.profile = profile
        api_version_header = self._get_api_requests()
        self.endpoint_cache = {}

        super(Session, self).__init__(user_agent=self.user_agent,
                                      additional_headers=api_version_header,
                                      **kwargs)

    def _get_api_requests(self):
        """Get API micro-version requests.

        :param profile: A profile object that contains customizations about
                        service name, region, version, interface or
                        api_version.
        :return: A standard header string if there is any specialization in
                 API microversion, or None if no such request exists.
        """
        if self.profile is None:
            return None

        req = []
        for svc in self.profile.get_services():
            if svc.service_type and svc.api_version:
                req.append(" ".join([svc.service_type, svc.api_version]))
        if req:
            return {API_REQUEST_HEADER: ",".join(req)}

        return None

    def _get_endpoint_versions(self, service_type, endpoint):
        """Get available endpoints from the remote service

        Take the endpoint that the Service Catalog gives us, then split off
        anything and just take the root. We need to make a request there
        to get the versions the API exposes.
        """
        parts = parse.urlparse(endpoint)
        root_endpoint = "://".join([parts.scheme, parts.netloc])
        response = self.get(root_endpoint)

        # Normalize the version response. Identity nests the versions
        # a level deeper than others, inside of a "values" dictionary.
        response_body = response.json()
        if "versions" in response_body:
            versions = response_body["versions"]
            if "values" in versions:
                versions = versions["values"]
            return root_endpoint, versions

        raise exceptions.EndpointNotFound(
            "Unable to parse endpoints for %s" % service_type)

    def _parse_version(self, version):
        """Parse the version and return major and minor components

        If the version was given with a leading "v", e.g., "v3", strip
        that off to just numerals.
        """
        version_num = version[version.find("v") + 1:]
        components = version_num.split(".")
        if len(components) == 1:
            # The minor version of a v2 ends up being -1 so that we can
            # loop through versions taking the highest available match
            # while also working around a direct match for 2.0.
            rv = Version(int(components[0]), -1)
        elif len(components) == 2:
            rv = Version(*[int(component) for component in components])
        else:
            raise ValueError("Unable to parse version string %s" % version)

        return rv

    def _get_version_match(self, versions, profile_version, service_type,
                           root_endpoint, requires_project_id):
        """Return the best matching version

        Look through each version trying to find the best match for
        the version specified in this profile.
         * The best match will only ever be found within the same
           major version, meaning a v2 profile will never match if
           only v3 is available on the server.
         * The search for the best match is fuzzy if needed.
           * If the profile specifies v2 and the server has
             v2.0, v2.1, and v2.2, the match will be v2.2.
           * When an exact major/minor is specified, e.g., v2.0,
             it will only match v2.0.
        """
        match = None
        for version in versions:
            api_version = self._parse_version(version["id"])
            if profile_version.major != api_version.major:
                continue

            if profile_version.minor <= api_version.minor:
                for link in version["links"]:
                    if link["rel"] == "self":
                        match = link["href"]

            # Only break out of the loop on an exact match,
            # otherwise keep trying.
            if profile_version.minor == api_version.minor:
                break

        if match is None:
            raise exceptions.EndpointNotFound(
                "Unable to determine endpoint for %s" % service_type)

        # Some services return only the path fragment of a URI.
        # If we split and see that we're not given the scheme and netloc,
        # construct the match with the root from the service catalog.
        match_split = parse.urlsplit(match)
        if not all([match_split.scheme, match_split.netloc]):
            match = root_endpoint + match

        # For services that require the project id in the request URI,
        # add them in here.
        if requires_project_id:
            match = utils.urljoin(match, self.get_project_id())

        return match

    def get_endpoint(self, auth=None, interface=None, service_type=None,
                     **kwargs):
        """Override get endpoint to automate endpoint filtering

        This method uses the service catalog to find the root URI of
        each service and then gets all available versions directly
        from the service, not from the service catalog.

        Endpoints are cached per service type and interface combination
        so that they're only requested from the remote service once
        per instance of this class.
        """
        key = (service_type, interface)
        if key in self.endpoint_cache:
            return self.endpoint_cache[key]

        filt = self.profile.get_filter(service_type)
        if filt.interface is None:
            filt.interface = interface

        sc_endpoint = super(Session, self).get_endpoint(auth,
                                                        **filt.get_filter())

        self.endpoint_cache[key] = sc_endpoint
        return sc_endpoint

        # Object Storage is, of course, different. Just use what we get
        # back from the service catalog as not only does it not offer
        # a list of supported versions, it appends an "AUTH_" prefix to
        # the project id so we'd have to special case that as well.
        # if service_type == "object-store":
        #     self.endpoint_cache[key] = sc_endpoint
        #     return sc_endpoint
        #
        # root_endpoint, versions = self._get_endpoint_versions(service_type,
        #                                                       sc_endpoint)
        # profile_version = self._parse_version(filt.version)
        # match = self._get_version_match(versions, profile_version,
        #                                 service_type, root_endpoint,
        #                                 filt.requires_project_id)
        #
        # self.endpoint_cache[key] = match
        # return match

    @map_exceptions
    def request(self, *args, **kwargs):
        return super(Session, self).request(*args, **kwargs)

    def _is_keystone_discover_result(self, content):
        """
        Check if given response body is keystone discover API result.
        :param string content: Response contents
        :return:
        """
        try:
            json_body = json.loads(content)
            if 'version' in json_body \
                    and 'links' in json_body['version'] \
                    and len(json_body['version']['links']) == 1 \
                    and 'href' in json_body['version']['links'][0]:
                return True
        except:
            return False
        return False

    def _replace_discoverd_keystone_url(self, content):
        """
        Replace discoverd url of keystone in case protocol returned as 'http'.
        Because only https access is allowd to ECL2.0 Keystone.
        :param string content: Response contents
        :return:
        """
        try:
            result = self._is_keystone_discover_result(content)
            if result:
                json_body = json.loads(content)

                # Check if url is returned as http url.
                discoverd_url = json_body['version']['links'][0]['href']
                if re.match('http:', discoverd_url):
                    https_url = discoverd_url.replace('http:', 'https:')
                    # Replace url if http.
                    json_body['version']['links'][0]['href'] = https_url

                    new_content = json.dumps(json_body)
                    return new_content
        except:
            pass
        return content

    def _send_request(self, url, method, redirect, log, logger,
                      connect_retries, connect_retry_delay=0.5, **kwargs):
        resp = super(Session, self)._send_request(
            url, method, redirect, log,
            logger, connect_retries,
            connect_retry_delay=connect_retry_delay,
            **kwargs)
        if re.match('https:', url):
            try:
                resp._content = self._replace_discoverd_keystone_url(
                    resp._content)
            except:
                pass
        return resp

    def get(self, url, **kwargs):
        self._append_accecpt_header(kwargs)
        return super(Session, self).get(url, **kwargs)

    def post(self, url, **kwargs):
        self._append_accecpt_header(kwargs)
        return super(Session, self).post(url, **kwargs)

    def put(self, url, **kwargs):
        self._append_accecpt_header(kwargs)
        return super(Session, self).put(url, **kwargs)

    def delete(self, url, **kwargs):
        self._append_accecpt_header(kwargs)
        return super(Session, self).delete(url, **kwargs)

    def patch(self, url, **kwargs):
        self._append_accecpt_header(kwargs)
        return super(Session, self).patch(url, **kwargs)

    def _append_accecpt_header(self, kwargs):
        headers = kwargs['headers'] if 'headers' in kwargs else {}
        if "Accept" not in headers:
            headers["Accept"] = "application/json"
        elif headers["Accept"] == '':
            headers["Accept"] = "application/json"
        kwargs['headers'] = headers
