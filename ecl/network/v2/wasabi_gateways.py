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

from ecl.network import network_service
from ecl import resource2


class WasabiGateways(resource2.Resource):
    resource_key = "wasabi_gateway"
    resources_key = "wasabi_gateways"
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/' + resources_key

    # Capabilities
    allow_create = True
    allow_delete = True
    allow_update = True
    allow_list = True
    allow_get = True
    patch_update = True

    # Properties
    #: ID for the resource
    wasabi_gateway_id = resource2.Body('wasabi_gateway_id')
    #: The Common Function Gateway ID to associate with this Wasabi Gateway.
    common_function_gateway_id = resource2.Body('common_function_gateway_id')
    #: Description of the Wasabi Gateway resource.
    description = resource2.Body('description')
    #: Name of the Wasabi Gateway resource
    name = resource2.Body('name')
    #: status of the resource.
    status = resource2.Body('status')
    #: Tenant ID of the owner (UUID)
    tenant_id = resource2.Body('tenant_id')


    def create(self, session, common_function_gateway_id, description, name, tenant_id):
        params = {
            "common_function_gateway_id": common_function_gateway_id,
            "description": description,
            "name": name,
            "tenant_id": tenant_id
        }
        resp = session.post(
            self.base_path,
            endpoint_filter = self.service,
            json={self.resource_key: params}
        )
        self._translate_response(resp, has_body=True)
        return self

    def update(self, session, wasabi_gateway_id, description=None, name=None):
        params = {}
        if description:
            params['description'] = description
        if name:
            params['name'] = name

        uri = self.base_path + '/' + wasabi_gateway_id
        resp = session.put(
            uri,
            endpoint_filter=self.service,
            json={self.resource_key: params}
        )
        self._translate_response(resp, has_body=True)
        return self
