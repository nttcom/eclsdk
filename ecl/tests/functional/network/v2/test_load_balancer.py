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

import time
import six
from ecl.tests.functional import base


class TestLoadBalancer(base.BaseFunctionalTest):
    def test_09_load_balancers(self):
        load_balancers = list(self.conn.network.load_balancers(
            status="ACTIVE", description="",
            load_balancer_plan_id="29da442c-9a06-4eb3-b3cd-b6b123198214",
            # id="911726aa-a249-4a58-a59b-c233a110649b"
        ))
        print([load_balancer.id for load_balancer in load_balancers])

    @classmethod
    def test_02_create_load_balancer(cls):
        load_balancer = cls.conn.network.create_load_balancer(
            load_balancer_plan_id="29da442c-9a06-4eb3-b3cd-b6b123198214"
        )
        print(load_balancer)
        cls.id = load_balancer.id
        time.sleep(360)

    def test_03_show_load_balancer(self):
        load_balancer = self.conn.network.show_load_balancer(
            self.id
        )
        print(load_balancer)
        self.assertIsInstance(load_balancer.admin_username, six.string_types)
        # self.assertIsInstance(load_balancer.availability_zone, six.string_types)
        # self.assertIsInstance(load_balancer.default_gateway, six.string_types)
        # self.assertIsInstance(load_balancer.description, six.string_types)
        self.assertIsInstance(load_balancer.id, six.string_types)
        self.assertIsInstance(load_balancer.interfaces, list)
        self.assertIsInstance(load_balancer.load_balancer_plan_id, six.string_types)
        self.assertIsInstance(load_balancer.name, six.string_types)
        self.assertIsInstance(load_balancer.status, six.string_types)
        self.assertIsInstance(load_balancer.status, six.string_types)
        self.assertIsInstance(load_balancer.tenant_id, six.string_types)
        self.assertIsInstance(load_balancer.user_username, six.string_types)

    def test_04_update_load_balancer(self):
        # self.id = "911726aa-a249-4a58-a59b-c233a110649b"
        load_balancer = self.conn.network.update_load_balancer(
            self.id,
            description="updated"
        )
        print(load_balancer)

    def test_05_delete_load_balancer(self):
        # self.id = "911726aa-a249-4a58-a59b-c233a110649b"
        self.conn.network.delete_load_balancer(
            self.id
        )
