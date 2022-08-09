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


class Metadata(resource2.Resource):
    service = mrdb_service.MrdbService()
    base_path = '/' + service.version + '/instances/%(instance_id)s/metadata'

    # Capabilities
    allow_list = True
    allow_update = True

    # Properties
    #: Metadata of the instance.
    metadata = resource2.Body("metadata", type=dict)

    def list(self, session, instance_id):
        resp = session.get(
            self.base_path % {"instance_id": instance_id},
            endpoint_filter=self.service,
            headers={"Accept": "application/json"}
        )
        self._translate_response(resp)
        return self

    def replace(self, session, instance_id, metadata):
        resp = session.put(
            self.base_path % {"instance_id": instance_id},
            endpoint_filter=self.service,
            json={"metadata": metadata},
            headers={"Accept": "application/json"}
        )
        self._translate_response(resp)
        return self
