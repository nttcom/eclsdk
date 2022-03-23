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

from ecl.managed_rdb.v1 import quota

QUOTA_EXAMPLE = {
    'max_instance_count': 512,
    'max_instance_metadata_count': 256,
}


class TestQuota(testtools.TestCase):

    def test_basic(self):
        sot = quota.Quota()
        self.assertEqual('quota', sot.resource_key)
        self.assertEqual('/quotas', sot.base_path)
        self.assertEqual('managed-rdb', sot.service.service_type)
        self.assertTrue(sot.allow_get)

    def test_make_basic(self):
        sot = quota.Quota(**QUOTA_EXAMPLE)
        self.assertEqual(QUOTA_EXAMPLE['max_instance_count'], sot.max_instance_count)
        self.assertEqual(QUOTA_EXAMPLE['max_instance_metadata_count'],
                         sot.max_instance_metadata_count)
