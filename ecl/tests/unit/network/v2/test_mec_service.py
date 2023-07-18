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
    "description": "Example service 1 description.",
    "id": "id12345678900",
    "name": "Example port 1",
    "tenant_id": "IDENTIFIER",
    "zone": "Name",
}


class TestPort(testtools.TestCase):

    def test_basic(self):
        sot = mec.MECService()
        self.assertEqual('mec_service', sot.resource_key)
        self.assertEqual('mec_services', sot.resources_key)
        self.assertEqual('/v2.0/mec_services', sot.base_path)
        self.assertEqual('network', sot.service.service_type)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_list)

    def test_make_it(self):
        sot = mec.MECService(**EXAMPLE)
        self.assertEqual(EXAMPLE['description'], sot.description)
        self.assertEqual(EXAMPLE['id'], sot.id)
        self.assertEqual(EXAMPLE['name'], sot.name)
        self.assertEqual(EXAMPLE['zone'], sot.zone)
        self.assertEqual(EXAMPLE['tenant_id'], sot.tenant_id)
