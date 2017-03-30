# -*- coding: utf-8 -*-

import six

from ecl.tests.functional import base


class TestAvailabilityZone(base.BaseFunctionalTest):

    @classmethod
    def setUpClass(cls):
        super(TestAvailabilityZone, cls).setUpClass()

    def test_azs(self):
        azs = self.conn.block_store.availability_zones()
        self.assertGreater(len(azs), 0)

        for az in azs:
            self.assertIsInstance(az.name, six.string_types)
