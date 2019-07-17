# -*- coding: utf-8 -*-


import six

from ecl.tests.functional import base


class TestMCIC(base.BaseFunctionalTest):

    @classmethod
    def setUpClass(cls):
        super(TestMCIC, cls).setUpClass()
        mcics = list(cls.conn.connectivity.mcics())
        cls.one_mcic = None
        if mcics and len(mcics) > 0:
            cls.one_mcic = mcics[0]

    def test_mcics(self):
        mcics = list(self.conn.connectivity.mcics())
        self.assertGreaterEqual(len(mcics), 0)

        for mcic in mcics:
            # print(mcic.to_dict()["service_type"])
            self.assertIsInstance(mcic.mcic_id, six.string_types)
            self.assertIsInstance(mcic.mcic_name, six.string_types)
            self.assertIsInstance(mcic.mcic_status, six.string_types)
            self.assertIsInstance(mcic.tenant_id, six.string_types)
            self.assertIsInstance(mcic.tenant_name, six.string_types)
            self.assertEqual(mcic.service_type, "NGC-colo")
            if mcic.ngc:
                self.assertIsInstance(mcic.ngc, dict)
            if mcic.colo:
                self.assertIsInstance(mcic.colo, dict)
            self.assertIsInstance(mcic.timezone, six.string_types)

    def test_get_mcic_by_id(self):
        mcic = self.conn.connectivity.get_mcic(self.one_mcic.mcic_id)
        self.assertEqual(mcic.mcic_id, self.one_mcic.mcic_id)
        self.assertEqual(mcic.mcic_name, self.one_mcic.mcic_name)
        self.assertEqual(mcic.mcic_status, self.one_mcic.mcic_status)
        self.assertEqual(mcic.tenant_id, self.one_mcic.tenant_id)
        self.assertEqual(mcic.tenant_name, self.one_mcic.tenant_name)
        self.assertEqual(mcic.service_type, self.one_mcic.service_type)
        self.assertEqual(mcic.ngc, self.one_mcic.ngc)
        self.assertEqual(mcic.colo, self.one_mcic.colo)
        self.assertEqual(mcic.timezone, self.one_mcic.timezone)
