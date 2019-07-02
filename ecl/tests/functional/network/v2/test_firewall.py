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
import time
from ecl.tests.functional import base


class TestFirewall(base.BaseFunctionalTest):

    def test_01_list_firewall(self):
        firewalls = list(self.conn.network.firewalls(
            status="ACTIVE"))
        print("Total: ", len(firewalls))
        print(firewalls)

        for firewall in firewalls:
            print(firewall.name, " ", firewall.id)

        firewall = firewalls[0]
        self.assertIsInstance(firewall.admin_username, six.string_types)
        # self.assertIsInstance(firewall.availability_zone, six.string_types)
        # self.assertIsInstance(firewall.default_gateway, six.string_types)
        self.assertIsInstance(firewall.description, six.string_types)
        self.assertIsInstance(firewall.firewall_plan_id, six.string_types)
        self.assertIsInstance(firewall.id, six.string_types)
        self.assertIsInstance(firewall.name, six.string_types)
        self.assertIsInstance(firewall.status, six.string_types)
        self.assertIsInstance(firewall.tenant_id, six.string_types)
        self.assertIsInstance(firewall.user_username, six.string_types)

    @classmethod
    def test_02_create_firewall(cls):
        firewall = cls.conn.network.create_firewall(
            firewall_plan_id="4441399b-a3dd-40c0-903f-a02e685f7e8c",
        )
        cls.id = firewall.id
        time.sleep(360)

    def test_03_show_firewall(self):
        firewall = self.conn.network.show_firewall(
            self.id
        )
        print(firewall)
        self.assertIsInstance(firewall.interfaces, list)

    def test_04_update_firewall(self):
        firewall = self.conn.network.update_firewall(
            self.id,
            description="updated description",
            name="sdk_firewall"
        )
        print(firewall)

    def test_05_delete_firewall(self):
        firewall = self.conn.network.delete_firewall(
            self.id
        )

    def test_06_list_firewall(self):
        firewalls = list(self.conn.network.firewalls(
            status="ACTIVE"))
        print("Total: ", len(firewalls))
