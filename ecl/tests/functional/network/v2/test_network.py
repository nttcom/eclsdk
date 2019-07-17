# -*- coding: utf-8 -*-

from ecl.tests.functional import base


class TestNetwork(base.BaseFunctionalTest):

    @classmethod
    def setUpClass(cls):
        super(TestNetwork, cls).setUpClass()
        cls.one_network = None
        nws = cls.conn.network.networks()
        for nw in nws:
            if nw.name == "test-network":
                cls.one_network = nw
                break

    def test_find(self):
        sot = self.conn.network.find_network(self.one_network.name)
        self.assertEqual(self.one_network.id, sot.id)

    def test_get(self):
        sot = self.conn.network.get_network(self.one_network.id)
        self.assertEqual(self.one_network.id, sot.id)
        self.assertEqual(self.one_network.name, sot.name)
        self.assertEqual(self.one_network.description, sot.description)

    def test_list(self):
        names = [o.name for o in self.conn.network.networks()]
        self.assertIn(self.one_network.name, names)

    def test_create(self):
        test_network = self.conn.network.create_network(
            name="test-network"
        )
        self.assertEqual(test_network.name, "test-network")

    def test_delete(self):
        sot = self.conn.network.find_network("test-network")
        self.conn.network.delete_network(sot.id)

    def test_update(self):
        test_description = "test edit the network(edit)"
        sot = self.conn.network.update_network(
            self.one_network.id,
            description=test_description
        )
        self.assertEqual(test_description, sot.description)
