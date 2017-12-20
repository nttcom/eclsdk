# -*- coding: utf-8 -*-

import testtools

from ecl.provider_connectivity.v1 import tenant_connection


IDENTIFIER = 'IDENTIFIER'
REQUEST_ID = 'REQUEST_ID'
BASIC_EXAMPLE = {
    'id': IDENTIFIER,
    'tenant_connection_id': IDENTIFIER,
    'tenant_connection_request_id': REQUEST_ID,
    'name': 'name',
    'description': 'description',
    'tags': {'key1': 'value2'},
    'tenant_id': 'tenant_id',
    'name_other': 'name_other',
    'description_other': 'description_other',
    'tags_other': 'tags_other',
    'tenant_id_other': 'tenant_id_other',
    'network_id': 'network_id',
    'device_type': 'device_type',
    'device_id': 'device_id',
    'device_interface_id': 'device_interface_id',
    'attachment_opts': {
      "segmentation_type": "segmentation_type",
      "segmentation_id": "segmentation_id",
      "fixed_ip": []
    },
    'port_id': 'port_id',
    'status': 'status'
}


class TestTenantConnection(testtools.TestCase):
    def test_basic(self):
        sot = tenant_connection.TenantConnection()
        self.assertEqual('tenant_connections', sot.resources_key)
        self.assertEqual('tenant_connection', sot.resource_key)
        self.assertEqual('/v2.0/tenant_connections', sot.base_path)
        self.assertEqual('provider-connectivity', sot.service.service_type)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_update)

    def test_make_basic(self):
        sot = tenant_connection.TenantConnection(**BASIC_EXAMPLE)
        self.assertEqual(BASIC_EXAMPLE['id'], sot.id)
        self.assertEqual(BASIC_EXAMPLE['tenant_connection_id'], sot.tenant_connection_id)
        self.assertEqual(BASIC_EXAMPLE['tenant_connection_request_id'], sot.tenant_connection_request_id)
        self.assertEqual(BASIC_EXAMPLE['name'], sot.name)
        self.assertEqual(BASIC_EXAMPLE['description'], sot.description)
        self.assertEqual(BASIC_EXAMPLE['tags'], sot.tags)
        self.assertEqual(BASIC_EXAMPLE['tenant_id'], sot.tenant_id)
        self.assertEqual(BASIC_EXAMPLE['name_other'], sot.name_other)
        self.assertEqual(BASIC_EXAMPLE['description_other'], sot.description_other)
        self.assertEqual(BASIC_EXAMPLE['tags_other'], sot.tags_other)
        self.assertEqual(BASIC_EXAMPLE['tenant_id_other'], sot.tenant_id_other)
        self.assertEqual(BASIC_EXAMPLE['network_id'], sot.network_id)
        self.assertEqual(BASIC_EXAMPLE['device_type'], sot.device_type)
        self.assertEqual(BASIC_EXAMPLE['device_id'], sot.device_id)
        self.assertEqual(BASIC_EXAMPLE['device_interface_id'], sot.device_interface_id)
        self.assertEqual(BASIC_EXAMPLE['attachment_opts'], sot.attachment_opts)
        self.assertEqual(BASIC_EXAMPLE['port_id'], sot.port_id)
        self.assertEqual(BASIC_EXAMPLE['status'], sot.status)
