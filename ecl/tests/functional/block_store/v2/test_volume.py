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

from ecl.block_store.v2 import volume as _volume
from ecl.tests.functional import base


class TestVolume(base.BaseFunctionalTest):

    @classmethod
    def setUpClass(cls):
        super(TestVolume, cls).setUpClass()
        cls.test_name = "test_volume_sdk"
        volumes = cls.conn.block_store.volumes()
        cls.one_volume = None
        for vol in volumes:
            if vol.name == cls.test_name:
                cls.one_volume = vol
                break
        if cls.one_volume is None:
            cls.one_volume = cls.conn.block_store.create_volume(
                15, name=cls.test_name)

    # def test_list(self):
    #     sots = self.conn.block_store.volumes()
    #     for sot in sots:
    #         self.assertIsInstance(sot.id, six.string_types)
    #
    # def test_get(self):
    #     sot = self.conn.block_store.get_volume(self.one_volume.id)
    #     self.assertEqual(self.one_volume.id, sot.id)
    #     self.assertEqual(self.one_volume.name, sot.name)
    #
    # def test_create(self):
    #     sot = self.conn.block_store.create_volume(15, name=self.test_name)
    #     self.one_volume = sot
    #     vol = self.conn.block_store.get_volume(sot.id)
    #     self.assertEqual(vol.size, 15)
    #     self.assertIsInstance(vol.id, six.string_types)
    #     self.assertIsInstance(vol.name, six.string_types)
    #
    # def test_delete(self):
    #     ret = self.conn.block_store.delete_volume(self.one_volume)
    #     self.assertIsNone(ret)
    #
    # def test_update(self):
    #     self.conn.block_store.update_volume(self.one_volume.id,
    #                                         name="test_sdk_volume")
    #     self.assertEqual(self.one_volume.size, 15)
    #     self.assertIsInstance(self.one_volume.id, six.string_types)
    #     self.assertIsInstance(self.one_volume.name, six.string_types)
    #
    # def test_extend(self):
    #     vol = self.conn.block_store.extend_volume(self.one_volume.id, 1)
    #     self.assertIsInstance(vol.id, six.string_types)
    #
    # def test_upload2image(self):
    #     self.conn.block_store.upload_to_image(self.one_volume,
    #                                           image_name="test_sdk_vol2image")

    def test_update_bootable(self):
        self.conn.block_store.update_bootable(self.one_volume, True)
