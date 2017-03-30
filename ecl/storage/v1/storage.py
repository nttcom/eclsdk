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

from ecl import utils
from ecl.storage import storage_service

from ecl import resource2
from ecl.storage import storage_service


class Storage(resource2.Resource):
    resource_key = 'virtual_storage'
    resources_key = 'virtual_storages'
    base_path = '/virtual_storages'

    service = storage_service.StorageService()

    # capabilities
    allow_list = True
    allow_get = True
    allow_create = True
    allow_delete = True
    allow_update = True

    # Properties
    #: id of storage(UUID)
    id = resource2.Body('id')
    #: Network id(UUID) of storage
    network_id = resource2.Body('network_id')
    #: Subnet id(UUID) of storage
    subnet_id = resource2.Body('subnet_id')
    #: The pool of IP addresses for storage
    ip_addr_pool = resource2.Body('ip_addr_pool', type=dict)
    #: static routes settings of storage
    host_routes = resource2.Body('host_routes', type=list)
    #: volume type id(UUID) of storage
    volume_type_id = resource2.Body('volume_type_id')
    #: name of storage
    name = resource2.Body('name')
    #: description of storage
    description = resource2.Body('description')
    #: status of storage
    status = resource2.Body('status')
    #: creation timestamp of storage
    created_at = resource2.Body('created_at')
    #: update timestamp of storage
    updated_at = resource2.Body('updated_at')
    #: error description of storage
    error_message = resource2.Body('error_message')

    def create(self, session, **attrs):
        body = {"virtual_storage": attrs}
        resp = session.post(
            self.base_path, endpoint_filter=self.service,
            json=body,
            headers={"Accept": "application/json"}
        )
        self._translate_response(resp, has_body=True)
        return self

    def update(self, session, storage_id, has_body=True, **attrs):
        uri = utils.urljoin(self.base_path, storage_id)
        body = {"virtual_storage": attrs}
        args = {'json': body}
        resp = session.put(uri, endpoint_filter=self.service, **args)
        self._translate_response(resp, has_body)
        return self


class StorageDetail(Storage):
    base_path = '/virtual_storages/detail'
    allow_get = False
    allow_create = False
    allow_delete = False
    allow_update = False
