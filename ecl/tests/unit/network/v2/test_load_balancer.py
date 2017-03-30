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

import testtools

from ecl.network.v2 import load_balancer

IDENTIFIER = 'IDENTIFIER'
EXAMPLE = {
    "admin_username": "admin",
    "admin_password": "pass",
    "availability_zone": "zoneA",
    "default_gateway": None,
    "description": "test-descr",
    "id": IDENTIFIER,
    "interfaces": [
      {
        "id": IDENTIFIER,
        "ip_address": "100.100.100.100",
        "name": "Interface 1/1",
        "network_id": IDENTIFIER,
        "slot_number": 1,
        "status": "ACTIVE",
        "type": "user",
        "virtual_ip_address": None,
        "virtual_ip_properties": None
      },
      {
        "id": IDENTIFIER,
        "ip_address": "100.100.100.100",
        "name": "Interface 1/1",
        "network_id": IDENTIFIER,
        "slot_number": 2,
        "status": "ACTIVE",
        "type": "user",
        "virtual_ip_address": None,
        "virtual_ip_properties": None
      },
      {
        "id": IDENTIFIER,
        "ip_address": "100.100.100.100",
        "name": "Interface 1/1",
        "network_id": IDENTIFIER,
        "slot_number": 3,
        "status": "ACTIVE",
        "type": "user",
        "virtual_ip_address": None,
        "virtual_ip_properties": None
      },
      {
        "id": IDENTIFIER,
        "ip_address": "100.100.100.100",
        "name": "Interface 1/1",
        "network_id": IDENTIFIER,
        "slot_number": 4,
        "status": "ACTIVE",
        "type": "user",
        "virtual_ip_address": None,
        "virtual_ip_properties": None
      },
    ],
    "load_balancer_plan_id": IDENTIFIER,
    "name": "test-name",
    "status": "ACTIVE",
    "tenant_id": IDENTIFIER,
    "user_username": "user",
    "user_password": "pass",
  }


class TestLoadBalancer(testtools.TestCase):

    def test_basic(self):
        sot = load_balancer.LoadBalancer()
        self.assertEqual('load_balancer', sot.resource_key)
        self.assertEqual('load_balancers', sot.resources_key)
        self.assertEqual('/load_balancers', sot.base_path)
        self.assertEqual('network', sot.service.service_type)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)

    def test_make_it(self):
        sot = load_balancer.LoadBalancer(**EXAMPLE)
        self.assertEqual(EXAMPLE['admin_username'], sot.admin_username)
        self.assertEqual(EXAMPLE['availability_zone'], sot.availability_zone)
        self.assertEqual(EXAMPLE['default_gateway'], sot.default_gateway)
        self.assertEqual(EXAMPLE['description'], sot.description)
        self.assertEqual(EXAMPLE['id'], sot.id)
        self.assertEqual(EXAMPLE['interfaces'], sot.interfaces)
        self.assertEqual(EXAMPLE['tenant_id'], sot.tenant_id)
        self.assertEqual(EXAMPLE['load_balancer_plan_id'], 
                         sot.load_balancer_plan_id)
        self.assertEqual(EXAMPLE['name'], sot.name)
        self.assertEqual(EXAMPLE['status'], sot.status)
        self.assertEqual(EXAMPLE['user_username'], sot.user_username)
