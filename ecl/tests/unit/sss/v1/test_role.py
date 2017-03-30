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

from ecl.sss.v1 import role

BASIC_EXAMPLE = {
  "user_id":"ecid1000024459",
  "region_id":"jp1",
  "region_name":"jp1",
  "tenant_id":"3c90482157664923ada457950a96aca8",
  "tenant_name":"Cheese",
  "role_name":"_member_"
}

class TestRole(testtools.TestCase):

    def test_role(self):
        sot = role.Role()
        self.assertEqual(None, sot.resources_key)
        self.assertEqual(None, sot.resource_key)
        self.assertEqual("/roles", sot.base_path)
        self.assertEqual('sss', sot.service.service_type)

        self.assertTrue(sot.allow_create)
        self.assertFalse(sot.allow_get)
        self.assertFalse(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertFalse(sot.allow_list)
        self.assertFalse(sot.put_create)

    def test_make_role(self):
        sot = role.Role(**BASIC_EXAMPLE)
        self.assertEqual(BASIC_EXAMPLE['user_id'], sot.user_id)
        self.assertEqual(BASIC_EXAMPLE['region_id'], sot.region_id)
        self.assertEqual(BASIC_EXAMPLE['region_name'], sot.region_name)
        self.assertEqual(BASIC_EXAMPLE['tenant_id'], sot.tenant_id)
        self.assertEqual(BASIC_EXAMPLE['tenant_name'], sot.tenant_name)
        self.assertEqual(BASIC_EXAMPLE['role_name'], sot.role_name)
