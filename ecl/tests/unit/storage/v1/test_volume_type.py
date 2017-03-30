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

from ecl.storage.v1 import volume_type as vt

IDENTIFIER = '6685584b-1eac-4da6-b5c3-555430cf68ff'
BASIC_EXAMPLE = {
    'id': IDENTIFIER,
    'name': 'piops_iscsi_na',
    'extra_specs': {
        'available_volume_size': [
            100, 250, 500, 1000, 2000, 4000, 8000, 12000
        ],
        'available_iops_per_gb': [
            '2', '4'
        ]
    }
}


class TestVolumeType(testtools.TestCase):

    def test_basic(self):
        sot = vt.VolumeType()
        self.assertEqual('volume_type', sot.resource_key)
        self.assertEqual('volume_types', sot.resources_key)
        self.assertEqual('/volume_types', sot.base_path)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_get)
        self.assertEqual('storage', sot.service.service_type)

    def test_basic_detail(self):
        sot = vt.VolumeTypeDetail()
        self.assertEqual('volume_type', sot.resource_key)
        self.assertEqual('volume_types', sot.resources_key)
        self.assertEqual('/volume_types/detail', sot.base_path)
        self.assertTrue(sot.allow_list)
        self.assertFalse(sot.allow_get)
        self.assertEqual('storage', sot.service.service_type)

    def test_make_basic(self):
        sot = vt.VolumeType(**BASIC_EXAMPLE)
        self.assertEqual(BASIC_EXAMPLE['id'], sot.id)
        self.assertEqual(BASIC_EXAMPLE['name'], sot.name)
        self.assertEqual(BASIC_EXAMPLE['extra_specs'], sot.extra_specs)
