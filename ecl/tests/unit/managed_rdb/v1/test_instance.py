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

from ecl.managed_rdb.v1 import instance

IDENTIFIER = 'IDENTIFIER'
INSTANCE_EXAMPLE = {
    'id': IDENTIFIER,
    'tenant_id': 'ec85e0b54e6f4a32ae082b06da06d9df',
    'name': 'MyInstance',
    'description': 'This is my instance',
    'flavor': {
        'id': '4CPU-32GB',
        'name': '4CPU-32GB',
        'core': 4,
        'memory': 32,
    },
    'database_version': {
        'id': 'POSTGRES_13_2',
        'name': 'POSTGRES_13_2',
        'dbms_name': 'POSTGRES',
        'major_version': 13,
    },
    'storage_type': {
        'name': '4IOPS-500GB',
        'type': 'piops_iscsi_na',
        'iops': 4,
        'size': 50,
    },
    'high_availability': True,
    'status': 'NEW',
    'task_type': 'CREATE',
    'task_state': 'NONE',
    'monitoring_state': 'AVAILABLE',
    'nodes': [{
        'availability_zone': 'groupa',
        'role': 'PRIMARY',
    }, {
        'availability_zone': 'groupb',
        'role': 'STANDBY',
    }],
    'network': {
        'id': 'mrdb-nw',
        'ip_address': '192.168.10.10',
        'reserved_ip_addresses': ['192.168.10.11', '192.168.10.12'],
    },
    'metadata': {
        'data-type': 'PRODUCT',
        'data-name': 'Apache Server',
    },
    'links': [{
        'rel': 'self',
        'href': 'http://localhost:8080/self',
    }, {
        'rel': 'bookmark',
        'href': 'http://localhost:8080/20220317173304',
    }],
    'created': '2019-08-24T14:15:22Z',
    'admin_password': 'pass#123',
}

INSTANCE_ACTION_EXAMPLE = {
    'admin_password': 'pass#123',
}


class TestInstance(testtools.TestCase):

    def test_basic(self):
        sot = instance.Instance()
        self.assertEqual('instances', sot.resources_key)
        self.assertEqual('instance', sot.resource_key)
        self.assertEqual('/instances', sot.base_path)
        self.assertEqual('managed-rdb', sot.service.service_type)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_delete)

    def test_make_basic(self):
        sot = instance.Instance(**INSTANCE_EXAMPLE)
        self.assertEqual(INSTANCE_EXAMPLE['id'], sot.id)
        self.assertEqual(INSTANCE_EXAMPLE['tenant_id'], sot.tenant_id)
        self.assertEqual(INSTANCE_EXAMPLE['name'], sot.name)
        self.assertEqual(INSTANCE_EXAMPLE['description'], sot.description)
        self.assertEqual(INSTANCE_EXAMPLE['flavor'], sot.flavor)
        self.assertEqual(INSTANCE_EXAMPLE['database_version'], sot.database_version)
        self.assertEqual(INSTANCE_EXAMPLE['storage_type'], sot.storage_type)
        self.assertEqual(INSTANCE_EXAMPLE['high_availability'], sot.high_availability)
        self.assertEqual(INSTANCE_EXAMPLE['status'], sot.status)
        self.assertEqual(INSTANCE_EXAMPLE['task_type'], sot.task_type)
        self.assertEqual(INSTANCE_EXAMPLE['task_state'], sot.task_state)
        self.assertEqual(INSTANCE_EXAMPLE['monitoring_state'], sot.monitoring_state)
        self.assertEqual(INSTANCE_EXAMPLE['nodes'], sot.nodes)
        self.assertEqual(INSTANCE_EXAMPLE['network'], sot.network)
        self.assertEqual(INSTANCE_EXAMPLE['metadata'], sot.metadata)
        self.assertEqual(INSTANCE_EXAMPLE['links'], sot.links)
        self.assertEqual(INSTANCE_EXAMPLE['created'], sot.created)
        self.assertEqual(INSTANCE_EXAMPLE['admin_password'], sot.admin_password)

    def test_detail(self):
        sot = instance.InstanceDetail()
        self.assertEqual('/instances/detail', sot.base_path)
        self.assertEqual('managed-rdb', sot.service.service_type)
        self.assertFalse(sot.allow_get)
        self.assertTrue(sot.allow_list)
        self.assertFalse(sot.allow_create)
        self.assertFalse(sot.allow_delete)
        self.assertFalse(sot.allow_update)
        self.assertFalse(sot.patch_update)

    def test_action(self):
        sot = instance.InstanceAction()
        self.assertEqual('/instances/%(instance_id)s/action', sot.base_path)
        self.assertEqual('managed-rdb', sot.service.service_type)

    def test_make_action(self):
        sot = instance.Instance(**INSTANCE_ACTION_EXAMPLE)
        self.assertEqual(INSTANCE_ACTION_EXAMPLE['admin_password'], sot.admin_password)
