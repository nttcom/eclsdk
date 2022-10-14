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

class Api_key(resource2.Resource):
    resource_key = None
    resources_key = None
    base_path = '/keys'
    service = sss_service.SssService()

    # Capabilities
    allow_update = True

    # Properties
    #: User's id whose API key updated.
    user_id = resource2.Body('user_id', alternate_id=True)
    #: New API key(keystone username)
    keystone_name = resource2.Body('keystone_name')
    #: New API secret(keystone password)
    keystone_password = resource2.Body('keystone_password')
    #: Update status. 'Success' for successful update
    status = resource2.Body('status')

    def update(self, session, user_id):
        url = '/keys/%s' % user_id
        resp = session.put(url, endpoint_filter=self.service)
        self._translate_response(resp, has_body=True)
        return self
