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

from ecl.network.v2.security_group_rule import SecurityGroupRule

IDENTIFIER = 'IDENTIFIER'
EXAMPLE = {
    'description': '1',
    'direction': '2',
    'ethertype': '3',
    'id': IDENTIFIER,
    'port_range_min': 4,
    'port_range_max': 5,
    'protocol': '6',
    'remote_group_id': IDENTIFIER,
    'remote_ip_prefix': '7',
    'security_group_id': IDENTIFIER,
    'tenant_id': IDENTIFIER,
}


class TestSecurityGroupRule(testtools.TestCase):

    def test_basic(self):
        sot = SecurityGroupRule()
        self.assertEqual('security_group_rule', sot.resource_key)
        self.assertEqual('security_group_rules', sot.resources_key)
        self.assertEqual('/v2.0/security-group-rules', sot.base_path)
        self.assertEqual('network', sot.service.service_type)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_get)
        self.assertFalse(sot.allow_update)
        self.assertTrue(sot.allow_delete)

    def test_make_it(self):
        sot = SecurityGroupRule(**EXAMPLE)
        self.assertEqual(EXAMPLE['description'], sot.description)
        self.assertEqual(EXAMPLE['direction'], sot.direction)
        self.assertEqual(EXAMPLE['ethertype'], sot.ethertype)
        self.assertEqual(EXAMPLE['id'], sot.id)
        self.assertEqual(EXAMPLE['port_range_min'], sot.port_range_min)
        self.assertEqual(EXAMPLE['port_range_max'], sot.port_range_max)
        self.assertEqual(EXAMPLE['protocol'], sot.protocol)
        self.assertEqual(EXAMPLE['remote_group_id'], sot.remote_group_id)
        self.assertEqual(EXAMPLE['remote_ip_prefix'], sot.remote_ip_prefix)
        self.assertEqual(EXAMPLE['security_group_id'], sot.security_group_id)
        self.assertEqual(EXAMPLE['tenant_id'], sot.tenant_id)
