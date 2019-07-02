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


class TestLoadBalancerAction(base.BaseFunctionalTest):
    def test_01_reboot_load_balancer(self):
        reboot = self.conn.network.reboot_load_balancer(
            "fd03dc6d-15dc-41c1-9ef5-0ea49ab88303",
            "HARD"
        )

    def test_02_reset_password(self):
        resp = self.conn.network.reset_password_load_balancer(
            "7589f9cd-400f-4f0e-8da3-de94fc919a0e",
            "user-read"
        )
        print(resp)
        self.assertIsInstance(resp.new_password, six.string_types)
        self.assertIsInstance(resp.username, six.string_types)
