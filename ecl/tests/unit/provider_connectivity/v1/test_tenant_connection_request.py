# -*- coding: utf-8 -*-

import testtools

from ecl.provider_connectivity.v1 import tenant_connection_request


IDENTIFIER = 'IDENTIFIER'
BASIC_EXAMPLE = {
    'id': IDENTIFIER,
    'tenant_connection_request_id': IDENTIFIER,
    'name': 'name',
    'description': 'description',
    'tags': {'key1': 'value2'},
    'tenant_id': 'tenant_id',
    'name_other': 'name_other',
    'description_other': 'description_other',
    'tags_other': 'tags_other',
    'tenant_id_other': 'tenant_id_other',
    'network_id': 'network_id',
    'keystone_user_id': 'keystone_user_id',
    'apporoval_request_id': 'apporoval_request_id',
    'status': 'status'
}


class TestTenantConnection(testtools.TestCase):
    def test_basic(self):
        sot = tenant_connection_request.TenantConnectionRequest()
        self.assertEqual('tenant_connection_requests', sot.resources_key)
        self.assertEqual('tenant_connection_request', sot.resource_key)
        self.assertEqual('/v2.0/tenant_connection_requests', sot.base_path)
        self.assertEqual('provider-connectivity', sot.service.service_type)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_update)

    def test_make_basic(self):
        sot = tenant_connection_request.TenantConnectionRequest(**BASIC_EXAMPLE)
        self.assertEqual(BASIC_EXAMPLE['id'], sot.id)
        self.assertEqual(BASIC_EXAMPLE['tenant_connection_request_id'], sot.tenant_connection_request_id)
        self.assertEqual(BASIC_EXAMPLE['name'], sot.name)
        self.assertEqual(BASIC_EXAMPLE['description'], sot.description)
        self.assertEqual(BASIC_EXAMPLE['tags'], sot.tags)
        self.assertEqual(BASIC_EXAMPLE['name_other'], sot.name_other)
        self.assertEqual(BASIC_EXAMPLE['description_other'], sot.description_other)
        self.assertEqual(BASIC_EXAMPLE['tags_other'], sot.tags_other)
        self.assertEqual(BASIC_EXAMPLE['tenant_id'], sot.tenant_id)
        self.assertEqual(BASIC_EXAMPLE['tenant_id_other'], sot.tenant_id_other)
        self.assertEqual(BASIC_EXAMPLE['network_id'], sot.network_id)
        self.assertEqual(BASIC_EXAMPLE['keystone_user_id'], sot.keystone_user_id)
        self.assertEqual(BASIC_EXAMPLE['apporoval_request_id'], sot.apporoval_request_id)
        self.assertEqual(BASIC_EXAMPLE['status'], sot.status)
