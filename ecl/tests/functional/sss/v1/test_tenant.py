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


class TestTenant(base.BaseFunctionalTest):

    @classmethod
    def test_01_create_tenant(cls):
        tenant = cls.conn.sss.create_tenant(
            tenant_name="T01test",
            description="forSDKtest",
            region="lab3ec",
            # contract_id="econ123467890",
        )
        cls.tenant_id = tenant.id
        print(tenant.id)
        assert isinstance(tenant.id, six.string_types)
        assert isinstance(tenant.tenant_name, six.string_types)
        assert isinstance(tenant.description, six.string_types)
        assert isinstance(tenant.region, six.string_types)
        assert isinstance(tenant.contract_id, six.string_types)

    def test_02_delete_tenant(self):
        self.conn.sss.delete_tenant(self.tenant_id)
