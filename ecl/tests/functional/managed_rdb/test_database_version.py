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

import six

from ecl.tests.functional import base


class TestDatabaseVersion(base.BaseFunctionalTest):

    def test_database_versions(self):
        database_version_list = list(self.conn.managed_rdb.database_versions())
        print(database_version_list)
        self.assertGreater(len(database_version_list), 0)

        for database_version in database_version_list:
            print(database_version)
            self.assertIsInstance(database_version.id, six.string_types)
            self.assertIsInstance(database_version.name, six.string_types)
            self.assertIsInstance(database_version.dbms_name, six.string_types)
            self.assertIsInstance(database_version.major_version, six.string_types)
            self.assertIsInstance(database_version.minor_version, six.string_types)

    def test_get_database_version(self):
        database_version = self.conn.managed_rdb.get_database_version('POSTGRES_13_2')
        print(database_version)
        self.assertIsInstance(database_version.id, six.string_types)
