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

from ecl.security_portal.v1 import security_device as _sd
from ecl import proxy2


class Proxy(proxy2.BaseProxy):
    def security_devices(self):
        """Listing security devices associated with specific tenant.

        :return: List security devices.
        :rtype: :class:`~ecl.security_portal.v1.security_device.SecurityDevice`
        """
        return list(self._list(_sd.SecurityDevice, paginated=False,
                               tenantid=self.session.get_project_id(),
                               usertoken=self.session.get_token()))

    def get_security_device(self, server_id):
        """Show security device details associated with specific tenant.

        :param string server_id: Server ID registered in Openstack(UUID).
        :return: One security device.
        :rtype: :class:`~ecl.security_portal.v1.security_device.SecurityDevice`
        """
        sd = _sd.SecurityDevice()
        return sd.get(self.session, server_id)
