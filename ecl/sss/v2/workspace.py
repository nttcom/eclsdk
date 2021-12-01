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

from ecl.sss import sss_service
from ecl import resource2

class Workspace(resource2.Resource):
    resource_key = None
    resources_key = 'workspaces'
    base_path = '/workspaces'
    service = sss_service.SssService()

    # Capabilities
    allow_create = True
    allow_get = True
    allow_list = True
    allow_delete = True
    allow_update = True

    # Properties
    #: Contract which owns these workspaces.
    contract_id = resource2.Body('contract_id')
    #: ID of the workspace
    workspace_id = resource2.Body('workspace_id')
    #: Name of the workspace. Workspace name is also a unique identifier of workspaces.
    workspace_name = resource2.Body('workspace_name')
    #: Description of the workspace.
    description = resource2.Body('description')
    #: Workspace created time.
    start_time = resource2.Body('start_time')
    #: Array of region information where tenants can be created.
    regions = resource2.Body('regions')
    #: Region which the workspace belongs to.
    regions.region_name	 = resource2.Body('regions.region_name	')
    #: The tenant ID that the tenant belongs.
    regions.tenant_id = resource2.Body('regions.tenant_id')
    #: An array of user information that has a workspace role in the workspace.
    workspaces = resource2.Body('workspaces')
    #: User list.
    users = resource2.Body('users')
    #: ID of the users who have access to this workspace.
    users.user_id = resource2.Body('users.user_id')
    #: Contract which owns the workspace.
    users.contract_id = resource2.Body('users.contract_id')
    #: This user is contract owner / or not.
    users.contract_owner = resource2.Body('users.contract_owner')
