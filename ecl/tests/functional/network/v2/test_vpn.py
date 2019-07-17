# -*- coding: utf-8 -*-

from ecl.tests.functional import base


class TestVPNService(base.BaseFunctionalTest):

    @classmethod
    def setUpClass(cls):
        super(TestVPNService, cls).setUpClass()
        cls.one_vpn_service = None
        vpn_services = cls.conn.network.vpn_services()
        if vpn_services and len(vpn_services) > 0:
            cls.one_vpn_service = vpn_services[0]

    def test_get(self):
        sot = self.conn.network.get_vpn_service(self.one_vpn_service.id)
        self.assertEqual(self.one_vpn_service.id, sot.id)


class TestVPNGateway(base.BaseFunctionalTest):

    @classmethod
    def setUpClass(cls):
        super(TestVPNGateway, cls).setUpClass()
        cls.one_vpn_gateway = None
        vpn_gws = cls.conn.network.vpn_gateways()
        if vpn_gws and len(vpn_gws) > 0:
            cls.one_vpn_gateway = vpn_gws[0]

    def test_get(self):
        sot = self.conn.network.get_vpn_gateway(self.one_vpn_gateway.id)
        self.assertEqual(self.one_vpn_gateway.id, sot.id)

    def find_get_by_id(self):
        sot = self.conn.network.find_vpn_gateway(self.one_vpn_gateway.id)
        self.assertEqual(self.one_vpn_gateway.id, sot.id)


class TestVPNInterface(base.BaseFunctionalTest):

    @classmethod
    def setUpClass(cls):
        super(TestVPNInterface, cls).setUpClass()
        cls.one_vpn_interface = None
        vpn_ifs = cls.conn.network.vpn_interfaces()
        if vpn_ifs and len(vpn_ifs) > 0:
            cls.one_vpn_interface = vpn_ifs[0]

    def test_get(self):
        sot = self.conn.network.get_vpn_interface(self.one_vpn_interface.id)
        self.assertEqual(self.one_vpn_interface.id, sot.id)
