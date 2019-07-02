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


class TestApiKey(base.BaseFunctionalTest):

    def test_01_update_api_key(self):
        api_key = self.conn.sss.update_api_key(
            "ecid1000378024"
        )
        self.assertIsInstance(api_key.user_id, six.string_types)
        self.assertIsInstance(api_key.keystone_name, six.string_types)
        self.assertIsInstance(api_key.keystone_password, six.string_types)
        self.assertIsInstance(api_key.status, six.string_types)
