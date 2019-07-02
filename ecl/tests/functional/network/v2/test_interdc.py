# -*- coding: utf-8 -*-

from ecl.tests.functional import base
from ecl.network.v2 import interdc as _interdc


class TestInterDCService(base.BaseFunctionalTest):

    @classmethod
    def setUpClass(cls):
        super(TestInterDCService, cls).setUpClass()
        cls.one_idc_service = None
        idc_services = cls.conn.network.interdc_services()
        if idc_services and len(idc_services) > 0:
            cls.one_idc_service = idc_services[0]

    def test_get(self):
        sot = self.conn.network.get_interdc_service(self.one_idc_service.id)
        self.assertEqual(self.one_idc_service.id, sot.id)


class TestInterDCGateway(base.BaseFunctionalTest):

    @classmethod
    def setUpClass(cls):
        super(TestInterDCGateway, cls).setUpClass()
        cls.one_idc_gateway = None
        idc_gws = cls.conn.network.interdc_gateways()
        if idc_gws and len(idc_gws) > 0:
            cls.one_idc_gateway = idc_gws[0]

    def test_get(self):
        sot = self.conn.network.get_interdc_gateway(self.one_idc_gateway.id)
        self.assertEqual(self.one_idc_gateway.id, sot.id)

    def test_find_by_id(self):
        sot = set.conn.network.find_interdc_gateway(
            self.one_idc_gateway.id
        )
        self.assertEqual(self.one_idc_gateway.id, sot.id)


class TestInterDCInterface(base.BaseFunctionalTest):

    @classmethod
    def prepare_create(cls):
        interdc_gws = cls.conn.network.interdc_gateways()
        if interdc_gws and len(interdc_gws) > 0:
            cls.one_idc_gateway = interdc_gws[0]
        network = cls.conn.network.networks()
        for nw in network:
            if nw.name == "test-network":
                cls.one_network = nw
                break

    @classmethod
    def setUpClass(cls):
        super(TestInterDCInterface, cls).setUpClass()
        cls.one_idc_interface = None
        cls.one_idc_gateway = None
        cls.one_idc_gateway_name = "N000001996_V15000001"
        cls.one_idc_interface_name = "interdc_interface_for_tenant-sdpgui01"
        cls.one_network = None

        idc_ifs = cls.conn.network.interdc_interfaces()
        for idcif in idc_ifs:
            if idcif.name == cls.one_idc_interface_name:
                cls.one_idc_interface = idcif
        if cls.one_idc_interface is None:
            cls.prepare_create()
            cls.one_idc_interface = cls.conn.network.create_interdc_interface(
                cls.one_idc_gateway.id,
                "xxx", "xxx", "xxx", "xxx", 1,
                name=cls.one_idc_interface_name, )

    def test_get(self):
        sot = self.conn.network.get_interdc_interface(self.one_idc_interface.id)
        self.assertEqual(self.one_idc_interface.id, sot.id)

    def test_create(self):
        if self.one_idc_gateway is None or self.one_network is None:
            self.prepare_create()
        self.one_idc_interface = self.conn.network.create_interdc_interface(
            self.one_idc_gateway.id,
            "xxx", "xxx", "xxx", "xxx", 1,
            name=self.one_idc_interface_name, )
        self.assertIsInstance(self.one_idc_interface, _interdc.InterDCInterface)

    def test_update(self):
        sot = self.conn.network.update_interdc_interface(self.one_idc_interface.id,
                                                         description="xxx")
        self.assertIsInstance(sot, _interdc.InterDCInterface)

    def test_delete(self):
        sot = self.conn.network.delete_interdc_interface(self.one_idc_interface.id)
        # self.assertIsInstance(sot, _interdc.InterDCInterface)
