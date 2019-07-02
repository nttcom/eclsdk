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

from ecl.tests.functional import base


class TestTag(base.BaseFunctionalTest):
    image_id = "1b782d43-4e43-4d96-883b-ff423f8b8b7c"

    def test_01_add_tag(self):
        tag = self.conn.image.add_tag(self.image_id, "tag01-01")

    def test_02_delete_tag(self):
        tag = self.conn.image.delete_tag(self.image_id, "tag01-01")
