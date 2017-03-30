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

import mock
import testtools

from ecl.compute.v2 import volume

VOLUME_RESP_BODY = {
    "displayName": "test-name",
    "displayDescription": "test-descr",
    "availabilityZone": "zone1_groupa",
    "status": "creating",
    "attachments": [{}],
    "volumeType": "nfsdriver",
    "snapshotId": None,
    "size": 15,
    "id": "e15c8756-a9d2-49b1-9192-ce898196e985",
    "createdAt": "2016-10-28T03:03:33.000000",
    "metadata": {}
}



class TestVolume(testtools.TestCase):

    def test_basic(self):
        sot = volume.Volume()
        self.assertEqual("volume", sot.resource_key)
        self.assertEqual("volumes", sot.resources_key)
        self.assertEqual("/os-volumes", sot.base_path)
        self.assertEqual("compute", sot.service.service_type)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)

    def test_make_it(self):
        sot = volume.Volume(**VOLUME_RESP_BODY)

        self.assertEqual(VOLUME_RESP_BODY["displayName"], sot.name)
        self.assertEqual(VOLUME_RESP_BODY["displayDescription"], sot.description)
        self.assertEqual(VOLUME_RESP_BODY["availabilityZone"], sot.availability_zone)
        self.assertEqual(VOLUME_RESP_BODY["status"], sot.status)
        self.assertEqual(VOLUME_RESP_BODY["attachments"], sot.attachments)
        self.assertEqual(VOLUME_RESP_BODY["volumeType"], sot.volume_type)
        self.assertEqual(VOLUME_RESP_BODY["snapshotId"], sot.snapshot_id)
        self.assertEqual(VOLUME_RESP_BODY["size"], sot.size)
        self.assertEqual(VOLUME_RESP_BODY["id"], sot.id)
        self.assertEqual(VOLUME_RESP_BODY["createdAt"], sot.created_at)
        self.assertEqual(VOLUME_RESP_BODY["metadata"], sot.metadata)


