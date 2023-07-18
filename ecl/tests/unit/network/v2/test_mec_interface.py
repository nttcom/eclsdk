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

from ecl.network.v2 import mec

EXAMPLE = {
    "description": "Example interface 1 description.",
    "id": "id12345678900",
    "mec_gw_id": "mecgid12345678",
    "name": "Example port 1",
    "status": "ACTIVE",
    "tenant_id": "IDENTIFIER",
    "primary": {
        "bgp_peer_ip": "192.168.1.11",
        "bgp_router_id": "192.168.1.12",
        "ip_address": "192.168.1.1/24",
    },
    "secondary": {
        "bgp_peer_ip": "192.168.1.11",
        "bgp_router_id": "192.168.1.12",
        "ip_address": "192.168.1.1/24",
    },
}


class TestPort(testtools.TestCase):

    def test_basic(self):
        sot = mec.MECInterface()
        self.assertEqual('mec_interface', sot.resource_key)
        self.assertEqual('mec_interfaces', sot.resources_key)
        self.assertEqual('/v2.0/mec_interfaces', sot.base_path)
        self.assertEqual('network', sot.service.service_type)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_list)

    def test_make_it(self):
        sot = mec.MECInterface(**EXAMPLE)
        self.assertEqual(EXAMPLE['description'], sot.description)
        self.assertEqual(EXAMPLE['id'], sot.id)
        self.assertEqual(EXAMPLE['mec_gw_id'], sot.mec_gw_id)
        self.assertEqual(EXAMPLE['name'], sot.name)
        self.assertEqual(EXAMPLE['status'], sot.status)
        self.assertEqual(EXAMPLE['tenant_id'], sot.tenant_id)
        self.assertEqual(EXAMPLE['primary'], sot.primary)
        self.assertEqual(EXAMPLE['secondary'], sot.secondary)
