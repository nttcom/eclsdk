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

from ecl.storage.v1 import volume as v

IDENTIFIER = 'IDENTIFIER'
BASIC_EXAMPLE = {
    'id': IDENTIFIER,
    'name': 'vol01',
    'description': 'Volume for vs01',
    'status': 'creating',
    'size': 100,
    'iops_per_gb': 4,
    'initiator_iqns': [],
    'initiator_secret': 'null',
    'target_secret': 'null',
    'snapshot_ids': [],
    'target_ips': [],
    'metadata': {},
    'virtual_storage_id': '2',
    'availability_zone': '3',
    'created_at': 'null',
    'updated_at': 'null',
    'error_message': '',
    'throughput': 50,
    'export_rules': []
}


class TestVolume(testtools.TestCase):

    def test_basic(self):
        sot = v.Volume()
        self.assertEqual('volume', sot.resource_key)
        self.assertEqual('volumes', sot.resources_key)
        self.assertEqual('/volumes', sot.base_path)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertEqual('storage', sot.service.service_type)

    def test_basic_detail(self):
        sot = v.VolumeDetail()
        self.assertEqual('volume', sot.resource_key)
        self.assertEqual('volumes', sot.resources_key)
        self.assertEqual('/volumes/detail', sot.base_path)
        self.assertTrue(sot.allow_list)
        self.assertFalse(sot.allow_get)
        self.assertFalse(sot.allow_create)
        self.assertFalse(sot.allow_update)
        self.assertFalse(sot.allow_delete)
        self.assertEqual('storage', sot.service.service_type)

    def test_make_basic(self):
        sot = v.Volume(**BASIC_EXAMPLE)
        self.assertEqual(BASIC_EXAMPLE['id'], sot.id)
        self.assertEqual(BASIC_EXAMPLE['name'], sot.name)
        self.assertEqual(BASIC_EXAMPLE['description'], sot.description)
        self.assertEqual(BASIC_EXAMPLE['status'], sot.status)
        self.assertEqual(BASIC_EXAMPLE['size'], sot.size)
        self.assertEqual(BASIC_EXAMPLE['iops_per_gb'], sot.iops_per_gb)
        self.assertEqual(BASIC_EXAMPLE['initiator_iqns'], sot.initiator_iqns)
        self.assertEqual(BASIC_EXAMPLE['initiator_secret'], sot.initiator_secret)
        self.assertEqual(BASIC_EXAMPLE['target_secret'], sot.target_secret)
        self.assertEqual(BASIC_EXAMPLE['snapshot_ids'], sot.snapshot_ids)
        self.assertEqual(BASIC_EXAMPLE['target_ips'], sot.target_ips)
        self.assertEqual(BASIC_EXAMPLE['metadata'], sot.metadata)
        self.assertEqual(BASIC_EXAMPLE['virtual_storage_id'], sot.virtual_storage_id)
        self.assertEqual(BASIC_EXAMPLE['availability_zone'], sot.availability_zone)
        self.assertEqual(BASIC_EXAMPLE['created_at'], sot.created_at)
        self.assertEqual(BASIC_EXAMPLE['updated_at'], sot.updated_at)
        self.assertEqual(BASIC_EXAMPLE['error_message'], sot.error_message)
        self.assertEqual(BASIC_EXAMPLE['throughput'], sot.throughput)
        self.assertEqual(BASIC_EXAMPLE['export_rules'], sot.export_rules)
