# -*- coding: utf-8 -*-

import six
from ecl.tests.functional import base


class TestReservedAddress(base.BaseFunctionalTest):

    @classmethod
    def setUpClass(cls):
        super(TestReservedAddress, cls).setUpClass()
        cls.one_reserved_address = None
        sots = cls.conn.network.reserved_addresses()
        if sots and len(sots) > 0:
            cls.one_reserved_address = sots[0]

    def test_list(self):
        sots = self.conn.network.reserved_addresses()
        for sot in sots:
            self.assertIsInstance(sot.id, six.string_types)
            self.assertIsInstance(sot.subnets, list)
            self.assertIsInstance(sot.tenant_id, six.string_types)

    def test_get(self):
        if not self.one_reserved_address:
            print("0 reserved addresses.")
            return
        sot = self.conn.network.get_reserved_address(self.one_reserved_address.id)
        self.assertEqual(sot.id, self.one_reserved_address.id)
        self.assertEqual(sot.subnets, self.one_reserved_address.subnets)
        self.assertEqual(sot.tenant_id, self.one_reserved_address.tenant_id)
