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

from ecl.network.v2 import network

IDENTIFIER = 'IDENTIFIER'
EXAMPLE = {
    "admin_state_up": True,
    "description": "Example network 1 description.",
    "id": IDENTIFIER,
    "name": "Example network 1",
    "plane": "data",
    "shared": True,
    "status": "ACTIVE",
    "subnets": [
      IDENTIFIER,
      IDENTIFIER
    ],
    "tags": {
      "keyword1": "value1",
      "keyword2": "value2"
    },
    "tenant_id": IDENTIFIER
}


class TestNetwork(testtools.TestCase):

    def test_basic(self):
        sot = network.Network()
        self.assertEqual('network', sot.resource_key)
        self.assertEqual('networks', sot.resources_key)
        self.assertEqual('/networks', sot.base_path)
        self.assertEqual('network', sot.service.service_type)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)

    def test_make_it(self):
        sot = network.Network(**EXAMPLE)
        self.assertTrue(sot.admin_state_up)
        self.assertTrue(sot.shared)
        self.assertEqual(EXAMPLE['id'], sot.id)
        self.assertEqual(EXAMPLE['name'], sot.name)
        self.assertEqual(EXAMPLE['tenant_id'], sot.project_id)
        self.assertEqual(EXAMPLE['status'], sot.status)
        self.assertEqual(EXAMPLE['subnets'], sot.subnet_ids)
        self.assertEqual(EXAMPLE['description'], sot.description)
        self.assertEqual(EXAMPLE['tags'], sot.tags)
        self.assertEqual(EXAMPLE['plane'], sot.plane)
