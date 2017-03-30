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

from ecl.sss.v1 import contract

BASIC_EXAMPLE = {
    "contract_id": "econXXXXXXXXXX",
    "status": "enable",
    "customer_number": "N1234567890",
    "channel_name": "test_channel",
    "channel_id": "chXXXXX",
    "management_channel": False,
    "contract_owner_user_id": "ecidXXXXXX",
    "start_time": "2016-03-04 12:24:50",
    "end_time": "",
    "login_integration": "",
    "sss_endpoint": "https://xxxxxxxxxx/api",
    "keystone_endpoint": "https://keystone-xxxxxxxxxx:443",
    "company_code": "C1234567890",
    "glass_customer_id": "",
    "glass_user_id": "",
    "owner_contract_id": "econxxxxxxxxxx",
    "charge_status": "xxxxxxxxx",
    "cycle_start_time": "yyyy-mm-dd hh:mm:ss",
    "cycle_end_time": "yyyy-mm-dd hh:mm:ss",
    "charge_data": {},
    "notify_password": False,
}

class TestRole(testtools.TestCase):

    def test_role(self):
        sot = contract.Contract()
        self.assertEqual(None, sot.resources_key)
        self.assertEqual(None, sot.resource_key)
        self.assertEqual("/contracts", sot.base_path)
        self.assertEqual('sss', sot.service.service_type)

        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_get)
        self.assertFalse(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertFalse(sot.put_create)

    def test_make_role(self):
        sot = contract.Contract(**BASIC_EXAMPLE)
        self.assertEqual(BASIC_EXAMPLE['contract_id'], sot.contract_id)
        self.assertEqual(BASIC_EXAMPLE['status'], sot.status)
        self.assertEqual(BASIC_EXAMPLE['customer_number'], sot.customer_number)
        self.assertEqual(BASIC_EXAMPLE['channel_name'], sot.channel_name)
        self.assertEqual(BASIC_EXAMPLE['channel_id'], sot.channel_id)
        self.assertEqual(BASIC_EXAMPLE['notify_password'], sot.notify_password)
        self.assertEqual(BASIC_EXAMPLE['management_channel'], sot.management_channel)
        self.assertEqual(BASIC_EXAMPLE['contract_owner_user_id'], sot.contract_owner_user_id)
        self.assertEqual(BASIC_EXAMPLE['contract_owner_user_id'], sot.contract_owner_user_id)
        self.assertEqual(BASIC_EXAMPLE['start_time'], sot.start_time)
        self.assertEqual(BASIC_EXAMPLE['end_time'], sot.end_time)
        self.assertEqual(BASIC_EXAMPLE['login_integration'], sot.login_integration)
        self.assertEqual(BASIC_EXAMPLE['sss_endpoint'], sot.sss_endpoint)
        self.assertEqual(BASIC_EXAMPLE['keystone_endpoint'], sot.keystone_endpoint)
        self.assertEqual(BASIC_EXAMPLE['company_code'], sot.company_code)
        self.assertEqual(BASIC_EXAMPLE['glass_customer_id'], sot.glass_customer_id)
        self.assertEqual(BASIC_EXAMPLE['glass_user_id'], sot.glass_user_id)
        self.assertEqual(BASIC_EXAMPLE['owner_contract_id'], sot.owner_contract_id)
        self.assertEqual(BASIC_EXAMPLE['charge_status'], sot.charge_status)
        self.assertEqual(BASIC_EXAMPLE['cycle_start_time'], sot.cycle_start_time)
        self.assertEqual(BASIC_EXAMPLE['cycle_end_time'], sot.cycle_end_time)
        self.assertEqual(BASIC_EXAMPLE['charge_data'], sot.charge_data)
        self.assertEqual(BASIC_EXAMPLE['notify_password'], sot.notify_password)
