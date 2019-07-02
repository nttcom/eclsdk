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

from ecl.compute.v2 import server
from ecl.tests.functional import base


class TestServer(base.BaseFunctionalTest):
    @classmethod
    def setUpClass(cls):
        super(TestServer, cls).setUpClass()
        instance_name = "test_sdk_server"
        cls.one_server = cls.conn.compute.find_server(instance_name)
        cls.one_serverif = None
        if cls.one_server is None:
            network_name = "test-network"
            cls.network = cls.conn.network.find_network(network_name)
            if cls.network is None:
                cls.conn.network.create_network(
                    name=network_name
                )
            if not cls.network:
                # We can't call TestCase.fail from within the setUpClass
                # classmethod, but we need to raise some exception in order
                # to get this setup to fail and thusly fail the entire class.
                raise Exception("Unable to create network for TestServer")
            subnet_name = "test_subnet"
            cls.subnet = cls.conn.network.find_subnet(subnet_name)
            if cls.subnet is None:
                cls.subnet = cls.conn.network.create_subnet(
                    cls.network.id, "172.16.12.0/24", name=subnet_name
                )
            if not cls.subnet:
                # We can't call TestCase.fail from within the setUpClass
                # classmethod, but we need to raise some exception in order
                # to get this setup to fail and thusly fail the entire class.
                raise Exception("Unable to create subnet for TestServer")

            cls.flavor = "1CPU-4GB"
            cls.image = "ad936ae4-2983-4f23-9187-e47e82cb2725"

            cls.one_server = cls.conn.compute.create_server(
                name=instance_name, flavor_id=cls.flavor, image_id=cls.image,
                networks=[{"uuid": cls.network.id}])
            cls.conn.compute.wait_for_server(cls.one_server)
        assert isinstance(cls.one_server, server.Server)
        cls.assertIs(cls.one_server.name, instance_name)

        ifs = cls.conn.compute.server_interfaces(cls.one_server.id)
        if ifs:
            cls.one_serverif = ifs[0]

    def test_create(self):
        one_server = self.conn.compute.create_server(
            name=self.one_server.name, flavor_id=self.one_server.flavorRef,
            image_id=self.one_server.imageRef,
            networks=[{"uuid": self.network.id}])
        self.conn.compute.wait_for_server(one_server)

    def test_delete(self):
        instance_name = "test_sdk_server"
        one_server = self.conn.compute.find_server(instance_name)
        if one_server is not None:
            self.conn.compute.delete_servers(one_server.id)
            self.conn.compute.wait_for_delete(one_server)

    def test_find(self):
        sot = self.conn.compute.find_server(self.one_server.name)
        self.assertEqual(self.one_server.id, sot.id)

    def test_get(self):
        sot = self.conn.compute.get_server(self.one_server.id)
        self.assertEqual(self.one_server.name, sot.name)
        self.assertEqual(self.one_server.id, sot.id)

    def test_list(self):
        names = [o.name for o in self.conn.compute.servers()]
        self.assertIn(self.one_server.name, names)

    def test_update(self):
        self.conn.compute.update_server(self.one_server.id, name="test_sdk_server")
        self.assertEqual(self.one_server.name, "test_sdk_server")

    def test_get_console(self):
        console = self.conn.compute.get_server_console(self.one_server.id,
                                                       vnc_type="novnc")
        self.assertEqual("novnc", console.get("type"))

    def test_start(self):
        ret = self.conn.compute.start_server(self.one_server.id)
        self.assertIsNotNone(ret)

    def test_stop(self):
        ret = self.conn.compute.stop_server(self.one_server.id)
        self.assertIsNotNone(ret)

    def test_resize(self):
        ret = self.conn.compute.resize_server(self.one_server.id, "2CPU-8GB")
        self.assertIsNotNone(ret)

    def test_server_metadata(self):
        test_server = self.conn.compute.get_server(self.one_server.id)

        # get metadata
        test_server = self.conn.compute.get_server_metadata(test_server)
        self.assertFalse(test_server.metadata)

        # set no metadata
        self.conn.compute.set_server_metadata(test_server)
        test_server = self.conn.compute.get_server_metadata(test_server)
        self.assertFalse(test_server.metadata)

        # set empty metadata
        self.conn.compute.set_server_metadata(test_server, k0='')
        server = self.conn.compute.get_server_metadata(test_server)
        self.assertTrue(server.metadata)

        # set metadata
        self.conn.compute.set_server_metadata(test_server, k1='v1')
        test_server = self.conn.compute.get_server_metadata(test_server)
        self.assertTrue(test_server.metadata)
        self.assertEqual(2, len(test_server.metadata))
        self.assertIn('k0', test_server.metadata)
        self.assertEqual('', test_server.metadata['k0'])
        self.assertIn('k1', test_server.metadata)
        self.assertEqual('v1', test_server.metadata['k1'])

        # set more metadata
        self.conn.compute.set_server_metadata(test_server, k2='v2')
        test_server = self.conn.compute.get_server_metadata(test_server)
        self.assertTrue(test_server.metadata)
        self.assertEqual(3, len(test_server.metadata))
        self.assertIn('k0', test_server.metadata)
        self.assertEqual('', test_server.metadata['k0'])
        self.assertIn('k1', test_server.metadata)
        self.assertEqual('v1', test_server.metadata['k1'])
        self.assertIn('k2', test_server.metadata)
        self.assertEqual('v2', test_server.metadata['k2'])

        # update metadata
        self.conn.compute.set_server_metadata(test_server, k1='v1.1')
        test_server = self.conn.compute.get_server_metadata(test_server)
        self.assertTrue(test_server.metadata)
        self.assertEqual(3, len(test_server.metadata))
        self.assertIn('k0', test_server.metadata)
        self.assertEqual('', test_server.metadata['k0'])
        self.assertIn('k1', test_server.metadata)
        self.assertEqual('v1.1', test_server.metadata['k1'])
        self.assertIn('k2', test_server.metadata)
        self.assertEqual('v2', test_server.metadata['k2'])

        # delete metadata
        self.conn.compute.delete_server_metadata(
            test_server, test_server.metadata.keys())
        test_server = self.conn.compute.get_server_metadata(test_server)
        self.assertFalse(test_server.metadata)

    def test_server_interfaces(self):
        ifs = self.conn.compute.server_interfaces(self.one_server.id)
        self.assertGreaterEqual(len(ifs), 0)

    def test_create_server_interface(self):
        network_list = self.conn.network.networks()
        network_id = None
        if len(network_list) > 0:
            networ_id = network_list[0].id
        server_if = self.conn.compute.create_server_interface(
            self.one_server.id, net_id=network_id)
        self.assertEqual(server_if.server_id, self.one_server.id)
        self.assertEqual(server_if.net_id, network_id)

    def test_delete_server_interface(self):
        ifs = self.conn.compute.server_interfaces(self.one_server.id)
        if_delete = None
        if len(ifs) > 0:
            if_delete = ifs[-1]
        ret = self.conn.compute.delete_server_interface(
            if_delete, self.one_server.id)
        self.assertIsNone(ret)

    def test_server_actions(self):
        actions = self.conn.compute.server_actions(self.one_server.id)
        self.assertGreaterEqual(len(actions), 0)

    def test_get_server_actions(self):
        actions = self.conn.compute.server_actions(self.one_server.id)
        action_id = None
        if len(actions) > 0:
            action_id = actions[0].request_id
        print(action_id)
        action = self.conn.compute.get_server_action(action_id, self.one_server.id)
        print(action)
        self.assertEqual(action.request_id, action_id)

    def test_server_volumes(self):
        attachments = self.conn.compute.server_volumes(self.one_server.id)
        self.assertGreaterEqual(len(attachments), 0)

    def test_create_server_volume(self):
        volume_id = "8d015ea7-3c23-4012-8565-236ee67f07f7"
        attachment = self.conn.compute.create_server_volume(
            self.one_server.id, volume_id
        )
        self.assertEqual(attachment.volumeId, volume_id)
        self.assertEqual(attachment.serverId, self.one_server.id)

    def test_delete_server_volume(self):
        attachments = self.conn.compute.server_volumes(self.one_server.id)
        if len(attachments) <= 0:
            return
        attachment = attachments[0]
        ret = self.conn.compute.delete_server_volume(
            attachment.id, self.one_server.id)
        self.assertIsNone(ret)
