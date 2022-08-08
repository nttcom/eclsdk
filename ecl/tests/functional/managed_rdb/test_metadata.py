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


class TestMetadata(base.BaseFunctionalTest):

    def test_metadatas(self):
        # IDはMock Serverに合わせて変更する
        instance_id = 'b87943ba-5a2a-4974-e5f4-f864a9fffd14'
        metadata = self.conn.managed_rdb.metadatas(instance_id)
        print(metadata)
        self.assertIsInstance(metadata.metadata, dict)

    def test_replace_metadata(self):
        # IDはMock Serverに合わせて変更する
        instance_id = '9809065a-7ce0-a098-a790-46078f0e93aa'
        metadata = metadata = {
            'data-type': 'PRODUCT',
            'data-name': 'Apache Server',
        }
        self.conn.managed_rdb.replace_metadata(instance_id, metadata)
        assert True
