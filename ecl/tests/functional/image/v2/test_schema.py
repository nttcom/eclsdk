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


class TestScheme(base.BaseFunctionalTest):
    image_id = "1b782d43-4e43-4d96-883b-ff423f8b8b7c"

    def test_01_get_image_schema(self):
        scheme = self.conn.image.get_image_schema()
        self.assertIsInstance(scheme.additionalProperties, dict)
        self.assertIsInstance(scheme.links, list)
        self.assertIsInstance(scheme.name, six.string_types)
        self.assertIsInstance(scheme.properties, dict)

    def test_02_get_images_schema(self):
        scheme = self.conn.image.get_images_schema()
        self.assertIsInstance(scheme.links, list)
        self.assertIsInstance(scheme.name, six.string_types)
        self.assertIsInstance(scheme.properties, dict)

    def test_03_get_image_member_schema(self):
        scheme = self.conn.image.get_image_member_schema()
        self.assertIsInstance(scheme.name, six.string_types)
        self.assertIsInstance(scheme.properties, dict)

    def test_04_get_metadata_namespace_schema(self):
        scheme = self.conn.image.get_metadata_namespace_schema()
        # self.assertIsInstance(scheme.additionalProperties, dict)
        self.assertIsInstance(scheme.definitions, dict)
        self.assertIsInstance(scheme.name, six.string_types)
        self.assertIsInstance(scheme.properties, dict)

    def test_05_get_metadata_object_schema(self):
        scheme = self.conn.image.get_metadata_object_schema()
        # self.assertIsInstance(scheme.additionalProperties, dict)
        self.assertIsInstance(scheme.definitions, dict)
        self.assertIsInstance(scheme.name, six.string_types)
        self.assertIsInstance(scheme.properties, dict)

    def test_06_get_metadata_property_schema(self):
        scheme = self.conn.image.get_metadata_property_schema()
        # self.assertIsInstance(scheme.additionalProperties, dict)
        self.assertIsInstance(scheme.definitions, dict)
        self.assertIsInstance(scheme.name, six.string_types)
        self.assertIsInstance(scheme.properties, dict)

    def test_07_get_metadata_resource_type_schema(self):
        scheme = self.conn.image.get_metadata_property_schema()
        # self.assertIsInstance(scheme.additionalProperties, dict)
        self.assertIsInstance(scheme.definitions, dict)
        self.assertIsInstance(scheme.name, six.string_types)
        self.assertIsInstance(scheme.properties, dict)
