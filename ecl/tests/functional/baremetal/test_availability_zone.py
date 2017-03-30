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


class TestAvailabilityZone(base.BaseFunctionalTest):

    def test_01_List_AvailabilityZone(self):
        zones = list(self.conn.baremetal.availability_zones())
        self.assertGreater(len(zones), 0)
        zone = zones[0]
        assert isinstance(zone.name, six.string_types)
        assert isinstance(zone.state, dict)
