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

import  testtools
from ecl.sss.v1 import tenant

BASIC_EXAMPLE = {
    "tenant_id": "91b5c7c09cbd45cab3c146fd67ae471e",
    "tenant_name": "new_project",
    "description": "cheeseshop web",
    "region": "jp1",
    "contract_id": "econ123467890"
}

class TestRole(testtools.TestCase):

    def test_role(self):
        sot = tenant.Tenant()
        self.assertEqual("tenants", sot.resources_key)
        self.assertEqual(None, sot.resource_key)
        self.assertEqual("/tenants", sot.base_path)
        self.assertEqual('sss', sot.service.service_type)

        self.assertTrue(sot.allow_create)
        self.assertFalse(sot.allow_get)
        self.assertFalse(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertFalse(sot.allow_list)
        self.assertFalse(sot.put_create)

    def test_make_role(self):
        sot = tenant.Tenant(**BASIC_EXAMPLE)
        self.assertEqual(BASIC_EXAMPLE['tenant_id'], sot.tenant_id)
        self.assertEqual(BASIC_EXAMPLE['tenant_name'], sot.tenant_name)
        self.assertEqual(BASIC_EXAMPLE['description'], sot.description)
        self.assertEqual(BASIC_EXAMPLE['region'], sot.region)
        self.assertEqual(BASIC_EXAMPLE['contract_id'], sot.contract_id)
