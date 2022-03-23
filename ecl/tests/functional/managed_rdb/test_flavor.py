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


class TestFlavor(base.BaseFunctionalTest):

    def test_flavors(self):
        flavor_list = list(self.conn.managed_rdb.flavors())
        print(flavor_list)
        self.assertGreater(len(flavor_list), 0)

        for flavor in flavor_list:
            print(flavor)
            self.assertIsInstance(flavor.id, six.string_types)
            self.assertIsInstance(flavor.name, six.string_types)
            self.assertIsInstance(flavor.core, int)
            self.assertIsInstance(flavor.memory, int)

    def test_get_flavor(self):
        flavor = self.conn.managed_rdb.get_flavor('4CPU-32GB')
        print(flavor)
        self.assertIsInstance(flavor.id, six.string_types)
        self.assertIsInstance(flavor.name, six.string_types)
        self.assertIsInstance(flavor.core, int)
        self.assertIsInstance(flavor.memory, int)
