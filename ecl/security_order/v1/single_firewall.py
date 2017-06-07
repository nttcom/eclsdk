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

from ecl.security_order import security_order_service
from ecl import resource2
from ecl import exceptions
from ecl import utils


class SingleFirewall(resource2.Resource):
    resource_key = None
    resources_key = None
    base_path = '/API/SoEntryFGS'
    service = security_order_service.SecurityOrderService()

    # Capabilities
    allow_create = True
    allow_get = True
    allow_delete = True
    allow_list = True
    allow_update = True

    # Properties
    #: Tenant ID of the owner (UUID).
    tenant_id = resource2.Body('tenant_id')
    #:
    gt_host = resource2.Body('gt_host')
    #:
    sokind = resource2.Body('sokind', alternate_id=True)
    #:
    locale = resource2.Body('locale')

    def list(self, session, locale=None):
        tenant_id = session.get_project_id()
        uri = '/API/ScreenEventFGSDeviceGet?tenant_id=%s' % tenant_id
        if locale is not None:
            uri += '&locale=%s' % locale
        headers = {'Content-Type': 'application/json'}
        resp = session.get(uri, endpoint_filter=self.service, headers=headers)
        self._translate_response(resp, has_body=True)
        return self
