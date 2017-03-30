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


class NicPhysicalPort(resource2.Resource):
    resource_key = "nic_physical_port"
    resources_key = "nic_physical_ports"
    base_path = '/servers/%(server_id)s/nic_physical_ports'
    service = baremetal_service.BaremetalService()

    # Capabilities
    allow_get = True
    allow_list = True

    # Properties
    #: ID for the specified server.
    server_id = resource2.Body('server_id')
    #: UUID of the NicPhysicalPort.
    id = resource2.Body('id')
    #: MAC address of the NicPhysicalPort.
    mac_addr = resource2.Body('mac_addr')
    #: Network controller port id of physical leaf switch.
    network_physical_port_id = resource2.Body('network_physical_port_id')
    #: Value = 'data'(default) or 'storage'. Assigning preferentially the
    #: order to the NIC physical port. data plane: all devices cloud be
    #: connected. storage plane: this plane type is only used and optimized
    #: for storages between servers.You can assigning each until 2 planes.
    plane = resource2.Body('plane')
    #: Logical attached ports of host.
    attached_ports = resource2.Body('attached_ports')
    #: ID of hardware attaching the NicPhysicalPort.
    hardware_id = resource2.Body('hardware_id')

    def list(self, session, server_id):
        uri = self.base_path % {"server_id" : server_id}
        resp = session.get(uri, endpoint_filter=self.service,
                           headers={"Accept": "application/json"})
        resp = resp.json()
        resp = resp[self.resources_key]

        for data in resp:
            value = self.existing(**data)
            yield value

    def get(self, session, server_id, port_id):
        uri = self.base_path + '/%(nic_physical_port_id)s'
        uri = uri % {"server_id": server_id,
                                "nic_physical_port_id": port_id}
        resp = session.get(uri, endpoint_filter=self.service,
                           headers={"Accept": "application/json"})
        self._translate_response(resp, has_body=True)
        return self
