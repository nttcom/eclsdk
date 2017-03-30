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

from ecl.sss.v1 import user

BASIC_EXAMPLE = {
    "user_id": "ecid1000005297",
    "login_id": "userlogin_id",
    "mail_address": "youremail@ntt.com",
    "contract_owner": True,
    "sss_endpoint": "https://sss-jp1-ecl.api.ntt.com:443/api",
    "keystone_endpoint": "https://keystone-jp1-ecl.api.ntt.com:443",
    "keystone_name": "XXXXXXXXXXX",
    "keystone_password": "XXXXXXXXXX",
    "start_time": "2016-01-06 00:44:39",
    "contract_id": "econ1000003351",
    "login_integration": "icp",
    "external_reference_id": "econ1000003351",
    "password": "password",
    "notify_password": True,
    "new_password": "new_password",
}

class TestUser(testtools.TestCase):

    def test_user(self):
        sot = user.User()
        self.assertEqual("users", sot.resources_key)
        self.assertEqual(None, sot.resource_key)
        self.assertEqual("/users", sot.base_path)
        self.assertEqual('sss', sot.service.service_type)

        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertFalse(sot.put_create)

    def test_make_user(self):
        sot = user.User(**BASIC_EXAMPLE)
        self.assertEqual(BASIC_EXAMPLE['login_id'], sot.login_id)
        self.assertEqual(BASIC_EXAMPLE['mail_address'], sot.mail_address)
        self.assertEqual(BASIC_EXAMPLE['user_id'], sot.user_id)
        self.assertEqual(BASIC_EXAMPLE['contract_owner'], sot.contract_owner)
        self.assertEqual(BASIC_EXAMPLE['contract_id'], sot.contract_id)
        self.assertEqual(BASIC_EXAMPLE['keystone_name'], sot.keystone_name)
        self.assertEqual(BASIC_EXAMPLE['keystone_endpoint'], sot.keystone_endpoint)
        self.assertEqual(BASIC_EXAMPLE['keystone_password'], sot.keystone_password)
        self.assertEqual(BASIC_EXAMPLE['sss_endpoint'], sot.sss_endpoint)
        self.assertEqual(BASIC_EXAMPLE['password'], sot.password)
        self.assertEqual(BASIC_EXAMPLE['notify_password'], sot.notify_password)
        self.assertEqual(BASIC_EXAMPLE['new_password'], sot.new_password)
        self.assertEqual(BASIC_EXAMPLE['external_reference_id'], sot.external_reference_id)
        self.assertEqual(BASIC_EXAMPLE['login_integration'], sot.login_integration)
