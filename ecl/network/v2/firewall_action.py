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

from ecl.network import network_service
from ecl import resource2


class FirewallAction(resource2.Resource):
    service = network_service.NetworkService("v2.0")
    base_path = ('/' + service.version +
                 "/firewalls/%(firewall_id)s/%(action)s")

    # Capabilities
    allow_get = True
    allow_create = True

    # Properties
    #: New password reset
    new_password = resource2.Body("new_password")
    #: Username of the firewall
    username = resource2.Body("username")

    def reboot(self, session, firewall_id, type):
        """Reboot firewall."""

        uri = self.base_path % {"firewall_id": firewall_id,
                                "action": "reboot"}
        resp = session.post(
            uri, endpoint_filter=self.service,
            json={"type": type}
        )
        self._translate_response(resp, has_body=False)
        return self

    def reset_password(self, session, firewall_id, username):
        """Reset password of firewall instance."""

        uri = self.base_path % {"firewall_id": firewall_id,
                                "action": "reset_password"}
        resp = session.post(
            uri, endpoint_filter=self.service,
            json={"username": username}
        )
        self._translate_response(resp, has_body=True)
        return self
