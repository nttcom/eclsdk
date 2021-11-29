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


class TestServer(base.BaseFunctionalTest):

    @classmethod
    def test_01_create(cls):
        server = cls.conn.baremetal.create_server(
            server={
                "name": "SDK-TEST-BARE-02",
                "flavorRef": "462f4f62-0b0a-4171-acfc-a3840fd50b4b",
                "imageRef": "4fc19fa6-4643-44bd-a52d-5388d4d011b1",
                "networks": [{"uuid": "4fdac559-914e-41b2-9e58-e5a36ba437dd"}]
            }
        )
        cls.server_id = server.id
        print(server)
        assert isinstance(server.id, six.string_types)

    def test_02_list(self):
        servers = list(self.conn.baremetal.servers(
            limit="10",
        ))
        server = servers[0]
        print(server)
        self.assertIsInstance(server.id, six.string_types)

    def test_03_list_detail(self):
        servers = list(self.conn.baremetal.servers(details=True))
        server = servers[0]
        print(server)
        self.assertIsInstance(server.id, six.string_types)

    def test_04_show_server(self):
        server = self.conn.baremetal.get_server("752aac2e-4b82-4d47-a7c7-fcbd0cbc86e2")
        print(server)
        self.assertIsInstance(server.OS_EXT_STS_power_state, six.string_types)
        self.assertIsInstance(server.OS_EXT_STS_task_state, six.string_types)
        self.assertIsInstance(server.OS_EXT_STS_vm_state, six.string_types)
        self.assertIsInstance(server.OS_EXT_AZ_availability_zone, six.string_types)
        self.assertIsInstance(server.created, six.string_types)
        self.assertIsInstance(server.flavor, dict)
        # self.assertIsInstance(server.hostId, six.string_types)
        self.assertIsInstance(server.image, dict)
        self.assertIsInstance(server.metadata, dict)
        self.assertIsInstance(server.links, list)
        self.assertIsInstance(server.progress, int)
        self.assertIsInstance(server.status, six.string_types)
        self.assertIsInstance(server.tenant_id, six.string_types)
        self.assertIsInstance(server.updated, six.string_types)
        self.assertIsInstance(server.user_id, six.string_types)
        self.assertIsInstance(server.raid_arrays, list)
        # self.assertIsInstance(server.lvm_volume_groups, list)
        # self.assertIsInstance(server.filesystems, list)
        self.assertIsInstance(server.nic_physical_ports, list)
        self.assertIsInstance(server.chassis_status, dict)

    def test_05_delete_server(self):
        server = self.conn.baremetal.delete_server("752aac2e-4b82-4d47-a7c7-xx")
        assert False
