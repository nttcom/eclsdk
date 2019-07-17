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


class TestLoadBalancerPlan(base.BaseFunctionalTest):

    def test_01_list_LB_plans(self):
        plans = list(self.conn.network.load_balancer_plans(
            version="11.0-67.12",
            vendor="citrix"
        ))
        print(plans)

    def test_02_show_LB_plan(self):
        plan = self.conn.network.get_load_balancer_plan(
            "0631eb6d-f4cd-4a18-b255-1fe603c2c3ec"
        )
        print(plan)
        self.assertIsInstance(plan.description, six.string_types)
        self.assertIsInstance(plan.id, six.string_types)
        self.assertIsInstance(plan.name, six.string_types)
        self.assertIsInstance(plan.model, dict)
        self.assertIsInstance(plan.vendor, six.string_types)
        self.assertIsInstance(plan.version, six.string_types)

    def test_03_find_LB_plan(self):
        plan = self.conn.network.find_load_balancer_plan(
            "0631eb6d-f4cd-4a18-b255-1fe603c2c3ec"
        )
        print(plan)
        self.assertIsInstance(plan.description, six.string_types)
        self.assertIsInstance(plan.id, six.string_types)
        self.assertIsInstance(plan.name, six.string_types)
        self.assertIsInstance(plan.model, dict)
        self.assertIsInstance(plan.vendor, six.string_types)
        self.assertIsInstance(plan.version, six.string_types)
