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


class User(resource2.Resource):
    resource_key = "user"
    resources_key = "users"
    base_path = '/instances/%(instance_id)s/users'
    service = database_service.DatabaseService()

    # _query_mapping = resource2.QueryParameters()

    # Capabilities
    allow_create = True
    allow_delete = True
    allow_list = True

    allow_update = False
    allow_get = False

    # Properties
    #: User's name of Database instance.
    name = resource2.Body('name', alternate_id=True)

    #: Allowed access host of user.
    host = resource2.Body('host')

    #: Relevant database of this user.
    databases = resource2.Body('databases', type=list)

    #: User's password of Database instance.
    #: This parameter is only used in instance creation.
    password = resource2.Body('password')

    #: ID of instance associated with this user
    instance_id = resource2.URI('instance_id')
