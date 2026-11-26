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

from ecl.compute.v2 import inplace_upgrade

IDENTIFIER = 'IDENTIFIER'
EXAMPLE = {
    'id': IDENTIFIER,
    'instance_id': 'ea5a4499-c71d-4af9-b58a-30a7bcf0a898',
    'status': 'Finished',
    'src_os': 'Windows2021',
    'dst_os': 'Windows2026',
    'created_at': '2022-10-01T00:00:00.000000',
    'upgrade_at': '2022-10-01T01:00:00.000000',
    'updated_at': '2022-10-01T02:00:00.000000',
}


class TestInplaceUpgrade(testtools.TestCase):

    def test_basic(self):
        sot = inplace_upgrade.InplaceUpgrade()
        self.assertEqual('inplace_upgrade', sot.resource_key)
        self.assertEqual('inplace_upgrades', sot.resources_key)
        self.assertEqual('/servers/%(server_id)s/inplace_upgrades',
                         sot.base_path)
        self.assertEqual('compute', sot.service.service_type)
        self.assertFalse(sot.allow_create)
        self.assertFalse(sot.allow_get)
        self.assertFalse(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertFalse(sot.allow_update)

    def test_make_it(self):
        sot = inplace_upgrade.InplaceUpgrade(**EXAMPLE)
        self.assertEqual(EXAMPLE['id'], sot.id)
        self.assertEqual(EXAMPLE['instance_id'], sot.instance_id)
        self.assertEqual(EXAMPLE['status'], sot.status)
        self.assertEqual(EXAMPLE['src_os'], sot.src_os)
        self.assertEqual(EXAMPLE['dst_os'], sot.dst_os)
        self.assertEqual(EXAMPLE['created_at'], sot.created_at)
        self.assertEqual(EXAMPLE['upgrade_at'], sot.upgrade_at)
        self.assertEqual(EXAMPLE['updated_at'], sot.updated_at)
