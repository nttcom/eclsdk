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


class DatabaseVersion(resource2.Resource):
    resources_key = "database_versions"
    resource_key = "database_versions"
    service = mrdb_service.MrdbService()
    base_path = '/' + service.version + '/database_versions'

    # Capabilities
    allow_get = True
    allow_list = True

    # Properties
    #: UUID of the database version.
    id = resource2.Body('id')
    #: Name of the database version.
    name = resource2.Body('name')
    #: Dbms name of the database version.
    dbms_name = resource2.Body('dbms_name')
    #: Major version of the database version.
    major_version = resource2.Body('major_version')
