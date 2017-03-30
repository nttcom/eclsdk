# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import testtools

from ecl.storage.v1 import storage as s

IDENTIFIER = 'IDENTIFIER'
BASIC_EXAMPLE = {
    'id': IDENTIFIER,
    'network_id': '2',
    'subnet_id': '3',
    'ip_addr_pool': {
        'start': '192.168.0.128',
        'end': '192.168.0.255'
    },
    'host_routes': [{
        'destination': '0.0.0.0/0',
        'nexthop': '123.456.78.9'
    },],
    'volume_type_id': '6685584b-1eac-4da6-b5c3-555430cf68ff',
    'name': 'vs01',
    'description': 'Virtual Storage for NW1',
    'status': 'creating',
    'created_at': 'null',
    'updated_at': 'null',
    'error_message': '',
}


class TestStorage(testtools.TestCase):

    def test_basic(self):
        sot = s.Storage()
        self.assertEqual('virtual_storage', sot.resource_key)
        self.assertEqual('virtual_storages', sot.resources_key)
        self.assertEqual('/virtual_storages', sot.base_path)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertEqual('storage', sot.service.service_type)

    def test_basic_detail(self):
        sot = s.StorageDetail()
        self.assertEqual('virtual_storage', sot.resource_key)
        self.assertEqual('virtual_storages', sot.resources_key)
        self.assertEqual('/virtual_storages/detail', sot.base_path)
        self.assertTrue(sot.allow_list)
        self.assertFalse(sot.allow_get)
        self.assertFalse(sot.allow_create)
        self.assertFalse(sot.allow_update)
        self.assertFalse(sot.allow_delete)
        self.assertEqual('storage', sot.service.service_type)

    def test_make_basic(self):
        sot = s.Storage(**BASIC_EXAMPLE)
        self.assertEqual(BASIC_EXAMPLE['id'], sot.id)
        self.assertEqual(BASIC_EXAMPLE['network_id'], sot.network_id)
        self.assertEqual(BASIC_EXAMPLE['subnet_id'], sot.subnet_id)
        self.assertEqual(BASIC_EXAMPLE['ip_addr_pool'], sot.ip_addr_pool)
        self.assertEqual(BASIC_EXAMPLE['host_routes'], sot.host_routes)
        self.assertEqual(BASIC_EXAMPLE['volume_type_id'], sot.volume_type_id)
        self.assertEqual(BASIC_EXAMPLE['name'], sot.name)
        self.assertEqual(BASIC_EXAMPLE['description'], sot.description)
        self.assertEqual(BASIC_EXAMPLE['status'], sot.status)
        self.assertEqual(BASIC_EXAMPLE['created_at'], sot.created_at)
        self.assertEqual(BASIC_EXAMPLE['updated_at'], sot.updated_at)
        self.assertEqual(BASIC_EXAMPLE['error_message'], sot.error_message)
