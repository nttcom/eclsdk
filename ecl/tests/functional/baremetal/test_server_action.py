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


class TestServerAction(base.BaseFunctionalTest):

    def test_01_start_server(self):
        server = self.conn.baremetal.start_server(
            "752aac2e-4b82-4d47-a7c7-fcbd0cbc86e2",
            "DISK"
        )

    def test_02_stop_server(self):
        server = self.conn.baremetal.stop_server(
            "752aac2e-4b82-4d47-a7c7-fcbd0cbc86e2",
            None
        )
        assert False

    def test_03_reboot_server(self):
        server = self.conn.baremetal.reboot_server(
            "752aac2e-4b82-4d47-a7c7-fcbd0cbc86e2",
            "SOFT",
            "disk"
        )

    def test_04_get_management_console(self):
        server = self.conn.baremetal.get_management_console(
            "752aac2e-4b82-4d47-a7c7-fcbd0cbc86e2",
            None
        )
        self.assertIsInstance(server.type, six.string_types)
        self.assertIsInstance(server.url, six.string_types)
        self.assertIsInstance(server.user_id, six.string_types)
        self.assertIsInstance(server.password, six.string_types)
