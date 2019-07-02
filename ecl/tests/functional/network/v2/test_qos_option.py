# -*- coding: utf-8 -*-

from ecl.tests.functional import base


class TestQosOption(base.BaseFunctionalTest):

    @classmethod
    def setUpClass(cls):
        super(TestQosOption, cls).setUpClass()
        cls.one_qos_option = None
        qoptions = cls.conn.network.qos_options()
        if qoptions and len(qoptions) > 0:
            cls.one_qos_option = qoptions[0]

    def test_get(self):
        sot = self.conn.network.get_qos_option(self.one_qos_option.id)
        self.assertEqual(self.one_qos_option.id, sot.id)

    def test_find_by_id(self):
        sot = self.conn.network.find_qos_option(self.one_qos_option.id)
        self.assertEqual(self.one_qos_option.id, sot.id)
