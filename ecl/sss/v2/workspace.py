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
    #: User list.
    users = resource2.Body('users')

    def add_workspace_role_assignment(self, session, user_id, workspace_id):
        """Add role between user and workspace."""

        url = '/workspace-roles'
        resp = session.post(url, endpoint_filter=self.service)
        self._translate_response(resp, has_body=True)
        return self

    def delete_workspace_role_assignment(self, session, workspace_id, user_id):
        """Delete role between user and workspace."""

        url = '/workspace-roles/workspaces/%s/users/%s' % (workspace_id, user_id)
        resp = session.delete(url, endpoint_filter=self.service)
        self._translate_response(resp, has_body=False)
        return self
