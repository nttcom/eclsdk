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


class TestStorageType(base.BaseFunctionalTest):

    def test_storage_types(self):
        storage_type_list = list(self.conn.managed_rdb.storage_types())
        print(storage_type_list)
        self.assertGreater(len(storage_type_list), 0)

        for storage_type in storage_type_list:
            print(storage_type)
            self.assertIsInstance(storage_type.name, six.string_types)
            self.assertIsInstance(storage_type.type, six.string_types)
            self.assertIsInstance(storage_type.iops, int)
            self.assertIsInstance(storage_type.size, int)
