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


class TestImage(base.BaseFunctionalTest):
    def test_01_list_image(self):
        images = list(self.conn.image.images(limit=5))
        image = images[0]
        self.assertIsInstance(image.name, six.string_types)
        self.assertIsInstance(image.image_status, six.string_types)
        self.assertIsInstance(image.tags, list)
        self.assertIsInstance(image.container_format, six.string_types)
        self.assertIsInstance(image.created_at, six.string_types)
        self.assertIsInstance(image.disk_format, six.string_types)
        self.assertIsInstance(image.locations, list)
        # self.assertIsInstance(image.direct_url, six.string_types)
        self.assertIsInstance(image.updated_at, six.string_types)
        self.assertIsInstance(image.visibility, six.string_types)
        self.assertIsInstance(image.min_disk, int)
        self.assertIsInstance(image.protected, bool)
        self.assertIsInstance(image.id, six.string_types)
        self.assertIsInstance(image.file, six.string_types)
        # self.assertIsInstance(image.checksum, six.string_types)
        self.assertIsInstance(image.owner, six.string_types)
        # self.assertIsInstance(image.size, int)
        self.assertIsInstance(image.min_ram, int)
        # self.assertIsInstance(image.image_schema, six.string_types)
        self.assertIsInstance(image.images_schema, six.string_types)
        self.assertIsInstance(image.first, six.string_types)

        # print(images)
        assert False

    @classmethod
    def test_02_create_image(cls):
        img = cls.conn.image.create_image(
            name="TEST_IMAGE_NAME",
            disk_format='raw',
            container_format='bare',
            properties='{"description": "This is not an image"}',
            # data=open('CONTRIBUTING.rst', 'r')
        )
        cls.id = img.id
        print(img)
    # id=5e9a2627-2acf-4ebf-b210-ffa75de9c1be

    def test_03_update_image(self):
        img = self.conn.image.update_image(
            "1b782d43-4e43-4d96-883b-ff423f8b8b7c",
            [{"path": "/name", "value": "sdk_test", "op": "replace"}]
        )
        print(img)

    def test_04_show_image(self):
        image = self.conn.image.get_image(
            "1b782d43-4e43-4d96-883b-ff423f8b8b7c")
        print(image.response)

    def test_05_delete_image(self):
        self.conn.image.delete_image(
            "5e9a2627-2acf-4ebf-b210-ffa75de9c1be")

    def test_06_upload_image(self):
        self.conn.image.upload_image(
            # self.id,
            "fake_id",
            "raw_data"
        )

    def test_07_download_image(self):
        image = self.conn.image.download_image(
            "1b782d43-4e43-4d96-883b-ff423f8b8b7c"
        )
        print(image)
