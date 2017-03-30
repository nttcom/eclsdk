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

from ecl.rca import rca_service
from ecl import resource2

class Version(resource2.Resource):
    resource_key = 'version'
    resources_key = 'versions'
    base_path = ''
    service = rca_service.RcaService(
        version=rca_service.RcaService.UNVERSIONED
    )

    # capabilities
    allow_list = True
    allow_get = True

    # Properties
    #: Version identifier included in API URL.
    id = resource2.Body('id')
    #: List of API endpoint link.
    links = resource2.Body('links')
    #: Version support status. Valid values are CURRENT or SUPPORTED.
    #: CURRENT is newest stable version. SUPPORTED is old supported version.
    status = resource2.Body('status')

    def get_version(self, session):
        url = self.base_path + '/v1.0'
        resp = session.get(
            url, headers={"Accept": "application/json"}, endpoint_filter=self.service
        )
        self._translate_response(resp, has_body=True)
        return self

    def list_version(self, session):
        url = self.base_path
        resp = session.get(
            url, headers={"Accept": "application/json"}, endpoint_filter=self.service
        )
        resp = resp.json()[self.resources_key]

        for data in resp:
            version = self.existing(**data)
            yield version