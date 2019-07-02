# -*- coding: utf-8 -*-


import six

from ecl.tests.functional import base


class TestMEIC(base.BaseFunctionalTest):

    @classmethod
    def setUpClass(cls):
        super(TestMEIC, cls).setUpClass()
        meics = list(cls.conn.connectivity.meics())
        cls.one_meic = None
        if meics and len(meics) > 0:
            cls.one_meic = meics[0]

    def test_meics(self):
        meics = list(self.conn.connectivity.meics())
        self.assertGreaterEqual(len(meics), 0)

        for meic in meics:
            # print meic.to_dict()["service_type"]
            self.assertIsInstance(meic.mcic_id, six.string_types)
            self.assertIsInstance(meic.mcic_name, six.string_types)
            self.assertIsInstance(meic.mcic_status, six.string_types)
            self.assertIsInstance(meic.tenant_id, six.string_types)
            self.assertIsInstance(meic.tenant_name, six.string_types)
            self.assertEqual(meic.service_type, "NGC-EC")
            if meic.ngc:
                self.assertIsInstance(meic.ngc, dict)
            if meic.ec:
                self.assertIsInstance(meic.ec, dict)
            self.assertIsInstance(meic.timezone, six.string_types)

    def test_get_meic_by_id(self):
        meic = self.conn.connectivity.get_meic(self.one_meic.mcic_id)
        self.assertEqual(meic.mcic_id, self.one_meic.mcic_id)
        self.assertEqual(meic.mcic_name, self.one_meic.mcic_name)
        self.assertEqual(meic.mcic_status, self.one_meic.mcic_status)
        self.assertEqual(meic.tenant_id, self.one_meic.tenant_id)
        self.assertEqual(meic.tenant_name, self.one_meic.tenant_name)
        self.assertEqual(meic.service_id, self.one_meic.service_id)
        self.assertEqual(meic.service_type, self.one_meic.service_type)
        self.assertEqual(meic.ngc, self.one_meic.ngc)
        self.assertEqual(meic.ec, self.one_meic.ec)
        self.assertEqual(meic.timezone, self.one_meic.timezone)
