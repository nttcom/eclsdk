# -*- coding: utf-8 -*-

from ecl.tests.functional import base


class TestPort(base.BaseFunctionalTest):

    @classmethod
    def setUpClass(cls):
        super(TestPort, cls).setUpClass()
        cls.one_network = None
        sot = cls.conn.network.networks()
        if sot is not None and len(sot) > 0:
            cls.one_network = sot[0]
        cls.one_port = None
        ports = list(cls.conn.network.ports())
        for port in ports:
            if not port.managed_by_service and \
                    port.device_owner.startswith("compute"):
                cls.one_port = port
                break

    def test_find(self):
        sot = self.conn.network.find_port(self.one_port.id)
        self.assertEqual(self.one_port.id, sot.id)

    def test_get(self):
        sot = self.conn.network.get_port(self.one_port.id)
        self.assertEqual(self.one_port.id, sot.id)
        self.assertEqual(self.one_port.name, sot.name)
        self.assertEqual(self.one_port.network_id, sot.network_id)
        self.assertEqual(self.one_port.admin_state_up, sot.admin_state_up)

    def test_list(self):
        ids = [o.id for o in self.conn.network.ports()]
        self.assertIn(self.one_port.id, ids)

    def test_update(self):
        test_name = "test_port_name"
        test_description = "test_port_description"
        sot = self.conn.network.update_port(self.one_port.id,
                                            name=test_name,
                                            description=test_description)
        self.assertEqual(test_name, sot.name)
        self.assertEqual(test_description, sot.description)

    def test_create(self):
        test_name = "test_port"
        self.conn.network.create_port(name=test_name)

    def test_delete(self):
        self.conn.network.delete_port(self.one_port.id)
