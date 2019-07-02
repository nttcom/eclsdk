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


class TestMember(base.BaseFunctionalTest):
    image_id = "1b782d43-4e43-4d96-883b-ff423f8b8b7c"

    def test_01_list(self):
        members = list(self.conn.image.members(self.image_id))
        print(members)

    def test_02_create_member(self):
        member = self.conn.image.create_member(
            self.image_id,
            member="f6a818c3d4aa458798ed86892e7150c0"
        )
        print(member)

    def test_03_update_member(self):
        member = self.conn.image.update_member(
            self.image_id,
            "f6a818c3d4aa458798ed86892e7150c0",
            status="accepted"
        )
        print(member)

    def test_04_show_member(self):
        member = self.conn.image.get_member(
            self.image_id, "f6a818c3d4aa458798ed86892e7150c0"
        )
        print(member)
        self.assertIsInstance(member.member_id, six.string_types)
        self.assertIsInstance(member.created_at, six.string_types)
        self.assertIsInstance(member.image_id, six.string_types)
        self.assertIsInstance(member.status, six.string_types)
        self.assertIsInstance(member.schema, six.string_types)
        self.assertIsInstance(member.updated_at, six.string_types)

    def test_05_delete_member(self):
        member = self.conn.image.delete_member(
            self.image_id, "f6a818c3d4aa458798ed86892e7150c0"
        )
