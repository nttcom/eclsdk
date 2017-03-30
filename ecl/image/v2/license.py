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

from ecl.image import image_service
from ecl import resource2

class License(resource2.Resource):
    service = image_service.ImageService()
    base_path = '/' + service.version + '/extension/license_switch/types'

    # Properties
    #: ("WindowsServer_2012R2_Standard_64_ComLicense",
    #: "WindowsServer_2012_Standard_64_ComLicense",
    #: "WindowsServer_2008R2_Enterprise_64_ComLicense",
    #: "WindowsServer_2008R2_Standard_64_ComLicense",
    #: "Red_Hat_Enterprise_Linux_7_64bit_BYOL")
    license_switch_types = resource2.Body('license_switch_types')

    def list(self, session):
        """List image license switch types."""

        resp = session.get(self.base_path,
                           headers={"Accept": "application/json"},
                           endpoint_filter=self.service
                           )
        self._translate_response(resp, has_body=True)
        return self