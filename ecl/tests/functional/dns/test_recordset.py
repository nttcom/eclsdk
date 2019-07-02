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


class TestRecordSet(base.BaseFunctionalTest):

    @classmethod
    def test_01_create(cls):
        recordset1 = cls.conn.dns.create_recordset(
            zone_id="d4f0ea0e-edb6-4bbb-aefd-2944457be234",
            name="ns20.base.co.jp",
            type="A",
            ttl=3600,
            records=["203.0.143.27", "203.0.143.28"]
        )
        # print(recordset1)
        cls.recordset_id = recordset1[0].id
        cls.recordset2_id = recordset1[1].id
        time.sleep(10)

    def test_02_get(self):
        zone = self.conn.dns.get_recordset(zone_id="d4f0ea0e-edb6-4bbb-aefd-2944457be234",
                                           recordset_id=self.recordset_id)
        print(zone)

    def test_03_update(self):
        zone = self.conn.dns.update_recordset(zone_id="d4f0ea0e-edb6-4bbb-aefd-2944457be234",
                                              recordset=self.recordset_id, ttl=3000, description="for test use")
        time.sleep(10)
        # print(zone)

    def test_04_find(self):
        zone = self.conn.dns.find_recordset(zone_id="d4f0ea0e-edb6-4bbb-aefd-2944457be234",
                                            name_or_id="ns19.base.co.jp.")
        # self.assertEqual(zone.id, self.recordset_id)
        # print(zone)

    def test_05_delete(self):
        self.conn.dns.delete_recordset(zone_id="d4f0ea0e-edb6-4bbb-aefd-2944457be234", recordset=self.recordset_id)
        time.sleep(3)

    def test_06_list(self):
        zones = self.conn.dns.recordsets(zone_id="d4f0ea0e-edb6-4bbb-aefd-2944457be234")
        # print(len(zones))

    def test_07_multi_delete(self):
        ids = [self.recordset2_id]
        self.conn.dns.delete_multiple_recordsets(
            "d4f0ea0e-edb6-4bbb-aefd-2944457be234",
            ids,
        )
