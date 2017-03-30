# -*- coding: utf-8 -*-

import testtools

from ecl.connectivity.v1.cic import CIC

IDENTIFIER = 'IDENTIFIER'
BASIC_EXAMPLE = {
    'cic_id': IDENTIFIER,
    'cic_name': 'xxx-name',
    'cic_status': 'xxx-status',
    'network_id': 'xxx-network-id',
    'network_name': 'xxx-network-name',
    'destination_vlan': 1,
    'bandwidth': 1
}


class TestMCIC(testtools.TestCase):

    def test_basic(self):
        sot = CIC()
        self.assertEqual(None, sot.resource_key)
        self.assertEqual(None, sot.resources_key)
        self.assertEqual('/mCICs/%(mcic_id)s/CICs', sot.base_path)
        self.assertEqual('interconnectivity', sot.service.service_type)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_update)

        self.assertDictEqual({"sort_key": "sort_key",
                              "sort_dir": "sort_dir"
                              },
                             sot._query_mapping._mapping)

    def test_make_basic(self):
        sot = CIC(**BASIC_EXAMPLE)
        self.assertEqual(BASIC_EXAMPLE['cic_id'], sot.cic_id)
        self.assertEqual(BASIC_EXAMPLE['cic_name'], sot.cic_name)
        self.assertEqual(BASIC_EXAMPLE['cic_status'], sot.cic_status)
        self.assertEqual(BASIC_EXAMPLE['network_id'], sot.network_id)
        self.assertEqual(BASIC_EXAMPLE['network_name'], sot.network_name)
        self.assertEqual(BASIC_EXAMPLE['destination_vlan'], sot.destination_vlan)
        self.assertEqual(BASIC_EXAMPLE['bandwidth'], sot.bandwidth)
