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

class Role(resource2.Resource):
    resource_key = None
    resources_key = None
    base_path = '/roles'
    service = sss_service.SssService()

    # Capabilities
    allow_create = True
    allow_delete = True
    put_create = False

    # Properties
    #: User's id who was attached with the role.
    user_id = resource2.Body('user_id')
    #: Region id which the tenant belongs to.
    region_id = resource2.Body('region_id')
    #: Region name which the tenant belongs to.
    region_name = resource2.Body('region_name')
    #: Tenant's id which is attached with the role.
    tenant_id = resource2.Body('tenant_id')
    #: Tenant's name which is attached with the role.
    tenant_name = resource2.Body('tenant_name')
    #: Attached role's name.
    role_name = resource2.Body('role_name', alternate_id=True)

    def delete(self, session, tenant_id, user_id):
        """Delete role with given tenant id and user id"""

        url = '/roles/tenants/%s/users/%s' % (tenant_id, user_id)
        resp = session.delete(url, endpoint_filter=self.service)
        self._translate_response(resp, has_body=False)
        return self



