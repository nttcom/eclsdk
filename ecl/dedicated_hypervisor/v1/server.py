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


class Server(resource2.Resource):
    resources_key = "servers"
    resource_key = "server"
    base_path = '/servers'
    service = dedicated_hypervisor_service.DedicatedHypervisorService()

    # Capabilities
    allow_list = True
    allow_get = True
    allow_create = True
    allow_delete = True

    _query_mapping = resource2.QueryParameters("image", "flavor", "name",
                                               "status",
                                               changes_since="changes-since")

    # Properties
    #: id of Dedicated Hypervisor instance.
    id = resource2.Body('id')
    #: Link of the Dedicated Hypervisor server.
    links = resource2.Body('links')
    #: name of Dedicated Hypervisor instance.
    name = resource2.Body('name')
    #: description of Dedicated Hypervisor instance.
    description = resource2.Body('description')
    #: type of hypervisor. vsphere_esxi or hyper_v.
    hypervisor_type = resource2.Body('hypervisor_type')
    #: image id of Dedicated Hypervisor instance.
    imageRef = resource2.Body('imageRef')
    image = resource2.Body('imageRef')
    #: flavor id of Dedicated Hypervisor instance.
    flavorRef = resource2.Body('flavorRef')
    flavor = resource2.Body('flavorRef')
    #: Networks.
    networks = resource2.Body('networks')
    #: Password for the administrator.
    adminPass = resource2.Body('adminPass')
    admin_pass = resource2.Body('adminPass')
    #: Status of the Dedicated Hypervisor instance.
    status = resource2.Body('status')
    #: detail of baremetal server.
    baremetal_server = resource2.Body('baremetal_server')
    #: Server's availability zone.
    availability_zone = resource2.Body('availability_zone')


class ServerDetail(Server):
    base_path = '/servers/detail'

    # capabilities
    allow_list = True
    allow_get = False
    allow_create = False
    allow_delete = False


class ServerAction(Server):
    resource_key = None
    resources_key = None
    base_path = '/servers/%s/action'

    # capabilities
    allow_list = False
    allow_get = True
    allow_create = True
    allow_delete = False

    vm_id = resource2.Body('vm_id')
    vm_name = resource2.Body('vm_name')
    license_types = resource2.Body('license_types')
    job_id = resource2.Body('job_id')
    status = resource2.Body('status')
    message = resource2.Body('message')
    requested_param = resource2.Body('requested_param')

    def add_license(self, session, server_id, license_types, vm_id=None, vm_name=None):
        uri = self.base_path % server_id
        params = {}
        params["license_types"] = license_types
        if vm_id:
            params["vm_id"] = vm_id
        if vm_name:
            params["vm_name"] = vm_name
        body = { "add-license-to-vm": params }
        resp = session.post(
            uri,
            endpoint_filter=self.service,
            json=body
        )
        self._translate_response(resp, has_body=True)
        return self

    def get_add_license_job(self, session, server_id, job_id):
        uri = self.base_path % server_id
        body = { "get-result-for-add-license-to-vm": { "job_id": job_id } }
        resp = session.post(
            uri,
            endpoint_filter=self.service,
            json=body
        )
        self._translate_response(resp, has_body=True)
        return self
