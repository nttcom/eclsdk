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

from ecl.database import database_service
from ecl import resource2
from ecl import exceptions


class Database(resource2.Resource):
    resource_key = "database"
    resources_key = "databases"
    base_path = '/instances/%(instance_id)s/databases'
    service = database_service.DatabaseService()

    # Capabilities
    allow_create = True
    allow_delete = True
    allow_list = True

    allow_update = False
    allow_get = False

    # Properties
    #: Name of Database.
    name = resource2.Body('name', alternate_id=True)
    #: Character set of Database.
    character_set = resource2.Body('character_set')
    #: Collate of Database.
    collate = resource2.Body('collate')
    #: ID of instance associated with this database
    instance_id = resource2.URI('instance_id')

    def create(self, session, instance_id, **attrs):
        base = self.base_path % {"instance_id": instance_id}
        body = {"databases": [attrs]}
        resp = session.post(base, endpoint_filter=self.service, json=body,
                            headers={"Accept": "application/json"})
        self._translate_response(resp, has_body=False)
        return self
