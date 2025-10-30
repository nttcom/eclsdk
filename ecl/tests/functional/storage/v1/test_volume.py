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
        if volume.description is not None:
            self.assertIsInstance(volume.description, six.string_types)
        else:
            self.assertIsNone(volume.description)
        self.assertIsInstance(volume.virtual_storage_id, six.string_types)
        self.assertIsInstance(volume.status, six.string_types)
        self.assertIsInstance(volume.size, six.integer_types)
        if volume.created_at is not None:
            self.assertIsInstance(volume.created_at, six.string_types)
        else:
            self.assertIsNone(volume.created_at)
        if volume.updated_at is not None:
            self.assertIsInstance(volume.updated_at, six.string_types)
        else:
            self.assertIsNone(volume.updated_at)
        self.assertIsInstance(volume.error_message, six.string_types)
        self.assertIsInstance(volume.target_ips, list)
        if volume.availability_zone is not None:
            self.assertIsInstance(volume.availability_zone, six.string_types)
        else:
            self.assertIsNone(volume.availability_zone)
        self.assertIsInstance(volume.snapshot_ids, list)
        # self.assertIsInstance(volume.encrypt, bool)

        # Only available for "piops_iscsi_na" or "piops_iscsi_na2" volumes
        self.assertIsInstance(volume.percentage_snapshot_reserve_used, six.integer_types)

        # Only available for "piops_iscsi_na" volumes
        # self.assertIsInstance(volume.iops_per_gb, six.integer_types)
        # self.assertIsInstance(volume.initiator_iqns, list)
        # self.assertIsNone(volume.initiator_secret)
        # self.assertIsNone(volume.target_secret)
        # self.assertIsInstance(volume.metadata, dict)

        # Only available for "piops_iscsi_na2" volumes
        self.assertIsInstance(volume.snapshot_reserve_size, six.integer_types)
        self.assertIsInstance(volume.snapshot_reserve_used, six.integer_types)

        # Only available for "standard_nfs_na" or "standard_smb_na" volumes
        # self.assertIsInstance(volume.export_rules, list)

        # Only available for "standard_smb_na" volumes
        # self.assertIsInstance(volume.smb_properties, dict)

    def test_02_show_volume(self):
        volume = self.conn.storage.get_volume("4096336b-7035-412a-8148-ad999f0e0bc8")

        # required
        self.assertIsInstance(volume.id, six.string_types)
        self.assertIsInstance(volume.name, six.string_types)
        if volume.description is not None:
            self.assertIsInstance(volume.description, six.string_types)
        else:
            self.assertIsNone(volume.description)
        self.assertIsInstance(volume.virtual_storage_id, six.string_types)
        self.assertIsInstance(volume.status, six.string_types)
        self.assertIsInstance(volume.size, six.integer_types)
        if volume.created_at is not None:
            self.assertIsInstance(volume.created_at, six.string_types)
        else:
            self.assertIsNone(volume.created_at)
        if volume.updated_at is not None:
            self.assertIsInstance(volume.updated_at, six.string_types)
        else:
            self.assertIsNone(volume.updated_at)
        self.assertIsInstance(volume.error_message, six.string_types)
        self.assertIsInstance(volume.target_ips, list)
        if volume.availability_zone is not None:
            self.assertIsInstance(volume.availability_zone, six.string_types)
        else:
            self.assertIsNone(volume.availability_zone)
        self.assertIsInstance(volume.snapshot_ids, list)
        # self.assertIsInstance(volume.encrypt, bool)

        # Only available for "piops_iscsi_na" or "piops_iscsi_na2" volumes
        self.assertIsInstance(volume.percentage_snapshot_reserve_used, six.integer_types)

        # Only available for "piops_iscsi_na" volumes
        # self.assertIsInstance(volume.iops_per_gb, six.integer_types)
        # self.assertIsInstance(volume.initiator_iqns, list)
        # self.assertIsNone(volume.initiator_secret)
        # self.assertIsNone(volume.target_secret)
        # self.assertIsInstance(volume.metadata, dict)

        # Only available for "piops_iscsi_na2" volumes
        self.assertIsInstance(volume.snapshot_reserve_size, six.integer_types)
        self.assertIsInstance(volume.snapshot_reserve_used, six.integer_types)

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
        if volume.description is not None:
            self.assertIsInstance(volume.description, six.string_types)
        else:
            self.assertIsNone(volume.description)
        self.assertIsInstance(volume.virtual_storage_id, six.string_types)
        self.assertIsInstance(volume.status, six.string_types)
        self.assertIsInstance(volume.size, six.integer_types)
        if volume.created_at is not None:
            self.assertIsInstance(volume.created_at, six.string_types)
        else:
            self.assertIsNone(volume.created_at)
        if volume.updated_at is not None:
            self.assertIsInstance(volume.updated_at, six.string_types)
        else:
            self.assertIsNone(volume.updated_at)
        self.assertIsInstance(volume.error_message, six.string_types)
        self.assertIsInstance(volume.target_ips, list)
        if volume.availability_zone is not None:
            self.assertIsInstance(volume.availability_zone, six.string_types)
        else:
            self.assertIsNone(volume.availability_zone)
        self.assertIsInstance(volume.snapshot_ids, list)
        # self.assertIsInstance(volume.encrypt, bool)

        # Only available for "piops_iscsi_na" or "piops_iscsi_na2" volumes
        self.assertIsInstance(volume.percentage_snapshot_reserve_used, six.integer_types)

        # Only available for "piops_iscsi_na" volumes
        # self.assertIsInstance(volume.iops_per_gb, six.integer_types)
        # self.assertIsInstance(volume.initiator_iqns, list)
        # self.assertIsNone(volume.initiator_secret)
        # self.assertIsNone(volume.target_secret)
        # self.assertIsInstance(volume.metadata, dict)

        # Only available for "piops_iscsi_na2" volumes
        self.assertIsInstance(volume.snapshot_reserve_size, six.integer_types)
        self.assertIsInstance(volume.snapshot_reserve_used, six.integer_types)

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
        assert isinstance(volume.id, six.string_types)
        assert isinstance(volume.name, six.string_types)
        if volume.description is not None:
            assert isinstance(volume.description, six.string_types)
        else:
            assert volume.description is None
        assert isinstance(volume.virtual_storage_id, six.string_types)
        assert isinstance(volume.status, six.string_types)
        assert isinstance(volume.size, six.integer_types)
        if volume.created_at is not None:
            assert isinstance(volume.created_at, six.string_types)
        else:
            assert volume.created_at is None
        if volume.updated_at is not None:
            assert isinstance(volume.updated_at, six.string_types)
        else:
            assert volume.updated_at is None
        assert isinstance(volume.error_message, six.string_types)
        assert isinstance(volume.target_ips, list)
        if volume.availability_zone is not None:
            assert isinstance(volume.availability_zone, six.string_types)
        else:
            assert volume.availability_zone is None
        assert isinstance(volume.snapshot_ids, list)
        # assert isinstance(volume.encrypt, bool)

        # Only available for "piops_iscsi_na" or "piops_iscsi_na2" volumes
        assert isinstance(volume.percentage_snapshot_reserve_used, six.integer_types)

        # Only available for "piops_iscsi_na" volumes
        # assert isinstance(volume.iops_per_gb, six.integer_types)
        # assert isinstance(volume.initiator_iqns, list)
        # assert volume.initiator_secret is None
        # assert volume.target_secret is None
        # assert isinstance(volume.metadata, dict)

        # Only available for "piops_iscsi_na2" volumes
        assert isinstance(volume.snapshot_reserve_size, six.integer_types)
        assert isinstance(volume.snapshot_reserve_used, six.integer_types)

        # Only available for "standard_nfs_na" or "standard_smb_na" volumes
        # assert isinstance(volume.export_rules, list)

        # Only available for "standard_smb_na" volumes
        # assert isinstance(volume.smb_properties, dict)

        cls.vol_id = volume.id

    def test_05_delete_volume(self):
        time.sleep(20)
        volume = self.conn.storage.delete_volume(self.vol_id)
