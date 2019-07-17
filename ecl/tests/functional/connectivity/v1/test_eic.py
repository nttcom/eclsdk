# -*- coding: utf-8 -*-


import six

from ecl.tests.functional import base


class TestEIC(base.BaseFunctionalTest):

    @classmethod
    def setUpClass(cls):
        super(TestEIC, cls).setUpClass()
        meics = list(cls.conn.connectivity.meics())
        cls.one_meic = None
        cls.one_eic = None
        if meics and len(meics) > 0:
            cls.one_meic = meics[0]
        if cls.one_meic is None:
            return

        eics = list(cls.conn.connectivity.eics(cls.one_meic.mcic_id))
        if eics and len(eics) > 0:
            cls.one_eic = eics[0]

    def test_eics(self):
        eics = list(self.conn.connectivity.eics(self.one_meic.mcic_id))
        self.assertGreaterEqual(len(eics), 0)
        for eic in eics:
            # print eic.to_dict()
            self.assertIsInstance(eic.cic_id, six.string_types)
            if eic.cic_name is not None:
                self.assertIsInstance(eic.cic_name, six.string_types)
            if eic.cic_status is not None:
                self.assertIsInstance(eic.cic_status, six.string_types)
            if eic.network_id is not None:
                self.assertIsInstance(eic.network_id, six.string_types)
            if eic.network_name is not None:
                self.assertIsInstance(eic.network_name, six.string_types)
            if eic.server_segment_name is not None:
                self.assertIsInstance(eic.server_segment_name, six.string_types)
            if eic.server_segment_nbr is not None:
                self.assertIsInstance(eic.server_segment_nbr, int)
            if eic.bandwidth is not None:
                self.assertIsInstance(eic.bandwidth, int)

    def test_get_eic_by_id(self):
        eic = self.conn.connectivity.get_eic(self.one_meic.mcic_id,
                                             self.one_eic.cic_id)
        self.assertEqual(eic.cic_id, self.one_eic.cic_id)
        self.assertEqual(eic.cic_name, self.one_eic.cic_name)
        self.assertEqual(eic.cic_status, self.one_eic.cic_status)
        self.assertEqual(eic.network_id, self.one_eic.network_id)
        self.assertEqual(eic.network_name, self.one_eic.network_name)
        self.assertEqual(eic.server_segment_name, self.one_eic.server_segment_name)
        self.assertEqual(eic.server_segment_nbr, self.one_eic.server_segment_nbr)
        self.assertEqual(eic.bandwidth, self.one_eic.bandwidth)

    def test_create_eic(self):
        eic_name = self.one_meic.mcic_name + "-xxx"
        network_id = self.one_eic.network_id
        server_segment_nbr = 4
        eic = self.conn.connectivity.create_eic(self.one_meic.mcic_id,
                                                eic_name,
                                                network_id,
                                                server_segment_nbr)
        self.assertIsInstance(eic.cic_id, six.string_types)

    def test_delete_eic(self):
        eic_id = self.one_eic.cic_id
        meic_id = self.one_meic.mcic_id
        eic = self.conn.connectivity.delete_eic(meic_id, eic_id)
        # print eic.to_dict()
        self.assertEqual(eic_id, eic.id)

    def test_update_eic(self):
        eic_id = self.one_eic.cic_id
        meic_id = self.one_meic.mcic_id
        eic = self.conn.connectivity.update_eic(meic_id, eic_id, "xxx")
        # print eic.to_dict()
        self.assertEqual(eic_id, eic.id)
