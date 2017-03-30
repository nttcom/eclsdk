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

from ecl.baremetal import baremetal_service
from ecl import resource2


class UEFI(resource2.Resource):
    resource_key = 'uefi'
    resources_key = 'uefi'
    base_path = '/servers/%(server_id)s/uefi'
    service = baremetal_service.BaremetalService()

    # capabilities
    allow_update = True
    allow_get = True

    #: Name for the flavor.
    flavor_name = resource2.Body('flavor_name')
    #: The ID for the flavor.
    flavor_id = resource2.Body('flavor_id', alternate_id=True)
    #: Updated time for UEFI
    updated = resource2.Body('updated')
    #: The last result of applying uefi setting.
    status = resource2.Body('status')
    #: Error messages when updating uefi setting is failed.
    message = resource2.Body('message')
    #: UEFI setting.
    setting = resource2.Body('setting', type=dict)

    def get(self, session, server_id):
        uri = self.base_path % {"server_id": server_id}
        resp = session.get(uri, endpoint_filter=self.service)
        self._translate_response(resp, has_body=True)
        return self

    def update(self, session, server_id, has_body=True, **attrs):
        uri = self.base_path % {"server_id": server_id}
        body = attrs
        args = {'json': body}
        resp = session.put(uri, endpoint_filter=self.service, **args)
        self._translate_response(resp, has_body=False)
        return self
