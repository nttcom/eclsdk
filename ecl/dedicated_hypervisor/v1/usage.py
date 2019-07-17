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

from six.moves.urllib.parse import quote
from ecl.dedicated_hypervisor import dedicated_hypervisor_service
from ecl import resource2


class Usage(resource2.Resource):
    resources_key = "usages"
    resource_key = None
    base_path = '/usages'
    service = dedicated_hypervisor_service.DedicatedHypervisorService()

    # Capabilities
    allow_list = True
    allow_get = True

    # Properties
    #: history id of Guest Image usage.
    id = resource2.Body('id')
    #: license type name for the usage.
    name = resource2.Body('name')
    #: license type description for the usage.
    description = resource2.Body('description')
    #: type of Guest Image usage.
    type = resource2.Body('type')
    #: if true, there is license key.
    has_license_key = resource2.Body('has_license_key')
    #: unit for the usage.
    unit = resource2.Body('unit')
    #: usage value.
    value = resource2.Body('value')
    #: uuid for the resource.
    resource_id = resource2.Body('resource_id')
    #: date to list usage from.
    From = resource2.Body('from')
    #: date to list usage to.
    #: month of the parameter must be the same as `from` .
    to = resource2.Body('to')
    #: name of license type to show.
    license_type = resource2.Body('license_type')
    #: histories of the usage
    histories = resource2.Body('histories')

    def get_usage_histories(self, session, history_id, **kwargs):
        """Shows your Guest Image usage history information."""

        params = []
        for key in kwargs.keys():
            item = "%s=%s" % (str(key), quote(str(kwargs[key]))) \
                if key in ['from', 'to'] \
                else "%s=%s" % (str(key), str(kwargs[key]))
            params.append(item)

        uri = self.base_path + '/%s/histories' % history_id
        if len(params) != 0:
            uri += '?'
            for item in params:
                uri += item + '&'
            uri = uri[:-1]

        resp = session.get(uri, endpoint_filter=self.service)
        self._translate_response(resp, has_body=True)
        return self
