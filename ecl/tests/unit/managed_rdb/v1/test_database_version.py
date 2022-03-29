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

from ecl.managed_rdb.v1 import database_version

IDENTIFIER = 'IDENTIFIER'
DATABASE_VERSION_EXAMPLE = {
    'id': IDENTIFIER,
    'name': 'POSTGRES_13_2',
    'dbms_name': 'POSTGRES',
    'major_version': 13,
    'minor_version': 2,
}


class TestDatabaseVersion(testtools.TestCase):

    def test_basic(self):
        sot = database_version.DatabaseVersion()
        self.assertEqual('database_versions', sot.resources_key)
        self.assertEqual('database_versions', sot.resource_key)
        self.assertEqual('/database_versions', sot.base_path)
        self.assertEqual('managed-rdb', sot.service.service_type)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_list)

    def test_make_basic(self):
        sot = database_version.DatabaseVersion(**DATABASE_VERSION_EXAMPLE)
        self.assertEqual(DATABASE_VERSION_EXAMPLE['id'], sot.id)
        self.assertEqual(DATABASE_VERSION_EXAMPLE['name'], sot.name)
        self.assertEqual(DATABASE_VERSION_EXAMPLE['dbms_name'], sot.dbms_name)
        self.assertEqual(DATABASE_VERSION_EXAMPLE['major_version'], sot.major_version)
        self.assertEqual(DATABASE_VERSION_EXAMPLE['minor_version'], sot.minor_version)
