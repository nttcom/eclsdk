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

from ecl.virtual_network_appliance.v1 import virtual_network_appliance as v

IDENTIFIER = 'IDENTIFIER'
BASIC_EXAMPLE = {
    'format': 'set',
    'data': 'c2V0IGludGVyZmFjZXMgZ2UtMC8wLzAgZGVzY3JpcHRpb24gInZuYTAiCnNldCBpbnRlcmZhY2VzIGdlLTAvMC8xIGRlc2NyaXB0aW9uICJ2bmExIgo=',
}

class TestVirtualNetworkApplianceAction(testtools.TestCase):

    def test_basic(self):
        sot = v.VirtualNetworkAppliance()

        self.assertEqual("virtual_network_appliances", sot.resources_key)
        self.assertEqual("virtual_network_appliance", sot.resource_key)
        self.assertEqual('/v1.0/virtual_network_appliances', sot.base_path)
        self.assertEqual("virtual-network-appliance", sot.service.service_type)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_delete)

    def test_export_configuration(self):
        sot = v.VirtualNetworkAppliance(**BASIC_EXAMPLE)
        self.assertEqual(BASIC_EXAMPLE['format'], sot.format)
        self.assertEqual(BASIC_EXAMPLE['data'], sot.data)