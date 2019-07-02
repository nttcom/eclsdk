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

import uuid
import six
from ecl.tests.functional import base


class TestKeypair(base.BaseFunctionalTest):

    @classmethod
    def test_01_import(cls):
        cls.NAME = uuid.uuid4().hex
        keypair = cls.conn.baremetal.create_keypair(name=cls.NAME)
        print(keypair)
        assert isinstance(keypair.fingerprint, six.string_types)
        assert isinstance(keypair.name, six.string_types)
        assert isinstance(keypair.public_key, six.string_types)
        assert isinstance(keypair.private_key, six.string_types)

    @classmethod
    def test_02_list(cls):
        keypairs = list(cls.conn.baremetal.keypairs())
        for keypair in keypairs:
            assert isinstance(keypair.fingerprint, six.string_types)
            assert isinstance(keypair.name, six.string_types)
            assert isinstance(keypair.public_key, six.string_types)

    def test_show_03(self):
        keypair = self.conn.baremetal.get_keypair(self.NAME)
        self.assertIsInstance(keypair.public_key, six.string_types)
        self.assertIsInstance(keypair.fingerprint, six.string_types)
        self.assertIsInstance(keypair.name, six.string_types)

    def test_03_delete(self):
        self.conn.baremetal.delete_keypair(self.NAME)

    @classmethod
    def test_05_create(cls):
        cls.NAME2 = uuid.uuid4().hex
        keypair = cls.conn.baremetal.create_keypair(
            name=cls.NAME2,
            public_key="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAQQCtzdf5vKNNSoeMfTUUj65eJLMjXfIbtc2GQn6+EEISHX6vjBzsTMdToQJEhgg+5rYlb5tc2mvPYNbPDIJV8OyV")
        print(keypair)
        assert isinstance(keypair.fingerprint, six.string_types)
        assert isinstance(keypair.name, six.string_types)
        assert isinstance(keypair.public_key, six.string_types)

    def test_06_delete(self):
        self.conn.baremetal.delete_keypair(self.NAME2)
