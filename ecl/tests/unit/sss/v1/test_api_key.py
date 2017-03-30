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
from ecl.sss.v1 import api_key

BASIC_EXAMPLE = {
    "user_id" : "ecid0000011111",
    "keystone_name" : "XTI3u6blgFu36je0jDjkBKlFG4GmI4kn",
    "keystone_password" : "Dbu1nZUprR8wg57k",
    "status" : "Success"
}

class TestRole(testtools.TestCase):

    def test_role(self):
        sot = api_key.Api_key()
        self.assertEqual(None, sot.resources_key)
        self.assertEqual(None, sot.resource_key)
        self.assertEqual("/keys", sot.base_path)
        self.assertEqual('sss', sot.service.service_type)

        self.assertFalse(sot.allow_create)
        self.assertFalse(sot.allow_get)
        self.assertTrue(sot.allow_update)
        self.assertFalse(sot.allow_delete)
        self.assertFalse(sot.allow_list)

    def test_make_role(self):
        sot = api_key.Api_key(**BASIC_EXAMPLE)
        self.assertEqual(BASIC_EXAMPLE['user_id'], sot.user_id)
        self.assertEqual(BASIC_EXAMPLE['keystone_name'], sot.keystone_name)
        self.assertEqual(BASIC_EXAMPLE['keystone_password'], sot.keystone_password)
        self.assertEqual(BASIC_EXAMPLE['status'], sot.status)
