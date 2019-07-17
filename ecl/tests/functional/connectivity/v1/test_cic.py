# -*- coding: utf-8 -*-


import six

from ecl.tests.functional import base


class TestCIC(base.BaseFunctionalTest):

    @classmethod
    def setUpClass(cls):
        super(TestCIC, cls).setUpClass()
        mcics = list(cls.conn.connectivity.mcics())
        cls.one_mcic = None
        cls.one_cic = None
        if mcics and len(mcics) > 0:
            cls.one_mcic = mcics[0]
        if cls.one_mcic is None:
            return

        cics = list(cls.conn.connectivity.cics(cls.one_mcic.mcic_id))
        if cics and len(cics) > 0:
            cls.one_cic = cics[0]

    def test_cics(self):
        cics = list(self.conn.connectivity.cics(self.one_mcic.mcic_id))
        self.assertGreaterEqual(len(cics), 0)

        for cic in cics:
            self.assertIsInstance(cic.cic_id, six.string_types)
            if cic.cic_name is not None:
                self.assertIsInstance(cic.cic_name, six.string_types)
            if cic.cic_status is not None:
                self.assertIsInstance(cic.cic_status, six.string_types)
            if cic.network_id is not None:
                self.assertIsInstance(cic.network_id, six.string_types)
            if cic.network_name is not None:
                self.assertIsInstance(cic.network_name, six.string_types)
            if cic.destination_vlan is not None:
                self.assertIsInstance(cic.destination_vlan, int)
            if cic.bandwidth is not None:
                self.assertIsInstance(cic.bandwidth, int)

    def test_get_cic_by_id(self):
        cic = self.conn.connectivity.get_cic(self.one_mcic.mcic_id,
                                             self.one_cic.cic_id)
        self.assertEqual(cic.cic_id, self.one_cic.cic_id)
        self.assertEqual(cic.cic_name, self.one_cic.cic_name)
        self.assertEqual(cic.cic_status, self.one_cic.cic_status)
        self.assertEqual(cic.network_id, self.one_cic.network_id)
        self.assertEqual(cic.network_name, self.one_cic.network_name)
        self.assertEqual(cic.destination_vlan, self.one_cic.destination_vlan)
        self.assertEqual(cic.bandwidth, self.one_cic.bandwidth)

    def test_create_cic(self):
        cic_name = self.one_mcic.mcic_name + "-xxx"
        network_id = self.one_cic.network_id
        colo_vlan = 4
        cic = self.conn.connectivity.create_cic(self.one_mcic.mcic_id,
                                                cic_name,
                                                network_id,
                                                colo_vlan)
        self.assertIsInstance(cic.cic_id, six.string_types)

    def test_delete_cic(self):
        cic_id = self.one_cic.cic_id
        mcic_id = self.one_mcic.mcic_id
        cic = self.conn.connectivity.delete_cic(mcic_id, cic_id)
        # print cic.to_dict()
        self.assertEqual(cic_id, cic.id)

    def test_update_cic(self):
        cic_id = self.one_cic.cic_id
        mcic_id = self.one_mcic.mcic_id
        cic = self.conn.connectivity.update_cic(mcic_id, cic_id, "xxx")
        # print cic.to_dict()
        self.assertEqual(cic_id, cic.id)
