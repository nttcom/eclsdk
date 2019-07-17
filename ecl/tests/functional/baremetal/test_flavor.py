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

    @classmethod
    def setUpClass(cls):
        super(TestFlavor, cls).setUpClass()

        cls.one_flavor = list(cls.conn.baremetal.flavors())[0]

    def test_flavors(self):
        flavors = list(self.conn.baremetal.flavors())
        self.assertGreater(len(flavors), 0)

        for flavor in flavors:
            self.assertIsInstance(flavor.id, six.string_types)
            self.assertIsInstance(flavor.links, list)

    def test_flavors_detail(self):
        flavors = list(self.conn.baremetal.flavors_detail())
        self.assertGreater(len(flavors), 0)

        for flavor in flavors:
            self.assertIsInstance(flavor.id, six.string_types)
            self.assertIsInstance(flavor.name, six.string_types)
            self.assertIsInstance(flavor.links, list)
            self.assertIsInstance(flavor.ram, int)
            self.assertIsInstance(flavor.vcpus, int)
            self.assertIsInstance(flavor.disk, int)

    def test_get_flavor(self):
        flavor = self.conn.baremetal.get_flavor(self.one_flavor.id)
        self.assertEqual(flavor.id, self.one_flavor.id)

    def test_find_flavor_by_id(self):
        flavor = self.conn.baremetal.find_flavor(self.one_flavor.id)
        self.assertEqual(flavor.id, self.one_flavor.id)

    def test_find_flavor_by_name(self):
        flavor = self.conn.baremetal.find_flavor(self.one_flavor.name)
        self.assertEqual(flavor.id, self.one_flavor.id)
