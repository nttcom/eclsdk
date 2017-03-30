# -*- coding: utf-8 -*-

from ecl.tests.functional import base


class TestSubnet(base.BaseFunctionalTest):

    @classmethod
    def setUpClass(cls):
        super(TestSubnet, cls).setUpClass()
        cls.one_network = None
        networks = cls.conn.network.networks()
        for nw in networks:
            if nw.name == "test-network":
                cls.one_network = nw
                break
        cls.one_subnet = None
        subnets = cls.conn.network.subnets()
        for sn in subnets:
            if sn.name == "test_subnet":
                cls.one_subnet = sn
                break

    def test_find(self):
        sot = self.conn.network.find_subnet(self.one_subnet.name)
        self.assertEqual(self.one_subnet.id, sot.id)

    def test_get(self):
        sot = self.conn.network.get_subnet(self.one_subnet.id)
        self.assertEqual(self.one_subnet.name, sot.name)
        self.assertEqual(self.one_subnet.id, sot.id)
        self.assertEqual(self.one_subnet.dns_nameservers, sot.dns_nameservers)
        self.assertEqual(self.one_subnet.cidr, sot.cidr)
        self.assertEqual(self.one_subnet.allocation_pools, sot.allocation_pools)
        self.assertEqual(self.one_subnet.ip_version, sot.ip_version)
        self.assertEqual(self.one_subnet.host_routes, sot.host_routes)
        self.assertEqual(self.one_subnet.gateway_ip, sot.gateway_ip)
        self.assertEqual(self.one_subnet.enable_dhcp, sot.enable_dhcp)

    def test_list(self):
        names = [o.name for o in self.conn.network.subnets()]
        self.assertIn(self.one_subnet.name, names)

    def test_create(self):
        cidr = "172.16.49.0/24"
        name = "test_subnet"
        sot = self.conn.network.create_subnet(network_id=self.one_network.id,
                                              name=name, cidr=cidr)
        self.assertEqual(sot.cidr, cidr)
        self.assertEqual(sot.name, name)

    def test_update(self):
        test_description = "test subnet update (edited)"
        sot = self.conn.network.update_subnet(self.one_subnet.id,
                                              description=test_description)
        self.assertEqual(test_description, sot.description)

    def test_delete(self):
        name = "test_subnet"
        sot = self.conn.network.find_subnet(name)
        self.conn.network.delete_subnet(sot.id)
