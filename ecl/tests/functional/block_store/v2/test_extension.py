# -*- coding: utf-8 -*-

import six

from ecl.tests.functional import base


class TestExtension(base.BaseFunctionalTest):

    def test_list(self):
        sots = self.conn.block_store.extensions()
        self.assertGreaterEqual(len(sots), 0)
