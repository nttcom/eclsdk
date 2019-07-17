# -*- coding: utf-8 -*-

from ecl.tests.functional import base


class TestIntenetService(base.BaseFunctionalTest):

    @classmethod
    def setUpClass(cls):
        super(TestIntenetService, cls).setUpClass()
        cls.one_inet_service = None
        inet_services = cls.conn.network.internet_services()
        if inet_services and len(inet_services) > 0:
            cls.one_inet_service = inet_services[0]

    def test_get(self):
        sot = self.conn.network.get_internet_service(self.one_inet_service.id)
        self.assertEqual(self.one_inet_service.id, sot.id)

    def test_find_by_id(self):
        sot = self.conn.network.find_internet_service(self.one_inet_service.id)
        self.assertEqual(self.one_inet_service.id, sot.id)

    def test_find_by_name(self):
        sot = self.conn.network.find_internet_service(self.one_inet_service.name)
        self.assertEqual(self.one_inet_service.id, sot.id)


class TestInternetGateway(base.BaseFunctionalTest):

    @classmethod
    def prepare_create(cls):
        inet_services = cls.conn.network.internet_services()
        if inet_services and len(inet_services) > 0:
            cls.one_inet_service = inet_services[0]
        qos_options = cls.conn.network.qos_options()
        for qos in qos_options:
            if qos.service_type == "internet" and qos.name.startswith("10Mbps"):
                cls.one_qos_option = qos
                break

    @classmethod
    def setUpClass(cls):
        super(TestInternetGateway, cls).setUpClass()
        cls.gw_name = "Test-sdk-inet-gw"
        cls.one_inet_gw = None
        cls.one_qos_option = None
        cls.one_inet_service = None

        inet_gws = cls.conn.network.internet_gateways()
        for inet_gw in inet_gws:
            if inet_gw.name == cls.gw_name:
                cls.one_inet_gw = inet_gw
                break
        if cls.one_inet_gw is None:
            cls.prepare_create()
            cls.one_inet_gw = cls.conn.network.create_internet_gateway(
                internet_service_id=cls.one_inet_service.id,
                qos_option_id=cls.one_qos_option.id,
                name=cls.gw_name,
            )
            cls.one_inet_gw .wait_for_gateway()

    def test_get(self):
        if self.one_inet_gw is not None:
            sot = self.conn.network.get_internet_gateway(self.one_inet_gw.id)
            self.assertEqual(self.one_inet_gw.id, sot.id)

    def _test_create(self):
        if self.one_inet_service is None:
            self.prepare_create()
        sot = self.conn.network.create_internet_gateway(
            internet_service_id=self.one_inet_service.id,
            qos_option_id=self.one_qos_option.id,
            name=self.gw_name,
        )
        sot.wait_for_gateway()
        if self.one_inet_gw is None:
            self.one_inet_gw = sot

    def test_update(self):
        sot = self.conn.network.update_internet_gateway(self.one_inet_gw.id,
                                                        description="(edited)")
        print(sot)

    def _test_delete(self):
        sot = self.conn.network.delete_internet_gateway(self.one_inet_gw.id)
        self.assertIsNone(sot)
