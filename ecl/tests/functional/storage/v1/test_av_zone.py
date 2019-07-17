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


class TestAVZone(base.BaseFunctionalTest):
    def test_01_av_zones(self):
        zones = list(self.conn.storage.availability_zones(details=True))
        print(zones[0])
        zone = zones[0]
        self.assertIsInstance(zone.zoneState, dict)
        self.assertIsInstance(zone.zoneName, six.string_types)

    def test_02_find_av_zones(self):
        zones = self.conn.storage.find_availability_zone("zone1-groupa")
        print(zones)
