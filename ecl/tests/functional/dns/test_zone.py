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

import time

from ecl.tests.functional import base


class TestZone(base.BaseFunctionalTest):

    @classmethod
    def test_01_create(cls):
        zone = cls.conn.dns.create_zone(
            name="test.co.jp.")
        cls.zone_id = zone.id
        time.sleep(10)

    def test_02_get(self):
        zone = self.conn.dns.get_zone(self.zone_id)
        # print(zone)

    def test_03_update(self):
        zone = self.conn.dns.update_zone(self.zone_id, description="for test use")
        # print(zone)
        time.sleep(10)

    def test_04_find(self):
        zone = self.conn.dns.find_zone("test.co.jp.")
        self.assertEqual(zone.id, self.zone_id)

    def test_05_delete(self):
        self.conn.dns.delete_zone(self.zone_id)
        time.sleep(3)

    def test_06_list(self):
        zones = self.conn.dns.zones()
        # print(zones)

    def test_07_get_nameserver(self):
        nameserver = self.conn.dns.get_name_server(self.zone_id)
        # print(nameserver)
