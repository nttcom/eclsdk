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
from ecl import resource2


class StorageType(resource2.Resource):
    resources_key = "storage_types"
    service = mrdb_service.MrdbService()
    base_path = '/' + service.version + '/storage_types'

    # Capabilities
    allow_list = True

    # Properties
    #: Name of the storage type.
    name = resource2.Body('name')
    #: Type of the storage type.
    type = resource2.Body('type')
    #: Iops of the storage type.
    iops = resource2.Body('iops', type=int)
    #: Size of the storage type. Unit: GB.
    size = resource2.Body('size', type=int)

    def list(self, session):
        resp = session.get(
            self.base_path,
            endpoint_filter=self.service,
            headers={"Accept": "application/json"}
        )
        resp = resp.json()
        for data in resp[self.resources_key]:
            value = self.existing(**data)
            yield value
