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

from ecl.tests.functional import base


class TestMetadata(base.BaseFunctionalTest):
    server_id = "752aac2e-4b82-4d47-a7c7-fcbd0cbc86e2"

    def setUp(self):
        print("\n>> Test Name: " + self.id())

    def test_01_list(self):
        metadata = self.conn.baremetal.metadata(self.server_id)
        print(metadata)
        self.assertIsInstance(metadata.metadata, dict)

    def test_02_replace(self):
        metadata = self.conn.baremetal.replace_metadata(
            self.server_id,
            metadata={"KEY1": "VALUE1",
                      "key2": "value2"}
        )
        print(metadata)
        self.assertIsInstance(metadata.metadata, dict)

    def test_03_delete(self):
        metadata = self.conn.baremetal.delete_metadata(
            self.server_id, "KEY1"
        )

    def test_04_merge(self):
        metadata = self.conn.baremetal.merge_metadata(
            self.server_id,
            metadata={"KEY60": "VALUE60"}
        )
        print(metadata)
        self.assertIsInstance(metadata.metadata, dict)

    def test_05_show(self):
        metadata = self.conn.baremetal.show_metadata(
            self.server_id, "KEY60"
        )
        print(metadata)
        self.assertIsInstance(metadata.metadata, dict)

    def test_06_update(self):
        metadata = self.conn.baremetal.update_metadata(
            self.server_id, "KEY60",
            metadata={"KEY60": "NEW_VALUE00"}
        )
        print(metadata)
        self.assertIsInstance(metadata.metadata, dict)

    def test_07_delete(self):
        metadata = self.conn.baremetal.delete_metadata(
            self.server_id, "key2"
        )

    def test_08_list(self):
        metadata = self.conn.baremetal.metadata(self.server_id)
        print(metadata)
        self.assertIsInstance(metadata.metadata, dict)
