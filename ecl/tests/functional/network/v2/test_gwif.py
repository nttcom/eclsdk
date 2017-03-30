# -*- coding: utf-8 -*-

from ecl.tests.functional import base
from ecl.network.v2.gw_interface import GatewayInterface


class TestGWIF(base.BaseFunctionalTest):

    @classmethod
    def setUpClass(cls):
        super(TestGWIF, cls).setUpClass()
        cls.one_gwif = None
        cls.one_nw = None
        cls.one_inet_gw = None
        cls.gw_name = "Test-sdk-inet-gw"
        cls.gwif_name = "Test-sdk-gwi"
        cls.nw_name = "nttcom01"
        cls.retrieve_gw()

        gwifs = cls.conn.network.gateway_interfaces()
        for gwi in gwifs:
            if gwi.name == cls.gwif_name:
                cls.one_gwif = gwi
                break
        if cls.one_gwif is None:
            cls.one_gwif = cls.conn.network.create_gateway_interface(
                "internet", cls.one_nw.id, 24,
                "192.168.1.112", "192.168.1.113", "192.168.1.114",
                1, name=cls.gwif_name, internet_gw_id = cls.one_inet_gw.id
            )
            cls.one_gwif.wait_for_create(cls.conn.network.session)

    @classmethod
    def retrieve_gw(cls):
        inet_gws = cls.conn.network.internet_gateways()
        for inet_gw in inet_gws:
            if inet_gw.name == cls.gw_name:
                cls.one_inet_gw = inet_gw
                break

        networks = cls.conn.network.networks()
        for nw in networks:
            if nw.name == cls.nw_name:
                cls.one_nw = nw
                break

    def _test_get(self):
        if self.one_gwif:
            sot = self.conn.network.get_gateway_interface(self.one_gwif.id)
            self.assertEqual(self.one_gwif.id, sot.id)

    def test_update(self):
        if self.one_gwif:
            sot = self.conn.network.update_gateway_interface(self.one_gwif.id,
                                                             description="Test SDK")
            self.assertIsInstance(sot, GatewayInterface)

    def _test_delete(self):
        sot = self.conn.network.delete_gateway_interface(self.one_gwif.id)
        self.assertIsInstance(sot, GatewayInterface)
