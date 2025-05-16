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

from ecl.dedicated_hypervisor import dedicated_hypervisor_service
from ecl import resource2


class VCenter(resource2.Resource):
    resources_key = "vcenters"
    resource_key = "vcenter"
    base_path = '/vcenters'
    service = dedicated_hypervisor_service.DedicatedHypervisorService()

    # Capabilities
    allow_list = True
    allow_create = True
    allow_update = True
    allow_delete = True

    # Properties
    #: id of vCenter Server.
    id = resource2.Body('id')
    #: local address.
    link_local_address = resource2.Body('link_local_address')
    #: status for connection.
    metering_health = resource2.Body('metering_health')
    #: type of health error.
    metering_health_error_type = resource2.Body('metering_health_error_type')
    #: version
    version = resource2.Body('version')
    #: name of vCenter server
    instance_name = resource2.Body('instance_name')
    #: The ID of the license key assigned to the vCenter Server
    license_id = resource2.Body('license_id')

    def register(self, session, link_local_address, password, license_id):
        params = {
            "link_local_address": link_local_address,
            "password": password,
            "license_id": license_id
        }
        resp = session.post(
            self.base_path,
            endpoint_filter = self.service,
            json={self.resource_key: params}
        )
        self._translate_response(resp, has_body=True)
        return self

    def update(self, session, vcenter_id, link_local_address, password, license_id):
        params = {}
        if link_local_address:
            params['link_local_address'] = link_local_address
        if password:
            params['password'] = password
        if license_id:
            params['license_id'] = license_id

        uri = self.base_path + '/' + vcenter_id
        resp = session.put(
            uri,
            endpoint_filter=self.service,
            json={self.resource_key: params}
        )
        self._translate_response(resp, has_body=True)
        return self


class LinkLocalAddresses(resource2.Resource):
    base_path = '/vcenters/addresses'
    resources_key = 'addresses'
    resource_key = 'address'
    service = dedicated_hypervisor_service.DedicatedHypervisorService()

    # capabilities
    allow_list = True

    # Properties
    #: IP address.
    address = resource2.Body('address', alternate_id=True)
    #: status that IP address is used or not.
    in_use = resource2.Body('in_use')
