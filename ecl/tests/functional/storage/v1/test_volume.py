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
import time
from ecl.tests.functional import base


class TestVolume(base.BaseFunctionalTest):
    def test_01_volumes(self):
        volumes = list(self.conn.storage.volumes(details=True))
        volume = volumes[1]
        self.assertIsInstance(volume.id, six.string_types)
        self.assertIsInstance(volume.status, six.string_types)
        self.assertIsInstance(volume.name, six.string_types)
        self.assertIsInstance(volume.size, int)
        self.assertIsInstance(volume.description, six.string_types)
        self.assertIsInstance(volume.iops_per_gb, six.string_types)
        self.assertIsInstance(volume.initiator_iqns, list)
        self.assertIsInstance(volume.target_ips, list)
        self.assertIsInstance(volume.metadata, dict)
        self.assertIsInstance(volume.virtual_storage_id, six.string_types)
        self.assertIsInstance(volume.availability_zone, six.string_types)
        self.assertIsInstance(volume.created_at, six.string_types)
        self.assertIsInstance(volume.updated_at, six.string_types)
        self.assertIsInstance(volume.id, six.string_types)

    def test_02_show_volume(self):
        volume = self.conn.storage.get_volume("4096336b-7035-412a-8148-ad999f0e0bc8")
        self.assertIsInstance(volume.id, six.string_types)
        self.assertIsInstance(volume.status, six.string_types)
        self.assertIsInstance(volume.name, six.string_types)
        self.assertIsInstance(volume.size, int)
        self.assertIsInstance(volume.description, six.string_types)
        self.assertIsInstance(volume.iops_per_gb, six.string_types)
        self.assertIsInstance(volume.initiator_iqns, list)
        self.assertIsInstance(volume.target_ips, list)
        self.assertIsInstance(volume.metadata, dict)
        self.assertIsInstance(volume.virtual_storage_id, six.string_types)
        self.assertIsInstance(volume.availability_zone, six.string_types)
        self.assertIsInstance(volume.created_at, six.string_types)
        self.assertIsInstance(volume.updated_at, six.string_types)
        self.assertIsInstance(volume.id, six.string_types)

    def test_03_update_volume(self):
        volume = self.conn.storage.update_volume(
            "4096336b-7035-412a-8148-ad999f0e0bc8",
            description="updated_test"
        )
        print(volume.description)
        self.assertIsInstance(volume.id, six.string_types)
        self.assertIsInstance(volume.status, six.string_types)
        self.assertIsInstance(volume.name, six.string_types)
        self.assertIsInstance(volume.size, int)
        self.assertIsInstance(volume.description, six.string_types)
        self.assertIsInstance(volume.iops_per_gb, six.string_types)
        self.assertIsInstance(volume.initiator_iqns, list)
        self.assertIsInstance(volume.target_ips, list)
        self.assertIsInstance(volume.metadata, dict)
        self.assertIsInstance(volume.virtual_storage_id, six.string_types)
        self.assertIsInstance(volume.availability_zone, six.string_types)
        self.assertIsInstance(volume.created_at, six.string_types)
        self.assertIsInstance(volume.updated_at, six.string_types)
        self.assertIsInstance(volume.id, six.string_types)

    @classmethod
    def test_04_create_volume(cls):
        volume = cls.conn.storage.create_volume(
            name="sdk_test",
            size=100,
            virtual_storage_id="19ff4cba-3b86-4da1-9663-25ea74f9b0a9",
        )
        assert isinstance(volume.id, six.string_types)
        assert isinstance(volume.status, six.string_types)
        assert isinstance(volume.name, six.string_types)
        assert isinstance(volume.size, int)
        assert isinstance(volume.description, six.string_types)
        assert isinstance(volume.iops_per_gb, six.string_types)
        assert isinstance(volume.initiator_iqns, list)
        assert isinstance(volume.target_ips, list)
        assert isinstance(volume.metadata, dict)
        assert isinstance(volume.virtual_storage_id, six.string_types)
        assert isinstance(volume.availability_zone, six.string_types)
        assert isinstance(volume.created_at, six.string_types)
        cls.vol_id = volume.id

    def test_05_delete_volume(self):
        time.sleep(20)
        volume = self.conn.storage.delete_volume(self.vol_id)
