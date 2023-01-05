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

from ecl.sss.v2 import token

BASIC_EXAMPLE = {
    "methods": ["password"],
    "user": {
        "domain": {"name": "Default", "id": "default"},
        "name": "USER1",
        "id": "fcb4a033",
        "password_expires_at": None
    },
    "issued_at": "2022-12-12T07:56:28.000000Z",
    "expires_at": "2022-12-12T08:56:28.000000Z",
    "audit_ids": ["cYb6kuPsS1Wiie0pS3m7yg"],
    "project": {
        "domain": {"name": "Default", "id": "default"},
        "id": "32c732c8",
        "name": "test-tenant"
    },
    "is_domain": False,
    "roles": [
        {"id": "db6713f9", "name": "_member_"}
    ],
    "catalog": [
        {
            "endpoints": [
                {"id": "481945da"}
            ]
        }
    ],
    "X-Subject-Token": "token_16718f6557f2",
}


class TestToken(testtools.TestCase):

    def test_token(self):
        sot = token.Token()
        self.assertEqual(None, sot.resources_key)
        self.assertEqual('token', sot.resource_key)
        self.assertEqual('/tokens/users', sot.base_path)
        self.assertEqual('sssv2', sot.service.service_type)

        self.assertTrue(sot.allow_create)
        self.assertFalse(sot.allow_get)
        self.assertFalse(sot.allow_update)
        self.assertFalse(sot.allow_delete)
        self.assertFalse(sot.allow_list)
        self.assertFalse(sot.put_create)

    def test_make_token(self):
        sot = token.Token(**BASIC_EXAMPLE)
        self.assertEqual(BASIC_EXAMPLE['methods'], sot.methods)
        self.assertEqual(BASIC_EXAMPLE['user'], sot.user)
        self.assertEqual(BASIC_EXAMPLE['issued_at'], sot.issued_at)
        self.assertEqual(BASIC_EXAMPLE['expires_at'], sot.expires_at)
        self.assertEqual(BASIC_EXAMPLE['audit_ids'], sot.audit_ids)
        self.assertEqual(BASIC_EXAMPLE['project'], sot.project)
        self.assertEqual(BASIC_EXAMPLE['is_domain'], sot.is_domain)
        self.assertEqual(BASIC_EXAMPLE['roles'], sot.roles)
        self.assertEqual(BASIC_EXAMPLE['catalog'], sot.catalog)
        self.assertEqual(BASIC_EXAMPLE['X-Subject-Token'], sot.subject_token)
