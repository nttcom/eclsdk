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

import six

from ecl import proxy2
from ecl import session
from ecl.rca.v1 import user as _user
from ecl.rca import version as _version


class VersionSession(session.Session):

    def get_endpoint(self, auth=None, interface='public', service_type=None,
                     **kwargs):
        """Override get endpoint to automate endpoint filtering

        This method uses the service catalog to find the root URI of
        each service and then gets all available versions directly
        from the service, not from the service catalog.

        Endpoints are cached per service type and interface combination
        so that they're only requested from the remote service once
        per instance of this class.
        """

        sc_endpoint = super(VersionSession, self).get_endpoint(
            auth, interface, service_type
        )

        if sc_endpoint is None or sc_endpoint == '':
            return sc_endpoint
        segments = sc_endpoint.split('/')
        if len(segments) > 0:
            segments = segments[:-2]
            sc_endpoint = ""
            for segment in segments:
                sc_endpoint += segment + '/'
            sc_endpoint = sc_endpoint[:-1]

        return sc_endpoint


class Proxy(proxy2.BaseProxy):

    def users(self):
        """
        List VPN user. Now, VPN user can create per one tenant, so user
        list hash only one user.

        :return: A list of user objects
        """
        return list(self._list(_user.User))

    def get_user(self, username):
        """
        Show VPN user.

        :param username: Query user name
        :return: One :class:`~ecl.rca.v1.user.User` or
                     :class:`~ecl.exceptions.ResourceNotFound`when no
                     resource can be found.
        """
        return self._get(_user.User, username)

    def create_user(self, password):
        """
        Create VPN user. One VPN user can create per one tenant.
        And username equal to tenant_id.

        :param password: The password of VPN connection.
                Available character is 8-127 character of alphabet[a-zA-Z],
                number[0-9] and Symbols[.-_/*+,!#$%&()~|].
        :return: The results of user creation
        :rtype: :class:`~ecl.rca.v1.user.User`
        """
        return self._create(_user.User, password=password)

    def update_user(self, username, password):
        """
        Update VPN user.

        :param username: The username of VPN user.
        :param password: The password of VPN connection. Available character is
                8-127 character of alphabet[a-zA-Z], number[0-9] and Symbols[
                .-_/*+,!#$%&()~|].
        :return: :class:`~ecl.rca.v1.user.User`
        """
        return self._update(_user.User, name=username, password=password)

    def delete_user(self, username):
        """
        Delete VPN user.

        :param username: The username of VPN user.
        :return: ``None``
        """
        return self._delete(_user.User, username)

    def find_user(self, name_or_id, ignore_missing=False):
        """Find a single VPN user.

        :param name_or_id: The name or ID of a user.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.rca.v1.user.User` or None
        """
        return self._find(_user.User, name_or_id, ignore_missing=ignore_missing)

    def get_version(self):
        """
        Show VPN version.

        :return: :class:`~ecl.rca.version.Version`
        """
        version = _version.Version()
        v_session = VersionSession(
            profile=self.session.profile,
            user_agent=self.session.user_agent,
        )
        for attr, value in six.iteritems(self.session.__dict__):
            v_session.__setattr__(attr, value)

        return version.get_version(session=v_session)

    def versions(self):
        """
        List VPN versions.

        :return: A generator of version objects
        """
        version = _version.Version()
        v_session = VersionSession(
            profile=self.session.profile,
            user_agent=self.session.user_agent,
        )
        for attr, value in six.iteritems(self.session.__dict__):
            v_session.__setattr__(attr, value)

        return list(version.list_version(session=v_session))
