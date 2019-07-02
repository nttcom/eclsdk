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


class TestVolumeType(base.BaseFunctionalTest):
    def test_01_volume_types(self):
        types = list(self.conn.storage.volume_types(False))
        type = types[0]
        self.assertIsInstance(type.extra_specs, dict)
        self.assertIsInstance(type.id, six.string_types)
        self.assertIsInstance(type.name, six.string_types)

    def test_02_get_volume_type(self):
        type = self.conn.storage.get_volume_type(
            "6328d234-7939-4d61-9216-736de66d15f9"
        )
        self.assertIsInstance(type.extra_specs, dict)
        self.assertIsInstance(type.id, six.string_types)
        self.assertIsInstance(type.name, six.string_types)
