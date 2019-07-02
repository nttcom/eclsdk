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


class TestUser(base.BaseFunctionalTest):

    @classmethod
    def setUpClass(cls):
        super(TestUser, cls).setUpClass()
        users_list = list(cls.conn.sss.users())
        cls.one_user = users_list[0]

    def test_users(self):
        users = list(self.conn.sss.users())
        for i in users:
            print(i.id + " " + i.login_id)
        self.assertGreater(len(users), 0)

    def test_01_find_user_by_id(self):
        user = self.conn.sss.find_user(self.one_user.id)
        self.assertIsInstance(user.login_id, six.string_types)
        self.assertIsInstance(user.mail_address, six.string_types)
        self.assertIsInstance(user.contract_owner, bool)
        self.assertIsInstance(user.keystone_name, six.string_types)
        self.assertIsInstance(user.keystone_password, six.string_types)
        self.assertIsInstance(user.keystone_endpoint, six.string_types)
        self.assertIsInstance(user.sss_endpoint, six.string_types)
        self.assertIsInstance(user.contract_id, six.string_types)
        self.assertIsInstance(user.login_integration, six.string_types)
        self.assertIsInstance(user.external_reference_id, six.string_types)
        self.assertEqual(user.id, self.one_user.id)

    def test_02_get_user_by_id(self):
        user = self.conn.sss.get_user(self.one_user.id)
        self.assertIsInstance(user.login_id, six.string_types)
        self.assertIsInstance(user.mail_address, six.string_types)
        self.assertIsInstance(user.contract_owner, bool)
        self.assertIsInstance(user.keystone_name, six.string_types)
        self.assertIsInstance(user.keystone_password, six.string_types)
        self.assertIsInstance(user.keystone_endpoint, six.string_types)
        self.assertIsInstance(user.sss_endpoint, six.string_types)
        self.assertIsInstance(user.contract_id, six.string_types)
        self.assertIsInstance(user.login_integration, six.string_types)
        self.assertIsInstance(user.external_reference_id, six.string_types)
        self.assertEqual(user.id, self.one_user.id)

    @classmethod
    def test_03_create_user(cls):
        user = cls.conn.sss.create_user(
            login_id="sdk_test02",
            mail_address="example@ntt.com",
            password="Mypassword01",
            notify_password="false",
        )
        assert isinstance(user.login_id, six.string_types)
        assert isinstance(user.mail_address, six.string_types)
        assert isinstance(user.id, six.string_types)
        assert isinstance(user.keystone_name, six.string_types)
        assert isinstance(user.keystone_password, six.string_types)
        assert isinstance(user.keystone_endpoint, six.string_types)
        assert isinstance(user.sss_endpoint, six.string_types)
        assert isinstance(user.password, six.string_types)
        cls.new_account_id = user.id

    def test_04_update_user(self):
        self.conn.sss.update_user(
            self.new_account_id,
            mail_address="example2@ntt.com",
        )
        user = self.conn.sss.get_user(self.new_account_id)
        self.assertEqual(user.mail_address, "example2@ntt.com")

    def test_05_delete_user(self):
        self.conn.sss.delete_user(self.new_account_id)
