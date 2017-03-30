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

from ecl.network.v2 import vpn

IDENTIFIER = 'IDENTIFIER'
EXAMPLE = {
    "description": "vpn connectivity provider",
    "id": IDENTIFIER,
    "name": "test-VPN",
    "zone": "test-zone"
}


class TestVPNService(testtools.TestCase):

    def test_basic(self):
        sot = vpn.VPNService()
        self.assertEqual('vpn_service', sot.resource_key)
        self.assertEqual('vpn_services', sot.resources_key)
        self.assertEqual('/vpn_services', sot.base_path)
        self.assertEqual('network', sot.service.service_type)
        self.assertFalse(sot.allow_create)
        self.assertTrue(sot.allow_get)
        self.assertFalse(sot.allow_update)
        self.assertFalse(sot.allow_delete)
        self.assertTrue(sot.allow_list)

    def test_make_it(self):
        sot = vpn.VPNService(**EXAMPLE)
        self.assertEqual(EXAMPLE['description'], sot.description)
        self.assertEqual(EXAMPLE['id'], sot.id)
        self.assertEqual(EXAMPLE['name'], sot.name)
        self.assertEqual(EXAMPLE['zone'], sot.zone)
