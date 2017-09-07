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


class Datastore(resource2.Resource):
    resource_key = None
    resources_key = 'datastores'
    base_path = '/datastores'
    service = database_service.DatabaseService()

    # capabilities
    allow_list = True

    _query_mapping = resource2.QueryParameters()

    # Properties
    #: The ID of this datastore
    id = resource2.Body('id')
    #: The name of this datastore.
    name = resource2.Body('name')
    #: Size of the disk this datastore offers. *Type: int*
    default_version = resource2.Body('default_version')
    #: The amount of RAM (in MB) this datastore offers. *Type: int*
    versions = resource2.Body('versions')
    #: Links pertaining to this datastore. This is a list of dictionaries,
    #: each including keys ``href`` and ``rel``.
    links = resource2.Body('links')
