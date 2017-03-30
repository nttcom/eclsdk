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

from ecl.baremetal.v2 import uefi

EXAMPLE = {
    "flavor_name": "General Purpose 2",
    "flavor_id": "fcec5541-81c3-4963-ba6f-dc24773ebf7f",
    "updated": "2012-09-07T16:56:37Z",
    "status": "SUCCESS",
    "message": "",
    "setting": {
        "hoge": {
            "value": "Enabled",
            "default": "Enabled",
            "type": "enum",
            "selection": ["Enabled", "Disabled"]
        },
        "fuga": {
            "value": "Disabled",
            "default": "Enabled",
            "type": "enum",
            "selection": ["Enabled", "Disabled"]
        }
    }
}


class TestUEFI(testtools.TestCase):

    def test_basic(self):
        sot = uefi.UEFI()
        self.assertEqual('uefi', sot.resource_key)
        self.assertEqual('uefi', sot.resources_key)
        self.assertEqual('/servers/%(server_id)s/uefi', sot.base_path)
        self.assertEqual('baremetal-server', sot.service.service_type)
        self.assertFalse(sot.allow_create)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_update)
        self.assertFalse(sot.allow_delete)
        self.assertFalse(sot.allow_list)

    def test_make_it(self):
        sot = uefi.UEFI(**EXAMPLE)
        self.assertEqual(EXAMPLE['flavor_name'], sot.flavor_name)
        self.assertEqual(EXAMPLE['flavor_id'], sot.flavor_id)
        self.assertEqual(EXAMPLE['updated'], sot.updated)
        self.assertEqual(EXAMPLE['status'], sot.status)
        self.assertEqual(EXAMPLE['message'], sot.message)
        self.assertEqual(EXAMPLE['setting'], sot.setting)
