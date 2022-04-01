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


class TestChassis(base.BaseFunctionalTest):

    def test_chassis(self):
        chassis_list = list(self.conn.baremetal.chassis(details=False))
        self.assertGreater(len(chassis_list), 0)

        for chassis in chassis_list:
            print(chassis)
            self.assertIsInstance(chassis.id, six.string_types)
            self.assertIsInstance(chassis.availability_zone, six.string_types)
            self.assertIsInstance(chassis.flavor_name, six.string_types)
            self.assertIsInstance(chassis.hardware_summary, dict)
            self.assertIsInstance(chassis.status, six.string_types)
            self.assertIsInstance(chassis.server_id,
                                  (six.string_types, type(None)))
            self.assertIsInstance(chassis.server_name,
                                  (six.string_types, type(None)))
            self.assertIsInstance(chassis.contract_year, int)
            self.assertIsInstance(chassis.start_time, six.string_types)

    def test_chassis_detail(self):
        chassis_list = list(self.conn.baremetal.chassis(details=True))
        self.assertGreater(len(chassis_list), 0)

        for chassis in chassis_list:
            print(chassis)
            self.assertIsInstance(chassis.id, six.string_types)
            self.assertIsInstance(chassis.availability_zone, six.string_types)
            self.assertIsInstance(chassis.flavor_name, six.string_types)
            self.assertIsInstance(chassis.hardware_summary, dict)
            self.assertIsInstance(chassis.status, six.string_types)
            self.assertIsInstance(chassis.server_id,
                                  (six.string_types, type(None)))
            self.assertIsInstance(chassis.server_name,
                                  (six.string_types, type(None)))
            self.assertIsInstance(chassis.contract_year, int)
            self.assertIsInstance(chassis.start_time, six.string_types)

            self.assertIsInstance(chassis.cpus, list)
            self.assertIsInstance(chassis.disks, list)
            self.assertIsInstance(chassis.rams, list)

    def test_get_chassis(self):
        # ChassisIDはMock Serverに合わせて変更する
        chassis_id = '31e7a0c4-f49e-19e6-2192-c9f9cc6f5a74'

        chassis = self.conn.baremetal.get_chassis(chassis_id)
        print(chassis)
        # Mock Serverを使用するとランダムなUUIDが返却されるのでパスパラメータを一致しない
        # self.assertEqual(chassis.id, chassis_id)

        self.assertIsInstance(chassis.availability_zone, six.string_types)
        self.assertIsInstance(chassis.flavor_name, six.string_types)
        self.assertIsInstance(chassis.hardware_summary, dict)
        self.assertIsInstance(chassis.status, six.string_types)
        self.assertIsInstance(chassis.server_id,
                              (six.string_types, type(None)))
        self.assertIsInstance(chassis.server_name,
                              (six.string_types, type(None)))
        self.assertIsInstance(chassis.contract_year, int)
        self.assertIsInstance(chassis.start_time, six.string_types)

        self.assertIsInstance(chassis.cpus, list)
        self.assertIsInstance(chassis.disks, list)
        self.assertIsInstance(chassis.rams, list)
    