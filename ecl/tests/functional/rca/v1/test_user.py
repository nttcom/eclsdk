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
    def test_01_list_user(cls):
        users = list(cls.conn.rca.list_users())
        user = users[0]
        cls.user_name = user.id
        assert isinstance(user.id, six.string_types)
        assert isinstance(user.vpn_endpoints, list)

    def test_02_show_user(self):
        user = self.conn.rca.get_user(self.user_name)
        self.assertIsInstance(user.name, six.string_types)
        self.assertIsInstance(user.vpn_endpoints, list)

    def test_03_create_user(self):
        user = self.conn.rca.create_user(
            password="Passw0rd!"
        )

    def test_04_update_user(self):
        user = self.conn.rca.update_user(
            username="72ab9350a47a4173966ad02dc51b32a1", password="Pa55w0rd+"
        )
        self.assertIsInstance(user.name, six.string_types)
        self.assertIsInstance(user.vpn_endpoints, list)

    def test_05_delete_user(self):
        self.conn.rca.delete_user("wrong_user_name")
