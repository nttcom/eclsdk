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
    "description": "Example gateway 1 description.",
    "id": "id12345678900",
    "name": "Example port 1",
    "qos_option_id": "qosid12345678",
    "tenant_id": "IDENTIFIER",
    "status": "ACTIVE",
    "mec_service_id": "mecsid12345678",
}


class TestPort(testtools.TestCase):

    def test_basic(self):
        sot = mec.MECGateway()
        self.assertEqual('mec_gateway', sot.resource_key)
        self.assertEqual('mec_gateways', sot.resources_key)
        self.assertEqual('/v2.0/mec_gateways', sot.base_path)
        self.assertEqual('network', sot.service.service_type)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_list)

    def test_make_it(self):
        sot = mec.MECGateway(**EXAMPLE)
        self.assertEqual(EXAMPLE['description'], sot.description)
        self.assertEqual(EXAMPLE['id'], sot.id)
        self.assertEqual(EXAMPLE['name'], sot.name)
        self.assertEqual(EXAMPLE['qos_option_id'], sot.qos_option_id)
        self.assertEqual(EXAMPLE['status'], sot.status)
        self.assertEqual(EXAMPLE['tenant_id'], sot.tenant_id)
        self.assertEqual(EXAMPLE['mec_service_id'], sot.mec_service_id)
