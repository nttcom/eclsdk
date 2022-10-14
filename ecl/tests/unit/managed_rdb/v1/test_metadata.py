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

from ecl.managed_rdb.v1 import metadata

METADATA_EXAMPLE = {
    'metadata': {
        'data-type': 'PRODUCT',
        'data-name': 'Apache Server',
    },
}


class TestMetadata(testtools.TestCase):

    def test_basic(self):
        sot = metadata.Metadata()
        self.assertEqual('/v1.0/instances/%(instance_id)s/metadata', sot.base_path)
        self.assertEqual('managed-rdb', sot.service.service_type)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_update)

    def test_make_basic(self):
        sot = metadata.Metadata(**METADATA_EXAMPLE)
        self.assertEqual(METADATA_EXAMPLE['metadata'], sot.metadata)
