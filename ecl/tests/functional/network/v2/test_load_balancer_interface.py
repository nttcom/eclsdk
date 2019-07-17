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


class TestLoadBalancerInterface(base.BaseFunctionalTest):
    def test_01_load_balancer_interfaces(self):
        load_balancer_interfaces = list(self.conn.network.load_balancer_interfaces(

        ))
        print(load_balancer_interfaces)

    def test_02_show_load_balancer_interface(self):
        interface = self.conn.network.show_load_balancer_interface(
            "0b2d4f07-313c-4bee-a1dd-4982ccef9bb1"
        )
        print(interface)
        # self.assertIsInstance(interface.description, six.string_types)
        self.assertIsInstance(interface.id, six.string_types)
        # self.assertIsInstance(interface.ip_address, six.string_types)
        self.assertIsInstance(interface.load_balancer_id, six.string_types)
        self.assertIsInstance(interface.name, six.string_types)
        # self.assertIsInstance(interface.network_id, six.string_types)
        # self.assertIsInstance(interface.slot_number, six.string_types)
        self.assertIsInstance(interface.status, six.string_types)
        self.assertIsInstance(interface.tenant_id, six.string_types)
        # self.assertIsInstance(interface.virtual_ip_address, six.string_types)
        # self.assertIsInstance(interface.virtual_ip_properties, dict)

    def test_03_update_load_balancer_interface(self):
        interface = self.conn.network.update_load_balancer_interface(
            "0b2d4f07-313c-4bee-a1dd-4982ccef9bb1",
            description="updated"
        )
        print(interface)
        self.assertIsInstance(interface.description, six.string_types)
