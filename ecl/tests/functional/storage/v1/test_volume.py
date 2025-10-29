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

        # required
        self.assertIsInstance(volume.id, six.string_types)
        self.assertIsInstance(volume.name, six.string_types)
        self.assertIsInstance(volume.description, six.string_types)
        self.assertIsInstance(volume.virtual_storage_id, six.string_types)
        self.assertIsInstance(volume.status, six.string_types)
        self.assertIsInstance(volume.size, int)
        self.assertIsInstance(volume.created_at, six.string_types)
        self.assertIsInstance(volume.updated_at, six.string_types)
        self.assertIsInstance(volume.error_message, six.string_types)
        self.assertIsInstance(volume.target_ips, list)
        self.assertIsInstance(volume.availability_zone, six.string_types)
        self.assertIsInstance(volume.snapshot_ids, six.string_types)
        self.assertIsInstance(volume.encrypt, bool)

        # Only available for "piops_iscsi_na" or "piops_iscsi_na2" volumes
        self.assertIsInstance(volume.percentage_snapshot_reserve_used, int)

        # Only available for "piops_iscsi_na" volumes
        # self.assertIsInstance(volume.iops_per_gb, int)
        # self.assertIsInstance(volume.initiator_iqns, list)
        # self.assertIsInstance(volume.initiator_secret, null)
        # self.assertIsInstance(volume.target_secret, null)
        # self.assertIsInstance(volume.metadata, dict)

        # Only available for "piops_iscsi_na2" volumes
        self.assertIsInstance(volume.snapshot_reserve_size, int)
        self.assertIsInstance(volume.snapshot_reserve_used, int)

        # Only available for "standard_nfs_na" or "standard_smb_na" volumes
        # self.assertIsInstance(volume.export_rules, list)

        # Only available for "standard_smb_na" volumes
        # self.assertIsInstance(volume.smb_properties, dict)

    def test_02_show_volume(self):
        volume = self.conn.storage.get_volume("4096336b-7035-412a-8148-ad999f0e0bc8")

        # required
        self.assertIsInstance(volume.id, six.string_types)
        self.assertIsInstance(volume.name, six.string_types)
        self.assertIsInstance(volume.description, six.string_types)
        self.assertIsInstance(volume.virtual_storage_id, six.string_types)
        self.assertIsInstance(volume.status, six.string_types)
        self.assertIsInstance(volume.size, int)
        self.assertIsInstance(volume.created_at, six.string_types)
        self.assertIsInstance(volume.updated_at, six.string_types)
        self.assertIsInstance(volume.error_message, six.string_types)
        self.assertIsInstance(volume.target_ips, list)
        self.assertIsInstance(volume.availability_zone, six.string_types)
        self.assertIsInstance(volume.snapshot_ids, six.string_types)
        self.assertIsInstance(volume.encrypt, bool)

        # Only available for "piops_iscsi_na" or "piops_iscsi_na2" volumes
        self.assertIsInstance(volume.percentage_snapshot_reserve_used, int)

        # Only available for "piops_iscsi_na" volumes
        # self.assertIsInstance(volume.iops_per_gb, int)
        # self.assertIsInstance(volume.initiator_iqns, list)
        # self.assertIsInstance(volume.initiator_secret, null)
        # self.assertIsInstance(volume.target_secret, null)
        # self.assertIsInstance(volume.metadata, dict)

        # Only available for "piops_iscsi_na2" volumes
        self.assertIsInstance(volume.snapshot_reserve_size, int)
        self.assertIsInstance(volume.snapshot_reserve_used, int)

        # Only available for "standard_nfs_na" or "standard_smb_na" volumes
        # self.assertIsInstance(volume.export_rules, list)

        # Only available for "standard_smb_na" volumes
        # self.assertIsInstance(volume.smb_properties, dict)

    def test_03_update_volume(self):
        volume = self.conn.storage.update_volume(
            "4096336b-7035-412a-8148-ad999f0e0bc8",
            description="updated_test"
        )
        print(volume.description)

        # required
        self.assertIsInstance(volume.id, six.string_types)
        self.assertIsInstance(volume.name, six.string_types)
        self.assertIsInstance(volume.description, six.string_types)
        self.assertIsInstance(volume.virtual_storage_id, six.string_types)
        self.assertIsInstance(volume.status, six.string_types)
        self.assertIsInstance(volume.size, int)
        self.assertIsInstance(volume.created_at, six.string_types)
        self.assertIsInstance(volume.updated_at, six.string_types)
        self.assertIsInstance(volume.error_message, six.string_types)
        self.assertIsInstance(volume.target_ips, list)
        self.assertIsInstance(volume.availability_zone, six.string_types)
        self.assertIsInstance(volume.snapshot_ids, six.string_types)
        self.assertIsInstance(volume.encrypt, bool)

        # Only available for "piops_iscsi_na" or "piops_iscsi_na2" volumes
        self.assertIsInstance(volume.percentage_snapshot_reserve_used, int)

        # Only available for "piops_iscsi_na" volumes
        # self.assertIsInstance(volume.iops_per_gb, int)
        # self.assertIsInstance(volume.initiator_iqns, list)
        # self.assertIsInstance(volume.initiator_secret, null)
        # self.assertIsInstance(volume.target_secret, null)
        # self.assertIsInstance(volume.metadata, dict)

        # Only available for "piops_iscsi_na2" volumes
        self.assertIsInstance(volume.snapshot_reserve_size, int)
        self.assertIsInstance(volume.snapshot_reserve_used, int)

        # Only available for "standard_nfs_na" or "standard_smb_na" volumes
        # self.assertIsInstance(volume.export_rules, list)

        # Only available for "standard_smb_na" volumes
        # self.assertIsInstance(volume.smb_properties, dict)

    @classmethod
    def test_04_create_volume(cls):
        volume = cls.conn.storage.create_volume(
            name="sdk_test",
            size=100,
            virtual_storage_id="19ff4cba-3b86-4da1-9663-25ea74f9b0a9",
        )

        # required
        assert isInstance(volume.id, six.string_types)
        assert isInstance(volume.name, six.string_types)
        assert isInstance(volume.description, six.string_types)
        assert isInstance(volume.virtual_storage_id, six.string_types)
        assert isInstance(volume.status, six.string_types)
        assert isInstance(volume.size, int)
        assert isInstance(volume.created_at, six.string_types)
        assert isInstance(volume.updated_at, six.string_types)
        assert isInstance(volume.error_message, six.string_types)
        assert isInstance(volume.target_ips, list)
        assert isInstance(volume.availability_zone, six.string_types)
        assert isInstance(volume.snapshot_ids, six.string_types)
        assert isInstance(volume.encrypt, bool)

        # Only available for "piops_iscsi_na" or "piops_iscsi_na2" volumes
        assert isInstance(volume.percentage_snapshot_reserve_used, int)

        # Only available for "piops_iscsi_na" volumes
        # assert isInstance(volume.iops_per_gb, int)
        # assert isInstance(volume.initiator_iqns, list)
        # assert isInstance(volume.initiator_secret, null)
        # assert isInstance(volume.target_secret, null)
        # assert isInstance(volume.metadata, dict)

        # Only available for "piops_iscsi_na2" volumes
        assert isInstance(volume.snapshot_reserve_size, int)
        assert isInstance(volume.snapshot_reserve_used, int)

        # Only available for "standard_nfs_na" or "standard_smb_na" volumes
        # assert isInstance(volume.export_rules, list)

        # Only available for "standard_smb_na" volumes
        # assert isInstance(volume.smb_properties, dict)

        cls.vol_id = volume.id

    def test_05_delete_volume(self):
        time.sleep(20)
        volume = self.conn.storage.delete_volume(self.vol_id)
