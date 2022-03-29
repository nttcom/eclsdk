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


class Flavor(resource2.Resource):
    resources_key = "flavors"
    resource_key = "flavor"
    base_path = '/flavors'
    service = mrdb_service.MrdbService()

    # Capabilities
    allow_get = True
    allow_list = True

    # Properties
    #: UUID of the flavor.
    id = resource2.Body('id')
    #: Name of the flavor.
    name = resource2.Body('name')
    #: Core of the flavor.
    core = resource2.Body('core', type=int)
    #: Memory of the flavor. Unit: GB.
    memory = resource2.Body('memory', type=int)
