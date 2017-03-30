# -*- coding: utf-8 -*-

import six

from ecl.tests.functional import base


class TestExtension(base.BaseFunctionalTest):

    def test_list(self):
        extensions = self.conn.network.extensions()
        self.assertGreaterEqual(len(extensions), 0)

        for ext in extensions:
            self.assertIsInstance(ext.name, six.string_types)
            self.assertIsInstance(ext.alias, six.string_types)

    def test_find(self):
        extension = self.conn.network.find_extension('external-net')
        self.assertEqual('Neutron external network', extension.name)
