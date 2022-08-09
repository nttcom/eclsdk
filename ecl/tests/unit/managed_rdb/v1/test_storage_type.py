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

from ecl.managed_rdb.v1 import storage_type

STORAGE_TYPE_EXAMPLE = {
    'name': '4IOPS-500GB',
    'type': 'piops_iscsi_na',
    'iops': 4,
    'size': 50,
}


class TestStorageType(testtools.TestCase):

    def test_basic(self):
        sot = storage_type.StorageType()
        self.assertEqual('storage_types', sot.resources_key)
        self.assertEqual('/v1.0/storage_types', sot.base_path)
        self.assertEqual('managed-rdb', sot.service.service_type)
        self.assertTrue(sot.allow_list)

    def test_make_basic(self):
        sot = storage_type.StorageType(**STORAGE_TYPE_EXAMPLE)
        self.assertEqual(STORAGE_TYPE_EXAMPLE['name'], sot.name)
        self.assertEqual(STORAGE_TYPE_EXAMPLE['type'], sot.type)
        self.assertEqual(STORAGE_TYPE_EXAMPLE['iops'], sot.iops)
        self.assertEqual(STORAGE_TYPE_EXAMPLE['size'], sot.size)
