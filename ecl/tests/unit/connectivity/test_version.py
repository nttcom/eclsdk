# -*- coding: utf-8 -*-

import testtools

from ecl.connectivity import version

IDENTIFIER = 'IDENTIFIER'
EXAMPLE = {
    'id': IDENTIFIER,
    'links': '2',
    'status': '3',
    'updated': '4',
}


class TestVersion(testtools.TestCase):

    def test_basic(self):
        sot = version.Version()
        self.assertEqual('version', sot.resource_key)
        self.assertEqual('versions', sot.resources_key)
        self.assertEqual('/', sot.base_path)
        self.assertEqual('interconnectivity', sot.service.service_type)
        self.assertFalse(sot.allow_create)
        self.assertFalse(sot.allow_retrieve)
        self.assertFalse(sot.allow_update)
        self.assertFalse(sot.allow_delete)
        self.assertTrue(sot.allow_list)

    def test_make_it(self):
        sot = version.Version(EXAMPLE)
        self.assertEqual(EXAMPLE['id'], sot.id)
        self.assertEqual(EXAMPLE['links'], sot.links)
        self.assertEqual(EXAMPLE['status'], sot.status)
        self.assertEqual(EXAMPLE['updated'], sot.updated)
