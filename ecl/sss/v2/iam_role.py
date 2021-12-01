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


class IAMRole(resource2.Resource):
    resource_key = None
    resources_key = 'iam_roles'
    base_path = '/iam/roles'

    # Capabilities
    allow_create = True
    allow_delete = True
    allow_list = True
    allow_get = True

    # Properties
    #: The IAM Role's ID.
    iam_role_id = resource2.Body('iam_role_id', alternate_id=True)
    #: The IAM Role's name.
    iam_role_name = resource2.Body('iam_role_name')
    #: Description of the IAM Role.
    description = resource2.Body('description')
    #: Whitelist rules of API exectution.
    resources = resource2.Body('resources')
    #: The contact ID that the IAM Role belongs.
    contract_id = resource2.Body('contract_id')

    def list(self, session, contract_id):
        """List IAM Role list in the designated contract."""

        url = self.base_path + '?contract_id=%s' % contract_id
        resp = session.get(url, endpoint_filter=self.service)
        self._translate_response(resp, has_body=True)
        return self
