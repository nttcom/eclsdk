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

from ecl.dedicated_hypervisor import dedicated_hypervisor_service
from ecl import resource2


class License(resource2.Resource):
    resources_key = "licenses"
    resource_key = "license"
    base_path = '/licenses'
    service = dedicated_hypervisor_service.DedicatedHypervisorService()

    # Capabilities
    allow_list = True
    allow_create = True
    allow_delete = True

    _query_mapping = resource2.QueryParameters("license_type")

    # Properties
    #: id of Guest Image license.
    id = resource2.Body('id')
    #: license key.
    key = resource2.Body('key')
    #: date the license assigned from.
    assigned_from = resource2.Body('assigned_from')
    #: expiration date for the license.
    expires_at = resource2.Body('expires_at')
    #: license_type of the license
    license_type = resource2.Body('license_type')

    def create(self, session, l_type):
        url = self.base_path
        resp = session.post(url, endpoint_filter = self.service,
                            json={"license_type": l_type})
        self._translate_response(resp, has_body=True)
        return self
