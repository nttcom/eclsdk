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

from ecl.network.v2 import quota

IDENTIFIER = 'IDENTIFIER'
EXAMPLE = {
    "colocation_logical_link": 2,
    "common_function_gateway": 1,
    "firewall": 2,
    "id": IDENTIFIER,
    "interdc_gateway": 1,
    "internet_gateway": 1,
    "load_balancer": 2,
    "network": 2,
    "port": 30,
    "subnet": 5,
    "tenant_id": IDENTIFIER,
    "vpn_gateway": 1
}



class TestQuota(testtools.TestCase):

    def test_basic(self):
        sot = quota.Quota()
        self.assertEqual('quota', sot.resource_key)
        self.assertEqual('quotas', sot.resources_key)
        self.assertEqual('/quotas', sot.base_path)
        self.assertEqual('network', sot.service.service_type)
        self.assertFalse(sot.allow_create)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)

    def test_make_it(self):
        sot = quota.Quota(**EXAMPLE)
        self.assertEqual(EXAMPLE['colocation_logical_link'], sot.colocation_logical_link)
        self.assertEqual(EXAMPLE['common_function_gateway'], sot.common_function_gateway)
        self.assertEqual(EXAMPLE['firewall'], sot.firewall)
        self.assertEqual(EXAMPLE['id'], sot.id)
        self.assertEqual(EXAMPLE['interdc_gateway'], sot.interdc_gateway)
        self.assertEqual(EXAMPLE['interdc_gateway'], sot.internet_gateway)
        self.assertEqual(EXAMPLE['load_balancer'], sot.load_balancer)
        self.assertEqual(EXAMPLE['network'], sot.networks)
        self.assertEqual(EXAMPLE['port'], sot.ports)
        self.assertEqual(EXAMPLE['subnet'], sot.subnets)
        self.assertEqual(EXAMPLE['tenant_id'], sot.project_id)
        self.assertEqual(EXAMPLE['vpn_gateway'], sot.vpn_gateway)

class TestQuotaDefault(testtools.TestCase):

    def test_basic(self):
        default = quota.QuotaDefault()
        self.assertEqual('quota', default.resource_key)
        self.assertEqual('quotas', default.resources_key)
        self.assertEqual('/quotas/%(project)s/default', default.base_path)
        self.assertEqual('network', default.service.service_type)
        self.assertFalse(default.allow_create)
        self.assertTrue(default.allow_get)
        self.assertFalse(default.allow_update)
        self.assertFalse(default.allow_delete)
        self.assertFalse(default.allow_list)

    def test_make_it(self):
        default = quota.QuotaDefault(**EXAMPLE)
        self.assertEqual(EXAMPLE['colocation_logical_link'], default.colocation_logical_link)
        self.assertEqual(EXAMPLE['common_function_gateway'], default.common_function_gateway)
        self.assertEqual(EXAMPLE['firewall'], default.firewall)
        self.assertEqual(EXAMPLE['id'], default.id)
        self.assertEqual(EXAMPLE['interdc_gateway'], default.interdc_gateway)
        self.assertEqual(EXAMPLE['interdc_gateway'], default.internet_gateway)
        self.assertEqual(EXAMPLE['load_balancer'], default.load_balancer)
        self.assertEqual(EXAMPLE['network'], default.networks)
        self.assertEqual(EXAMPLE['port'], default.ports)
        self.assertEqual(EXAMPLE['subnet'], default.subnets)
        self.assertEqual(EXAMPLE['tenant_id'], default.project_id)
        self.assertEqual(EXAMPLE['vpn_gateway'], default.vpn_gateway)
