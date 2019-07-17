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


class TestVirtualStorage(base.BaseFunctionalTest):
    def test_01_list_virtual_storages(self):
        vs = list(self.conn.storage.storages(False))
        print(vs)

    @classmethod
    def test_02_create_virtual_storage(cls):
        vs = cls.conn.storage.create_storage(
            name="test-vs01-for-heat",
            network_id="9d28c903-2bba-4900-a719-ab230a32b10b",
            subnet_id="01c7f86b-a653-40fb-ab9c-ea7b8bb21f69",
            volume_type_id="6328d234-7939-4d61-9216-736de66d15f9",
            ip_addr_pool={"start": "10.1.1.21",
                          "end": "10.1.1.30"}

        )
        cls.id = vs.id
        assert isinstance(vs.status, six.string_types)
        assert isinstance(vs.id, six.string_types)
        assert isinstance(vs.volume_type_id, six.string_types)
        assert isinstance(vs.name, six.string_types)
        assert isinstance(vs.network_id, six.string_types)
        assert isinstance(vs.ip_addr_pool, dict)
        assert isinstance(vs.subnet_id, six.string_types)
        assert isinstance(vs.host_routes, list)

    def test_03_show_virtual_storage(self):
        vs = self.conn.storage.get_storage(
            self.id
        )
        print(vs)
        self.assertIsInstance(vs.subnet_id, six.string_types)
        self.assertIsInstance(vs.host_routes, list)
        self.assertIsInstance(vs.status, six.string_types)
        self.assertIsInstance(vs.id, six.string_types)
        self.assertIsInstance(vs.volume_type_id, six.string_types)
        self.assertIsInstance(vs.name, six.string_types)
        self.assertIsInstance(vs.network_id, six.string_types)
        self.assertIsInstance(vs.ip_addr_pool, dict)

    def test_04_update_virtual_storage(self):
        vs = self.conn.storage.update_storage(
            self.id,
            description="sdk test"
        )
        self.assertIsInstance(vs.subnet_id, six.string_types)
        self.assertIsInstance(vs.host_routes, list)
        self.assertIsInstance(vs.status, six.string_types)
        self.assertIsInstance(vs.id, six.string_types)
        self.assertIsInstance(vs.volume_type_id, six.string_types)
        self.assertIsInstance(vs.name, six.string_types)
        self.assertIsInstance(vs.network_id, six.string_types)
        self.assertIsInstance(vs.ip_addr_pool, dict)
        self.assertIsInstance(vs.description, six.string_types)
        print(vs.description)

    def test_05_delete_virtual_storage(self):
        vs = self.conn.storage.delete_storage(
            self.id
        )
