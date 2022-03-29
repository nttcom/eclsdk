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


class TestInstance(base.BaseFunctionalTest):

    @classmethod
    def test_01_create(cls):
        instance = cls.conn.managed_rdb.create_instance(
            '4CPU-32GB',
            'POSTGRES_13_2',
            '4IOPS-500GB',
            True,
            {
                'id': '497f6eca-6276-4993-bfeb-53cbbbba6f08',
                'ip_address': '192.168.10.10',
                'reserved_addresses': ['192.168.10.11', '192.168.10.12'],
            }
        )
        cls.instance_id = instance.id
        print(instance)
        assert isinstance(instance.id, six.string_types)

    def test_02_list(self):
        instances = list(self.conn.managed_rdb.instances(
            limit="10",
        ))
        instance = instances[0]
        print(instance)
        self.assertIsInstance(instance.id, six.string_types)

    def test_03_list_detail(self):
        instances = list(self.conn.managed_rdb.instances(details=True))
        instance = instances[0]
        print(instance)
        self.assertIsInstance(instance.id, six.string_types)

    def test_04_show_instance(self):
        instance = self.conn.managed_rdb.get_instance("752aac2e-4b82-4d47-a7c7-fcbd0cbc86e2")
        print(instance)
        self.assertIsInstance(instance.id, six.string_types)
        self.assertIsInstance(instance.tenant_id, six.string_types)
        self.assertIsInstance(instance.name, six.string_types)
        self.assertIsInstance(instance.description, six.string_types)
        self.assertIsInstance(instance.flavor, dict)
        self.assertIsInstance(instance.database_version, dict)
        self.assertIsInstance(instance.storage_type, dict)
        self.assertIsInstance(instance.high_availability, bool)
        self.assertIsInstance(instance.status, six.string_types)
        self.assertIsInstance(instance.task_type, six.string_types)
        self.assertIsInstance(instance.task_state, six.string_types)
        self.assertIsInstance(instance.monitoring_state, six.string_types)
        self.assertIsInstance(instance.availability_zone, six.string_types)
        self.assertIsInstance(instance.network, dict)
        self.assertIsInstance(instance.metadata, dict)
        self.assertIsInstance(instance.links, list)
        self.assertIsInstance(instance.created, six.string_types)
        self.assertIsNone(instance.admin_password)

    def test_05_delete_instance(self):
        # IDはMock Serverに合わせて変更する
        instance_id = "2ecd05a0-0a87-986c-b9e5-2232077a17ee"
        self.conn.managed_rdb.delete_instance(instance_id)
        assert True

    def test_06_update_instance(self):
        # IDはMock Serverに合わせて変更する
        instance_id = "2a18cb19-d2b4-cbf3-b627-be31e88eaf33"
        name = "hoge"
        description = "fuga"

        instance = self.conn.managed_rdb.update_instance(instance_id, name=name,
                                                         description=description)
        print(instance)
        self.assertIsInstance(instance.id, six.string_types)

    def test_07_find_instance(self):
        # IDはMock Serverに合わせて変更する
        instance_id = "497f6eca-6276-4993-bfeb-53cbbbba6f08"
        instance = self.conn.managed_rdb.find_instance(instance_id)
        self.assertIsInstance(instance.id, six.string_types)
