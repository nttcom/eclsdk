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

import six
from ecl.tests.functional import base


class TestFirewallInterface(base.BaseFunctionalTest):
    def test_01_list_interface(self):
        interfaces = list(self.conn.network.firewall_interfaces())
        interface = interfaces[0]
        self.assertIsInstance(interface.firewall_id, six.string_types)
        self.assertIsInstance(interface.id, six.string_types)
        self.assertIsInstance(interface.name, six.string_types)
        self.assertIsInstance(interface.status, six.string_types)
        self.assertIsInstance(interface.tenant_id, six.string_types)

    def test_02_show_interface(self):
        interface = self.conn.network.show_firewall_interface(
            "a96d13c3-6f82-4dee-9d8f-3dc3abdee81b"
        )
        self.assertIsInstance(interface.firewall_id, six.string_types)
        self.assertIsInstance(interface.id, six.string_types)
        self.assertIsInstance(interface.name, six.string_types)
        self.assertIsInstance(interface.status, six.string_types)
        self.assertIsInstance(interface.tenant_id, six.string_types)

    def test_03_update_interface(self):
        interface = self.conn.network.update_firewall_interface(
            "fca334de-0d13-4a94-ab3d-ef1b2d389573",
            description="new description"
        )
        self.assertIsInstance(interface.description, six.string_types)
        self.assertIsInstance(interface.firewall_id, six.string_types)
        self.assertIsInstance(interface.id, six.string_types)
        self.assertIsInstance(interface.name, six.string_types)
        self.assertIsInstance(interface.status, six.string_types)
        self.assertIsInstance(interface.tenant_id, six.string_types)
