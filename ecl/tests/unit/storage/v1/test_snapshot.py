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

from ecl.storage.v1 import snapshot as s

IDENTIFIER = 'IDENTIFIER'
BASIC_EXAMPLE = {
    'id': IDENTIFIER,
    "status": "available",
    "name": "snapshotForVol120160601",
    "description": None,
    "usage": 12,
    "volume_id": "90ff9a35-726d-47d6-a048-f080d2c90b57",
    "snapshot_type_id": "c113437f-755d-11e6-9494-080027aeede7",
    "created_at": "2015-05-17T18:14:34.000000",
    "updated_at": None,
    "error_message": ""
}


class TestSnapshot(testtools.TestCase):

    def test_basic(self):
        sot = s.Snapshot()
        self.assertEqual('snapshot', sot.resource_key)
        self.assertEqual('snapshots', sot.resources_key)
        self.assertEqual('/snapshots', sot.base_path)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertEqual('storage', sot.service.service_type)

    def test_basic_detail(self):
        sot = s.SnapshotDetail()
        self.assertEqual('snapshot', sot.resource_key)
        self.assertEqual('snapshots', sot.resources_key)
        self.assertEqual('/snapshots/detail', sot.base_path)
        self.assertTrue(sot.allow_list)
        self.assertFalse(sot.allow_get)
        self.assertFalse(sot.allow_create)
        self.assertFalse(sot.allow_update)
        self.assertFalse(sot.allow_delete)
        self.assertEqual('storage', sot.service.service_type)

    def test_make_basic(self):
        sot = s.Snapshot(**BASIC_EXAMPLE)
        self.assertEqual(BASIC_EXAMPLE['id'], sot.id)
        self.assertEqual(BASIC_EXAMPLE['status'], sot.status)
        self.assertEqual(BASIC_EXAMPLE['name'], sot.name)
        self.assertEqual(BASIC_EXAMPLE['description'], sot.description)
        self.assertEqual(BASIC_EXAMPLE['usage'], sot.usage)
        self.assertEqual(BASIC_EXAMPLE['volume_id'], sot.volume_id)
        self.assertEqual(BASIC_EXAMPLE['snapshot_type_id'], sot.snapshot_type_id)
        self.assertEqual(BASIC_EXAMPLE['description'], sot.description)
        self.assertEqual(BASIC_EXAMPLE['created_at'], sot.created_at)
        self.assertEqual(BASIC_EXAMPLE['updated_at'], sot.updated_at)
        self.assertEqual(BASIC_EXAMPLE['error_message'], sot.error_message)
