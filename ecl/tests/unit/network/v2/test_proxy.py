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

from ecl.network.v2 import _proxy
from ecl.network.v2 import extension
from ecl.network.v2 import load_balancer
from ecl.network.v2 import network
from ecl.network.v2 import port
from ecl.network.v2 import quota
from ecl.network.v2 import subnet
from ecl.network.v2 import vpn
from ecl.tests.unit import test_proxy_base2


class TestNetworkProxy(test_proxy_base2.TestProxyBase):
    def setUp(self):
        super(TestNetworkProxy, self).setUp()
        self.proxy = _proxy.Proxy(self.session)

    def test_load_balancer_create_attrs(self):
        self.verify_create(self.proxy.create_load_balancer,
                           load_balancer.LoadBalancer, 
                           method_kwargs={"load_balancer_plan_id":"1212"})

    def test_load_balancer_delete(self):
        self.verify_delete(self.proxy.delete_load_balancer,
                           load_balancer.LoadBalancer, 
                           False,
                           method_kwargs={})

    def test_load_balancer_delete_ignore(self):
        self.verify_delete(self.proxy.delete_load_balancer,
                           load_balancer.LoadBalancer, True, 
                           method_kwargs={})

    def test_load_balancer_get(self):
        self.verify_get(self.proxy.get_load_balancer,
                        load_balancer.LoadBalancer)

    def test_load_balancers(self):
        self.verify_list(self.proxy.load_balancers,
                         load_balancer.LoadBalancer,
                         paginated=False)

    def test_load_balancer_update(self):
        self.verify_update(self.proxy.update_load_balancer,
                           load_balancer.LoadBalancer)

    def test_network_create_attrs(self):
        self.verify_create(self.proxy.create_network, network.Network, 
                           method_kwargs={"name":"test"})

    def test_network_delete(self):
        self.verify_delete(self.proxy.delete_network, network.Network, False)

    def test_network_delete_ignore(self):
        self.verify_delete(self.proxy.delete_network, network.Network, True)

    def test_network_find(self):
        self.verify_find(self.proxy.find_network, network.Network)

    def test_network_get(self):
        self.verify_get(self.proxy.get_network, network.Network)

    def test_networks(self):
        self.verify_list(self.proxy.networks, network.Network,
                         paginated=False)

    def test_network_update(self):
        self.verify_update(self.proxy.update_network, network.Network)

    def test_port_create_attrs(self):
        self.verify_create(self.proxy.create_port, port.Port, 
                           method_kwargs={"name":"test"})

    def test_port_delete(self):
        self.verify_delete(self.proxy.delete_port, port.Port, False)

    def test_port_delete_ignore(self):
        self.verify_delete(self.proxy.delete_port, port.Port, True)

    def test_port_find(self):
        self.verify_find(self.proxy.find_port, port.Port)

    def test_port_get(self):
        self.verify_get(self.proxy.get_port, port.Port)

    def test_ports(self):
        self.verify_list(self.proxy.ports, port.Port, paginated=False)

    def test_port_update(self):
        self.verify_update(self.proxy.update_port, port.Port)

    def test_quota_get(self):
        self.verify_get(self.proxy.get_quota, quota.Quota)

    # def test_quota_default_get(self):
    #     self.verify_get(self.proxy.get_quota_default, quota.QuotaDefault,
    #                     value=[mock.sentinel.project_id],
    #                     expected_args=[quota.QuotaDefault],
    #                     expected_kwargs={"path_args": {
    #                         "project": mock.sentinel.project_id}})

    def test_subnet_create_attrs(self):
        self.verify_create(self.proxy.create_subnet, subnet.Subnet, 
                           method_kwargs={"network_id": "test_id", 
                                          "cidr": "12121"})

    def test_subnet_delete(self):
        self.verify_delete(self.proxy.delete_subnet, subnet.Subnet, False)

    def test_subnet_delete_ignore(self):
        self.verify_delete(self.proxy.delete_subnet, subnet.Subnet, True)

    def test_subnet_find(self):
        self.verify_find(self.proxy.find_subnet, subnet.Subnet)

    def test_subnet_get(self):
        self.verify_get(self.proxy.get_subnet, subnet.Subnet)

    def test_subnets(self):
        self.verify_list(self.proxy.subnets, subnet.Subnet, paginated=False)

    def test_subnet_update(self):
        self.verify_update(self.proxy.update_subnet, subnet.Subnet)

    def test_vpn_service_get(self):
        self.verify_get(self.proxy.get_vpn_service, vpn.VPNService)

    def test_vpn_services(self):
        self.verify_list(self.proxy.vpn_services, vpn.VPNService,
                         paginated=False, 
                         mock_method="ecl.proxy2.BaseProxy._list")

