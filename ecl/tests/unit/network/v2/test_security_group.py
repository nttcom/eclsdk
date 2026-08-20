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

from ecl.network.v2.security_group import SecurityGroup

IDENTIFIER = 'IDENTIFIER'
EXAMPLE = {
    "description": '1',
    "id": IDENTIFIER,
    "name": '2',
    "status": '3',
    "tags": {
        'tag1': '4',
        'tag2': '5'
    },
    "tenant_id": IDENTIFIER,
    "security_group_rules": [
        {
            'rule1': '6',
            'rule2': '7'
        }
    ]
}


class TestSecurityGroup(testtools.TestCase):

    def test_basic(self):
        sot = SecurityGroup()
        self.assertEqual('security_group', sot.resource_key)
        self.assertEqual('security_groups', sot.resources_key)
        self.assertEqual('/v2.0/security-groups', sot.base_path)
        self.assertEqual('network', sot.service.service_type)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_delete)

    def test_make_it(self):
        sot = SecurityGroup(**EXAMPLE)
        self.assertEqual(EXAMPLE['description'], sot.description)
        self.assertEqual(EXAMPLE['id'], sot.id)
        self.assertEqual(EXAMPLE['name'], sot.name)
        self.assertEqual(EXAMPLE['status'], sot.status)
        self.assertEqual(EXAMPLE['tags'], sot.tags)
        self.assertEqual(EXAMPLE['tenant_id'], sot.tenant_id)
        self.assertEqual(EXAMPLE['security_group_rules'], sot.security_group_rules)
