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


class TestRole(base.BaseFunctionalTest):

    def test_01_create_role(self):
        role = self.conn.sss.create_role(
            tenant_id="5de7c7c21bba4939b071b3879172213e",
            user_id="ecid1000030914",
        )
        assert isinstance(role.user_id, six.string_types)
        assert isinstance(role.tenant_id, six.string_types)
        assert isinstance(role.tenant_name, six.string_types)
        assert isinstance(role.region_id, six.string_types)
        assert isinstance(role.region_name, six.string_types)
        assert isinstance(role.role_name, six.string_types)

    def test_02_delete_role(self):
        self.conn.sss.delete_role("5de7c7c21bba4939b071b3879172213e",
                                  "ecid1000030914")
