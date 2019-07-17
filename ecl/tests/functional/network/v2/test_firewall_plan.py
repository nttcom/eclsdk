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


class TestFirewallPlan(base.BaseFunctionalTest):

    def test_01_list_firewall_plans(self):
        plans = list(self.conn.network.firewall_plans(
            name="Brocade_5600_vRouter_3.5R6S3_4CPU-16GB-8IF",
            vendor="vyatta"
        ))
        print(plans)

    def test_02_show_firewall_plan(self):
        plan = self.conn.network.get_firewall_plan(
            "be90a148-99b9-4f69-b5cb-b03897eebd5d"
        )
        print(plan)
        self.assertIsInstance(plan.description, six.string_types)
        self.assertIsInstance(plan.id, six.string_types)
        self.assertIsInstance(plan.name, six.string_types)
        self.assertIsInstance(plan.vendor, six.string_types)
        self.assertIsInstance(plan.version, six.string_types)

    def test_02_find_firewall_plan(self):
        plan = self.conn.network.find_firewall_plan(
            "be90a148-99b9-4f69-b5cb-b03897eebd5d"
        )
        print(plan)
        self.assertIsInstance(plan.description, six.string_types)
        self.assertIsInstance(plan.id, six.string_types)
        self.assertIsInstance(plan.name, six.string_types)
        self.assertIsInstance(plan.vendor, six.string_types)
        self.assertIsInstance(plan.version, six.string_types)
