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


class TestVersion(base.BaseFunctionalTest):

    def test_01_versions(self):
        versions = list(self.conn.baremetal.versions())
        version = versions[0]
        self.assertIsInstance(version.status, six.string_types)
        self.assertIsInstance(version.id, six.string_types)
        self.assertIsInstance(version.links, list)

    def test_02_show_version(self):
        version = self.conn.baremetal.get_version()
        print(version)
        self.assertIsInstance(version.status, six.string_types)
        self.assertIsInstance(version.id, six.string_types)
        self.assertIsInstance(version.links, list)
