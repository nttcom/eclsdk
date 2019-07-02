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

from ecl.compute.v2 import keypair
from ecl.tests.functional import base


class TestKeypair(base.BaseFunctionalTest):

    @classmethod
    def setUpClass(cls):
        super(TestKeypair, cls).setUpClass()
        cls.one_keypair = None
        sots = cls.conn.compute.keypairs()
        if sots and len(sots) > 0:
            cls.one_keypair = sots[0]

    def test_list(self):
        names = [o.name for o in self.conn.compute.keypairs()]
        print(names)
        self.assertIn(self.one_keypair.name, names)

    def test_find(self):
        sot = self.conn.compute.find_keypair(self.one_keypair.name)
        self.assertEqual(self.one_keypair.id, sot.id)

    def test_get(self):
        sot = self.conn.compute.get_keypair(self.one_keypair.name)
        self.assertEqual(self.one_keypair.name, sot.name)
        self.assertEqual(self.one_keypair.id, sot.id)

    def test_create(self):
        test_name = "Test-Keypair"
        sot = self.conn.compute.create_keypair(test_name)
        self.assertIsInstance(sot, keypair.Keypair)

    def test_delete(self):
        sot = self.conn.compute.delete_keypair("Test-Keypair")
        self.assertIsNone(sot)
