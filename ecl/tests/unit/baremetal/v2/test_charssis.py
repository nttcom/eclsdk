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

from ecl.baremetal.v2 import chassis

IDENTIFIER = 'IDENTIFIER'
CHASSIS_EXAMPLE = {
    'id': IDENTIFIER,
    'availability_zone': '2',
    'flavor_name': '3',
    'hardware_summary': {'4': 4},
    'status': '5',
    'server_id': '6',
    'server_name': '7',
    'contract_year': 8,
    'start_time': '9',
}

CHASSIS_DETAIL_EXAMPLE = {
    'id': IDENTIFIER,
    'availability_zone': '2',
    'flavor_name': '3',
    'hardware_summary': {'4': 4},
    'status': '5',
    'server_id': '6',
    'server_name': '7',
    'contract_year': 8,
    'start_time': '9',
    'cpus': [{'10': 10},],
    'disks': [{'11': 11},],
    'rams': [{'12': 12},],
}
from unittest.mock import patch

class TestChassis(testtools.TestCase):

    def test_basic(self):
        sot = chassis.Chassis()
        self.assertEqual('chassis', sot.resource_key)
        self.assertEqual('chassis', sot.resources_key)
        self.assertEqual('/chassis', sot.base_path)
        self.assertEqual('baremetal-server', sot.service.service_type)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_list)
        self.assertFalse(sot.allow_create)
        self.assertFalse(sot.allow_delete)
        self.assertFalse(sot.allow_update)
        self.assertFalse(sot.allow_head)

    def test_make_basic(self):
        sot = chassis.Chassis(**CHASSIS_EXAMPLE)
        self.assertEqual(CHASSIS_EXAMPLE['id'], sot.id)
        self.assertEqual(CHASSIS_EXAMPLE['availability_zone'], sot.availability_zone)
        self.assertEqual(CHASSIS_EXAMPLE['flavor_name'], sot.flavor_name)
        self.assertEqual(CHASSIS_EXAMPLE['hardware_summary'], sot.hardware_summary)
        self.assertEqual(CHASSIS_EXAMPLE['status'], sot.status)
        self.assertEqual(CHASSIS_EXAMPLE['server_id'], sot.server_id)
        self.assertEqual(CHASSIS_EXAMPLE['server_name'], sot.server_name)
        self.assertEqual(CHASSIS_EXAMPLE['contract_year'], sot.contract_year)
        self.assertEqual(CHASSIS_EXAMPLE['start_time'], sot.start_time)

    def test_detail(self):
        sot = chassis.ChassisDetail()
        self.assertEqual('chassis', sot.resource_key)
        self.assertEqual('chassis', sot.resources_key)
        self.assertEqual('/chassis/detail', sot.base_path)
        self.assertEqual('baremetal-server', sot.service.service_type)
        self.assertFalse(sot.allow_get)
        self.assertTrue(sot.allow_list)
        self.assertFalse(sot.allow_create)
        self.assertFalse(sot.allow_delete)
        self.assertFalse(sot.allow_update)
        self.assertFalse(sot.allow_head)

    def test_make_detail(self):
        sot = chassis.ChassisDetail(**CHASSIS_DETAIL_EXAMPLE)
        self.assertEqual(CHASSIS_DETAIL_EXAMPLE['id'], sot.id)
        self.assertEqual(CHASSIS_DETAIL_EXAMPLE['availability_zone'], sot.availability_zone)
        self.assertEqual(CHASSIS_DETAIL_EXAMPLE['flavor_name'], sot.flavor_name)
        self.assertEqual(CHASSIS_DETAIL_EXAMPLE['hardware_summary'], sot.hardware_summary)
        self.assertEqual(CHASSIS_DETAIL_EXAMPLE['status'], sot.status)
        self.assertEqual(CHASSIS_DETAIL_EXAMPLE['server_id'], sot.server_id)
        self.assertEqual(CHASSIS_DETAIL_EXAMPLE['server_name'], sot.server_name)
        self.assertEqual(CHASSIS_DETAIL_EXAMPLE['contract_year'], sot.contract_year)
        self.assertEqual(CHASSIS_DETAIL_EXAMPLE['start_time'], sot.start_time)
        self.assertEqual(CHASSIS_DETAIL_EXAMPLE['cpus'], sot.cpus)
        self.assertEqual(CHASSIS_DETAIL_EXAMPLE['disks'], sot.disks)
        self.assertEqual(CHASSIS_DETAIL_EXAMPLE['rams'], sot.rams)
