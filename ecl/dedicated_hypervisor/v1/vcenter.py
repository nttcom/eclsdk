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


class Vcenter(resource2.Resource):
    resources_key = "vcenter"
    resource_key = "vcenter"
    base_path = '/vcenters'
    service = dedicated_hypervisor_service.DedicatedHypervisorService()

    # Capabilities
    allow_list = True
    allow_create = True
    allow_delete = True

    _query_mapping = resource2.QueryParameters("vcenters")

    # Properties
    #: id of vCenter Server.
    id = resource2.Body('id')
    #: local address.
    local_address = resource2.Body('link_local_address')
    #: status for connection.
    metering_health = resource2.Body('metering_health')
    #: type of health error.
    metering_health_error_type = resource2.Body('metering_health_error_type')
    #: version
    version = resource2.Body('version')
    #: name of vCenter server
    instance_name = resource2.Body('instance_name')

    def show_vcenter(self, session):
        uri = self.base_path
        resp = session.get(
            uri,
            endpoint_filter=self.service
        )
        self._translate_response(resp)
        return self

    def register_vcenter(self, session, password, license_id):
        url = self.base_path
        resp = session.post(url, endpoint_filter = self.service,
                            json={"password": password,
                                  "Licence_id": license_id})
        self._translate_response(resp, has_body=True)
        return self

    def update_vcenter(self, session, vcenter_id, password, license_id):
        uri = self.base_path + vcenter_id
        params = {}
        if password:
            params['password'] = password
        if license_id:
            params['license_id'] = license_id

        resp = session.post(
            uri,
            endpoint_filter=self.service,
            json=params
        )
        self._translate_response(resp, has_body=True)
        return self
