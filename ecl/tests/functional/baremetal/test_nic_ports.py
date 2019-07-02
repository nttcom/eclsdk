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


class TestNicPorts(base.BaseFunctionalTest):

    @classmethod
    def test_01_list(cls):
        server_id = "752aac2e-4b82-4d47-a7c7-fcbd0cbc86e2"
        ports = list(cls.conn.baremetal.nic_physical_ports(server_id))
        cls.port = ports[0]
        assert isinstance(cls.port.id, six.string_types)
        assert isinstance(cls.port.mac_addr, six.string_types)
        assert isinstance(cls.port.network_physical_port_id,
                          six.string_types)
        assert isinstance(cls.port.plane, six.string_types)
        assert isinstance(cls.port.attached_ports, list)
        assert isinstance(cls.port.hardware_id, six.string_types)

    def test_02_show(self):
        server_id = "752aac2e-4b82-4d47-a7c7-fcbd0cbc86e2"
        port = "e0ca770c-2ced-4099-b051-26512d9af43d"
        port = self.conn.baremetal.get_nic_physical_port(server_id, port)
        self.assertIsInstance(port.hardware_id, six.string_types)
        self.assertIsInstance(port.id, six.string_types)
        self.assertIsInstance(port.mac_addr, six.string_types)
        self.assertIsInstance(port.network_physical_port_id,
                              six.string_types)
        self.assertIsInstance(port.attached_ports, list)
        self.assertIsInstance(port.plane, six.string_types)
