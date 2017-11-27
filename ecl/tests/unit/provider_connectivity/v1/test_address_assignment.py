# -*- coding: utf-8 -*-

import testtools

from ecl.provider_connectivity.v1 import address_assignment


IDENTIFIER = 'IDENTIFIER'
REQUEST_ID = 'REQUEST_ID'
BASIC_EXAMPLE = {
    'tenant_connection_id': IDENTIFIER,
    'tenant_connection_request_id': REQUEST_ID,
    'network_id': 'network_id',
    'mac_address': 'mac_address'
}


class TestTenantConnection(testtools.TestCase):
    def test_basic(self):
        sot = address_assignment.AddressAssignment(REQUEST_ID)
        self.assertEqual('address_assignments', sot.resources_key)
        self.assertEqual('address_assignment', sot.resource_key)
        self.assertEqual('/v2.0/tenant_connection_requests/'
                         '%(tenant_connection_request_id)s/address_assignment', sot.base_path)
        self.assertEqual('provider-connectivity', sot.service.service_type)
        self.assertTrue(sot.allow_list)
        self.assertFalse(sot.allow_create)
        self.assertFalse(sot.allow_get)
        self.assertFalse(sot.allow_delete)
        self.assertFalse(sot.allow_update)

    def test_make_basic(self):
        sot = address_assignment.AddressAssignment(**BASIC_EXAMPLE)
        self.assertEqual(BASIC_EXAMPLE['tenant_connection_id'], sot.tenant_connection_id)
        self.assertEqual(BASIC_EXAMPLE['tenant_connection_request_id'], sot.tenant_connection_request_id)
        self.assertEqual(BASIC_EXAMPLE['network_id'], sot.network_id)
        self.assertEqual(BASIC_EXAMPLE['mac_address'], sot.mac_address)
