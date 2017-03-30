# -*- coding: utf-8 -*-

from ecl.network.v2.static_route import StaticRoute
from ecl.tests.functional import base


class TestStaticRoute(base.BaseFunctionalTest):

    @classmethod
    def prepare_create(cls):
        for inet in cls.conn.network.internet_gateways():
            if inet.name == "Test-sdk-inet-gw":
                cls.one_inet_gw = inet
                break

        for pip in cls.conn.network.publicips():
            cls.one_pip = pip
            break

        for gwif in cls.conn.network.gateway_interfaces():
            if gwif.name == "Test-sdk-gwi":
                cls.one_gwif = gwif

    @classmethod
    def setUpClass(cls):
        super(TestStaticRoute, cls).setUpClass()
        cls.one_sr = None
        cls.one_sr_name = None
        cls.one_inet_gw = None
        cls.one_pip = None
        cls.one_gwif = None
        srs = cls.conn.network.static_routes()
        for sr in srs:
            if sr.name == cls.one_sr_name:
                cls.one_sr = sr
                break
        if cls.one_sr is None:
            cls.prepare_create()
            cls.one_sr = cls.conn.network.create_static_route(
                "internet",
                cls.one_pip.cidr, "192.168.1.115",
                name=cls.one_sr_name,
                internet_gw_id=cls.one_inet_gw.id,
            )
            cls.one_sr.wait_for_create(cls.conn.network.session)

    def test_get(self):
        if self.one_sr:
            sot = self.conn.network.get_static_route(self.one_sr.id)
            self.assertEqual(self.one_sr.id, sot.id)

    def test_update(self):
        if self.one_sr:
            sot = self.conn.network.update_static_route(self.one_sr.id,
                                                        description="Test SDK")
            self.assertIsInstance(sot, StaticRoute)

    def test_delete(self):
        if self.one_sr:
            sot = self.conn.network.delete_static_route(self.one_sr.id)
            self.assertIsInstance(sot, StaticRoute)
