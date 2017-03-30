# -*- coding: utf-8 -*-

import testtools

from ecl.connectivity.v1.mcic import MCIC

IDENTIFIER = 'IDENTIFIER'
BASIC_EXAMPLE = {
    'mcic_id': IDENTIFIER,
    'mcic_name': 'xxx-name',
    'mcic_status': 'xxx-status',
    'tenant_id': 'xxx-tenant-id',
    'tenant_name': 'xxx-tenant-name',
    'service_type': 'xxx-service-type',
    'ngc': None,
    'colo': {},
    'timezone': 'UTC'
}


class TestMCIC(testtools.TestCase):

    def test_basic(self):
        sot = MCIC()
        self.assertEqual(None, sot.resource_key)
        self.assertEqual(None, sot.resources_key)
        self.assertEqual('/mCICs', sot.base_path)
        self.assertEqual('interconnectivity', sot.service.service_type)
        self.assertFalse(sot.allow_create)
        self.assertTrue(sot.allow_get)
        self.assertFalse(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertFalse(sot.allow_update)

        self.assertDictEqual({"sort_key": "sort_key",
                              "sort_dir": "sort_dir"
                              },
                             sot._query_mapping._mapping)

    def test_make_basic(self):
        sot = MCIC(**BASIC_EXAMPLE)
        self.assertEqual(BASIC_EXAMPLE['mcic_id'], sot.mcic_id)
        self.assertEqual(BASIC_EXAMPLE['mcic_name'], sot.mcic_name)
        self.assertEqual(BASIC_EXAMPLE['mcic_status'], sot.mcic_status)
        self.assertEqual(BASIC_EXAMPLE['tenant_id'], sot.tenant_id)
        self.assertEqual(BASIC_EXAMPLE['tenant_name'], sot.tenant_name)
        self.assertEqual(BASIC_EXAMPLE['service_type'], sot.service_type)
        self.assertEqual(BASIC_EXAMPLE['ngc'], sot.ngc)
        self.assertEqual(BASIC_EXAMPLE['colo'], sot.colo)
        self.assertEqual(BASIC_EXAMPLE['timezone'], sot.timezone)
