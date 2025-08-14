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

from ecl.network.v2 import wasabi_gateways

IDENTIFIER = 'IDENTIFIER'
EXAMPLE = {
    "id": IDENTIFIER,
    "common_function_gateway": IDENTIFIER,
    "description": "Example wasabi gateway 1 description.",
    "name": "Example wasabi gateway 1",
    "status": "ACTIVE",
    "tenant_id": IDENTIFIER
}


class TestWasabiGateways(testtools.TestCase):

    def test_basic(self):
        sot = wasabi_gateways.WasabiGateways()
        self.assertEqual('wasabi_gateway', sot.resource_key)
        self.assertEqual('wasabi_gateways', sot.resources_key)
        self.assertEqual('/wasabi_gateways', sot.base_path)
        self.assertEqual('wasabi_gateway', sot.service.service_type)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)

    def test_make_it(self):
        sot = wasabi_gateways.WasabiGateways(**EXAMPLE)
        self.assertEqual(EXAMPLE['id'], sot.id)
        self.assertEqual(EXAMPLE['common_function_gateway'], sot.common_function_gateway)
        self.assertEqual(EXAMPLE['description'], sot.description)
        self.assertEqual(EXAMPLE['name'], sot.name)
        self.assertEqual(EXAMPLE['status'], sot.status)
        self.assertEqual(EXAMPLE['tenant_id'], sot.project_id)
