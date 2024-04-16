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

import os
import unittest

import six

import ecl
from ecl.tests.functional import base


class TestToken(base.BaseFunctionalTest):
    """Test token resources

    To run this test, you will need.
    - Prior Smart Data Platform login
    - Administrator account
    """
    @classmethod
    def setUpClass(cls):
        # keystone admin endpoint URL
        admin_keystone_url = os.getenv('ADMIN_KEYSTONE_URL')
        # adminstrator account
        admin_username = os.getenv('ADMIN_USER_NAME')
        admin_password = os.getenv('ADMIN_PASSWORD')
        # user information
        cls.user_ecid = os.getenv('USER_ECID')
        cls.user_tenant_id = os.getenv('UESR_TENANT_ID')

        cls.conn = ecl.connection.Connection(auth_url=admin_keystone_url,
                                             username=admin_username,
                                             password=admin_password,
                                             user_domain_id='default',
                                             timeout=100)

    @unittest.skip("Skip as it requires administrator authorization.")
    def test_get_user_token_by_admin(self):
        token = self.conn.sss.get_user_token_by_admin(self.user_ecid)

        self.assertIsInstance(token.methods, list)
        self.assertIsInstance(token.user, dict)
        self.assertIsInstance(token.issued_at, six.string_types)
        self.assertIsInstance(token.expires_at, six.string_types)
        self.assertIsInstance(token.audit_ids, list)
        self.assertIsNone(token.project)
        self.assertIsNone(token.is_domain)
        self.assertIsNone(token.roles)
        self.assertIsNone(token.catalog)
        self.assertIsInstance(token.subject_token, six.string_types)

    @unittest.skip("Skip as it requires administrator authorization.")
    def test_get_user_token_by_admin_with_catalog(self):
        token = self.conn.sss.get_user_token_by_admin(
            self.user_ecid, tenant_id=self.user_tenant_id, no_catalog=False)

        self.assertIsInstance(token.methods, list)
        self.assertIsInstance(token.user, dict)
        self.assertIsInstance(token.issued_at, six.string_types)
        self.assertIsInstance(token.expires_at, six.string_types)
        self.assertIsInstance(token.audit_ids, list)
        self.assertIsInstance(token.project, dict)
        self.assertIsInstance(token.is_domain, bool)
        self.assertIsInstance(token.roles, list)
        self.assertIsInstance(token.catalog, list)
        self.assertIsInstance(token.subject_token, six.string_types)
