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


import six
from ecl.tests.functional import base


class TestUEFI(base.BaseFunctionalTest):

    # def test_01_show_UEFI(self):
    #     server_id = "752aac2e-4b82-4d47-a7c7-fcbd0cbc86e2"
    #     uefi = self.conn.baremetal.get_uefi(server_id)
    #     print uefi
    #     self.assertIsInstance(uefi.flavor_name, six.string_types)
    #     self.assertIsInstance(uefi.flavor_id, six.string_types)
    #     self.assertIsInstance(uefi.status, six.string_types)
    #     self.assertIsInstance(uefi.message, six.string_types)
    #     self.assertIsInstance(uefi.setting, dict)

    def test_02_update_UEFI(self):
        server_id = "752aac2e-4b82-4d47-a7c7-fcbd0cbc86e2"

        new_uefi = {
            "setting": {
                "CollabPowerControl": {"value": "Enabled"}
            }
        }
        uefi = self.conn.baremetal.update_uefi(server_id, uefi=new_uefi)
        self.assertIsInstance(uefi.flavor_name, six.string_types)
        self.assertIsInstance(uefi.flavor_id, six.string_types)
        self.assertIsInstance(uefi.status, six.string_types)
        self.assertIsInstance(uefi.message, six.string_types)
        self.assertIsInstance(uefi.setting, dict)
