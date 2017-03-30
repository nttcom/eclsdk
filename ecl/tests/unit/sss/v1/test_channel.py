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
from ecl.sss.v1 import channel

BASIC_EXAMPLE = {
    "channel_id": "Chiquia",
    "channel_name": "cheroot",
    "language": "ha",
    "management_channel": True,
    "parent_channel_id": None,
    "contracts": [
        {
            "contract_id": "excusableness",
            "status": "enable"
        }
    ]
}

class TestRole(testtools.TestCase):

    def test_role(self):
        sot = channel.Channel()
        self.assertEqual("channels", sot.resources_key)
        self.assertEqual(None, sot.resource_key)
        self.assertEqual("/channels?get_contracts=%(get_contracts)s", sot.base_path)
        self.assertEqual('sss', sot.service.service_type)

        self.assertFalse(sot.allow_create)
        self.assertFalse(sot.allow_get)
        self.assertFalse(sot.allow_update)
        self.assertFalse(sot.allow_delete)
        self.assertTrue(sot.allow_list)

    def test_make_role(self):
        sot = channel.Channel(**BASIC_EXAMPLE)
        self.assertEqual(BASIC_EXAMPLE['channel_id'], sot.channel_id)
        self.assertEqual(BASIC_EXAMPLE['channel_name'], sot.channel_name)
        self.assertEqual(BASIC_EXAMPLE['language'], sot.language)
        self.assertEqual(BASIC_EXAMPLE['management_channel'], sot.management_channel)
        self.assertEqual(BASIC_EXAMPLE['parent_channel_id'], sot.parent_channel_id)
        self.assertEqual(BASIC_EXAMPLE['contracts'], sot.contracts)
