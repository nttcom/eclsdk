# -*- coding: utf-8 -*-

from ecl.tests.functional import base
from ecl.block_store.v2.limit import Limit


class TestLimits(base.BaseFunctionalTest):

    def test_show(self):
        sot = self.conn.block_store.limits()
        self.assertIsInstance(sot, Limit)
