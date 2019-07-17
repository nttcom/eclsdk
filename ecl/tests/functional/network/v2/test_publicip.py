# -*- coding: utf-8 -*-

from ecl.tests.functional import base
from ecl.network.v2.publicip import PublicIP


class TestPublic(base.BaseFunctionalTest):
    @classmethod
    def retrieve_gw(cls):
        cls.gw_name = "Test-sdk-inet-gw"
        inet_gws = cls.conn.network.internet_gateways()
        for inet_gw in inet_gws:
            if inet_gw.name == cls.gw_name:
                cls.one_inet_gw = inet_gw
                break

    @classmethod
    def setUpClass(cls):
        super(TestPublic, cls).setUpClass()
        cls.one_publicip = None
        cls.pip_name = "Test-sdk-publicip"
        cls.one_inet_gw = None
        cls.retrieve_gw()
        publicips = cls.conn.network.publicips()
        for publicip in publicips:
            if publicip.internet_gw_id == cls.one_inet_gw.id:
                cls.one_publicip = publicip
                break
        if not cls.one_publicip:
            cls.one_publicip = cls.conn.network.create_publicip(
                cls.one_inet_gw.id, 28, name=cls.pip_name)
            cls.one_publicip.wait_for_publicip(cls.conn.network.session)

    def _test_get(self):
        sot = self.conn.network.get_publicip(self.one_publicip.id)
        self.assertEqual(self.one_publicip.id, sot.id)

    def _test_delete(self):
        sot = self.conn.network.delete_publicip(self.one_publicip.id)
        self.assertIsInstance(sot, PublicIP)

    def test_update(self):
        if self.one_publicip:
            sot = self.conn.network.update_public_ip(self.one_publicip.id,
                                                     description="Test SDK")
            self.assertIsInstance(sot, PublicIP)
