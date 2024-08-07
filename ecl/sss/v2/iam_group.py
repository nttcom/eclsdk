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

from ecl.sss import  sss_service
from ecl import resource2


class IAMGroup(resource2.Resource):
    resource_key = None
    resources_key = 'iam_groups'
    base_path = '/iam/groups'

    # Capabilities
    allow_create = True
    allow_delete = True
    allow_list = True
    allow_update = True

    # Properties
    #: The IAM Group ID.
    iam_group_id = resource2.Body('iam_group_id', alternate_id=True)
    #: The IAM Group name.
    iam_group_name = resource2.Body('iam_group_name')
    #: Description of the IAM group.
    description = resource2.Body('description')
    #: IAM Role Object.
    #: * iam_role_id: The IAM Role ID.
    #: * iam_role_name: The IAM Role name.
    iam_roles = resource2.Body('iam_roles')
    #: The IAM Role ID.
    iam_role_id = resource2.Body('iam_role_id')
    #: The IAM Role name.
    iam_role_name = resource2.Body('iam_role_name')
    #: User ID that belongs in the designated IAM Group ID.
    users = resource2.Body('users')
    #: The User ID.
    user_id = resource2.Body('user_id')
    #: The contact ID that the IAM Group belongs.
    contract_id = resource2.Body('contract_id')

    def list(self, session, contract_id):
        """List iam groups by contract id"""

        url = self.base_path + '?contract_id=%s' % contract_id
        resp = session.get(url, endpoint_filter=self.service)
        self._translate_response(resp, has_body=True)
        return self

    def assign_iam_role(self, session, iam_group_id, iam_role_id):
        """Assignment of the IAM Role to the IAM Group."""

        url = self.base_path + '/%s/roles/%s' % (iam_group_id, iam_role_id)
        resp = session.put(url, endpoint_filter=self.service)
        self._translate_response(resp, has_body=True)
        return self

    def delete_assign_iam_role(self, session, iam_group_id, iam_role_id):
        """Delete Assignment of the IAM Role to the IAM Group."""

        url = self.base_path + '/%s/roles/%s' % (iam_group_id, iam_role_id)
        resp = session.delete(url, endpoint_filter=self.service)
        self._translate_response(resp, has_body=False)
        return self

    def list_users(self, session, iam_group_id):
        """Show User list in the designated IAM Group ID."""

        url = self.base_path + '/%s/users' % iam_group_id
        resp = session.get(url, endpoint_filter=self.service)
        self._translate_response(resp, has_body=True)
        return self

    def assign_user(self, session, iam_group_id, user_id):
        """Assignment of the IAM User to the IAM Group."""

        url = self.base_path + '/%s/users/%s' % (iam_group_id, user_id)
        resp = session.put(url, endpoint_filter=self.service)
        self._translate_response(resp, has_body=True)
        return self

    def delete_assign_user(self, session, iam_group_id, user_id):
        """Delete Assignment of the IAM User to the IAM Group."""

        url = self.base_path + '/%s/users/%s' % (iam_group_id, user_id)
        resp = session.delete(url, endpoint_filter=self.service)
        self._translate_response(resp, has_body=False)
        return self
