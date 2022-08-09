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

from ecl.managed_rdb.v1 import flavor

IDENTIFIER = 'IDENTIFIER'
FLAVOR_EXAMPLE = {
    'id': IDENTIFIER,
    'name': '4CPU-32GB',
    'core': 4,
    'memory': 32,
}


class TestFlavor(testtools.TestCase):

    def test_basic(self):
        sot = flavor.Flavor()
        self.assertEqual('flavors', sot.resources_key)
        self.assertEqual('flavor', sot.resource_key)
        self.assertEqual('/v1.0/flavors', sot.base_path)
        self.assertEqual('managed-rdb', sot.service.service_type)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_list)

    def test_make_basic(self):
        sot = flavor.Flavor(**FLAVOR_EXAMPLE)
        self.assertEqual(FLAVOR_EXAMPLE['id'], sot.id)
        self.assertEqual(FLAVOR_EXAMPLE['name'], sot.name)
        self.assertEqual(FLAVOR_EXAMPLE['core'], sot.core)
        self.assertEqual(FLAVOR_EXAMPLE['memory'], sot.memory)
