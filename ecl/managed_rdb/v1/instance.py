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

from ecl.managed_rdb import mrdb_service
from ecl import exceptions
from ecl import resource2


class Instance(resource2.Resource):
    resources_key = "instances"
    resource_key = "instance"
    base_path = '/instances'
    service = mrdb_service.MrdbService()

    # Capabilities
    allow_get = True
    allow_list = True
    allow_delete = True

    # Properties
    #: UUID of the mRDB instance.
    id = resource2.Body('id')
    #: Tenant id of the mRDB instance.
    tenant_id = resource2.Body('tenant_id')
    #: Name of the mRDB instance.
    name = resource2.Body('name')
    #: Description of the mRDB instance.
    description = resource2.Body('description')
    #: Flavor of the mRDB instance.
    flavor = resource2.Body('flavor', type=dict)
    #: Database version of the mRDB instance.
    database_version = resource2.Body('database_version', type=dict)
    #: Storage type of the mRDB instance.
    storage_type = resource2.Body('storage_type', type=dict)
    #: High availability of the mRDB instance.
    high_availability = resource2.Body('high_availability', type=bool)
    #: Status of the mRDB instance.
    status = resource2.Body('status')
    #: Task type of the mRDB instance.
    task_type = resource2.Body('task_type')
    #: Task state of the mRDB instance.
    task_state = resource2.Body('task_state')
    #: Monitoring state of the mRDB instance.
    monitoring_state = resource2.Body('monitoring_state')
    #: Nodes of the mRDB instance.
    nodes = resource2.Body('nodes', type=list)
    #: Network of the mRDB instance.
    network = resource2.Body('network', type=dict)
    #: Metadata of the mRDB instance.
    metadata = resource2.Body('metadata', type=dict)
    #: Links of the mRDB instance.
    links = resource2.Body('links', type=list)
    #: Created of the mRDB instance.
    created = resource2.Body('created')
    #: Admin password of the mRDB instance.
    admin_password = resource2.Body('admin_password')

    def create(self, session, **attrs):
        body = {"instance": attrs}
        resp = session.post(
            self.base_path,
            endpoint_filter=self.service,
            json=body,
            headers={"Accept": "application/json"}
        )
        self._translate_response(resp)
        return self

    def update(self, session, instance_id, **attrs):
        url = "%s/%s" % (self.base_path, instance_id)
        body = {"instance": attrs}
        resp = session.patch(
            url,
            endpoint_filter=self.service,
            json=body,
            headers={"Accept": "application/json"}
        )
        self._translate_response(resp)
        return self


class InstanceDetail(Instance):
    base_path = '/instances/detail'

    # capabilities
    allow_get = False
    allow_list = True
    allow_create = False
    allow_delete = False
    allow_update = False
    patch_update = False


class InstanceAction(resource2.Resource):
    base_path = '/instances/%(instance_id)s/action'
    service = mrdb_service.MrdbService()

    # Properties
    #: Admin password of the mRDB instance.
    admin_password = resource2.Body('admin_password')

    def change_password(self, session, instance_id, **attrs):
        """Change the password to the given password."""
        uri = self.base_path % {"instance_id": instance_id}
        body = {'change-password': attrs}
        resp = session.post(
            uri,
            endpoint_filter=self.service,
            json=body,
            headers={"Accept": "application/json"}
        )
        self._translate_response(resp)
        return self
