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

from ecl.network.v2 import port

IDENTIFIER = 'IDENTIFIER'
EXAMPLE = {
    "admin_state_up": True,
    "allowed_address_pairs": [],
    "description": "Example port 1 description.",
    "device_id": "IDENTIFIER",
    "device_owner": "compute:test-device1",
    "fixed_ips": [
      {
        "ip_address": "10.10.10.10",
        "subnet_id": IDENTIFIER
      }
    ],
    "mac_address": "test-mac",
    "name": "Example port 1",
    "network_id": IDENTIFIER,
    "segmentation_id": 0,
    "segmentation_type": "flat",
    "tags": {
      "keyword1": "value1",
      "keyword2": "value2"
    },
    "tenant_id": IDENTIFIER,
    "status": "ACTIVE",
}


class TestPort(testtools.TestCase):

    def test_basic(self):
        sot = port.Port()
        self.assertEqual('port', sot.resource_key)
        self.assertEqual('ports', sot.resources_key)
        self.assertEqual('/ports', sot.base_path)
        self.assertEqual('network', sot.service.service_type)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)

    def test_make_it(self):
        sot = port.Port(**EXAMPLE)
        self.assertTrue(sot.admin_state_up)
        self.assertEqual('UP', sot.admin_state)
        self.assertEqual(EXAMPLE['allowed_address_pairs'],
                         sot.allowed_address_pairs)
        self.assertEqual(EXAMPLE['description'], sot.description)
        self.assertEqual(EXAMPLE['device_id'], sot.device_id)
        self.assertEqual(EXAMPLE['device_owner'], sot.device_owner)
        self.assertEqual(EXAMPLE['fixed_ips'], sot.fixed_ips)
        self.assertEqual(EXAMPLE['mac_address'], sot.mac_address)
        self.assertEqual(EXAMPLE['name'], sot.name)
        self.assertEqual(EXAMPLE['network_id'], sot.network_id)
        self.assertEqual(EXAMPLE['segmentation_id'], sot.segmentation_id)
        self.assertEqual(EXAMPLE['segmentation_type'], sot.segmentation_type)
        self.assertEqual(EXAMPLE['tags'], sot.tags)
        self.assertEqual(EXAMPLE['tenant_id'], sot.project_id)
        self.assertEqual(EXAMPLE['status'], sot.status)
