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

from ecl.compute.v2 import _proxy
from ecl.compute.v2 import availability_zone as az
from ecl.compute.v2 import extension
from ecl.compute.v2 import flavor
from ecl.compute.v2 import image
from ecl.compute.v2 import keypair
from ecl.compute.v2 import limits
from ecl.compute.v2 import server
from ecl.compute.v2 import server_interface
from ecl.tests.unit import test_proxy_base2


class TestComputeProxy(test_proxy_base2.TestProxyBase):
    def setUp(self):
        super(TestComputeProxy, self).setUp()
        self.proxy = _proxy.Proxy(self.session)

    def test_extensions(self):
        self.verify_list_no_kwargs(self.proxy.extensions, extension.Extension,
                                   paginated=False)

    def test_flavor_find(self):
        self.verify_find(self.proxy.find_flavor, flavor.Flavor)

    def test_flavor_get(self):
        self.verify_get(self.proxy.get_flavor, flavor.Flavor)

    def test_flavors_detailed(self):
        self.verify_list(self.proxy.flavors, flavor.FlavorDetail,
                         paginated=True,
                         method_kwargs={"details": True, "query": 1},
                         expected_kwargs={"query": 1})

    def test_flavors_not_detailed(self):
        self.verify_list(self.proxy.flavors, flavor.Flavor,
                         paginated=True,
                         method_kwargs={"details": False, "query": 1},
                         expected_kwargs={"query": 1})

    def test_image_delete(self):
        self.verify_delete(self.proxy.delete_image, image.Image, False)

    def test_image_delete_ignore(self):
        self.verify_delete(self.proxy.delete_image, image.Image, True)

    def test_image_find(self):
        self.verify_find(self.proxy.find_image, image.Image)

    def test_image_get(self):
        self.verify_get(self.proxy.get_image, image.Image)

    def test_images_detailed(self):
        self.verify_list(self.proxy.images, image.ImageDetail,
                         paginated=True,
                         method_kwargs={"details": True, "query": 1},
                         expected_kwargs={"query": 1})

    def test_images_not_detailed(self):
        self.verify_list(self.proxy.images, image.Image,
                         paginated=True,
                         method_kwargs={"details": False, "query": 1},
                         expected_kwargs={"query": 1})

    def test_keypair_create(self):
        self.verify_create(self.proxy.create_keypair, keypair.Keypair)

    def test_keypair_delete(self):
        self.verify_delete(self.proxy.delete_keypair, keypair.Keypair, False)

    def test_keypair_delete_ignore(self):
        self.verify_delete(self.proxy.delete_keypair, keypair.Keypair, True)

    def test_keypair_find(self):
        self.verify_find(self.proxy.find_keypair, keypair.Keypair)

    def test_keypair_get(self):
        self.verify_get(self.proxy.get_keypair, keypair.Keypair)

    def test_keypairs(self):
        self.verify_list_no_kwargs(self.proxy.keypairs, keypair.Keypair,
                                   paginated=False)

    def test_limits_get(self):
        self.verify_get(self.proxy.get_limits, limits.Limits, value=[])

    def test_server_interface_create(self):
        self.verify_create(self.proxy.create_server_interface,
                           server_interface.ServerInterface,
                           method_kwargs={"server": "test_id"},
                           expected_kwargs={"server_id": "test_id"})

    def test_server_interface_delete(self):
        self.proxy._get_uri_attribute = lambda *args: args[1]

        interface_id = "test_interface_id"
        server_id = "test_server_id"
        test_interface = server_interface.ServerInterface(id=interface_id)
        test_interface.server_id = server_id

        # Case1: ServerInterface instance is provided as value
        self._verify2("ecl.proxy2.BaseProxy._delete",
                      self.proxy.delete_server_interface,
                      method_args=[test_interface],
                      method_kwargs={"server": server_id},
                      expected_args=[server_interface.ServerInterface],
                      expected_kwargs={"server_id": server_id,
                                       "port_id": interface_id,
                                       "ignore_missing": True})

        # Case2: ServerInterface ID is provided as value
        self._verify2("ecl.proxy2.BaseProxy._delete",
                      self.proxy.delete_server_interface,
                      method_args=[interface_id],
                      method_kwargs={"server": server_id},
                      expected_args=[server_interface.ServerInterface],
                      expected_kwargs={"server_id": server_id,
                                       "port_id": interface_id,
                                       "ignore_missing": True})

    def test_server_interface_delete_ignore(self):
        self.proxy._get_uri_attribute = lambda *args: args[1]
        self.verify_delete(self.proxy.delete_server_interface,
                           server_interface.ServerInterface, True,
                           method_kwargs={"server": "test_id"},
                           expected_args=[server_interface.ServerInterface],
                           expected_kwargs={"server_id": "test_id",
                                            "port_id": "resource_or_id"})

    def test_server_interfaces(self):
        self.verify_list(self.proxy.server_interfaces,
                         server_interface.ServerInterface,
                         paginated=False, method_args=["test_id"],
                         expected_kwargs={"server_id": "test_id"})

    def test_server_create_attrs(self):
        self.verify_create(self.proxy.create_server, server.Server)

    def test_server_delete(self):
        self.verify_delete(self.proxy.delete_server, server.Server, False)

    def test_server_delete_ignore(self):
        self.verify_delete(self.proxy.delete_server, server.Server, True)

    def test_server_force_delete(self):
        self._verify("ecl.compute.v2.server.Server.force_delete",
                     self.proxy.delete_server,
                     method_args=["value", False, True])

    def test_server_find(self):
        self.verify_find(self.proxy.find_server, server.Server)

    def test_server_get(self):
        self.verify_get(self.proxy.get_server, server.Server)

    def test_servers_detailed(self):
        self.verify_list(self.proxy.servers, server.ServerDetail,
                         paginated=True,
                         method_kwargs={"details": True,
                                        "changes_since": 1, "image": 2},
                         expected_kwargs={"changes_since": 1, "image": 2})

    def test_servers_not_detailed(self):
        self.verify_list(self.proxy.servers, server.Server,
                         paginated=True,
                         method_kwargs={"details": False,
                                        "changes_since": 1, "image": 2},
                         expected_kwargs={"paginated": True,
                                          "changes_since": 1, "image": 2})

    def test_server_update(self):
        self.verify_update(self.proxy.update_server, server.Server)

    def test_server_wait_for(self):
        value = server.Server(id='1234')
        self.verify_wait_for_status(
            self.proxy.wait_for_server,
            method_args=[value],
            expected_args=[value, 'ACTIVE', ['ERROR'], 2, 120])

    def test_server_resize(self):
        self._verify("ecl.compute.v2.server.Server.resize",
                     self.proxy.resize_server,
                     method_args=["value", "test-flavor"],
                     expected_args=["test-flavor"])

    def test_availability_zones(self):
        self.verify_list_no_kwargs(self.proxy.availability_zones,
                                   az.AvailabilityZone,
                                   paginated=False)

    def test_get_all_server_metadata(self):
        self._verify2("ecl.compute.v2.server.Server.get_metadata",
                      self.proxy.get_server_metadata,
                      method_args=["value"],
                      method_result=server.Server(id="value", metadata={}),
                      expected_args=[self.session],
                      expected_result={})

    def test_set_server_metadata(self):
        kwargs = {"a": "1", "b": "2"}
        id = "an_id"
        self._verify2("ecl.compute.v2.server.Server.set_metadata",
                      self.proxy.set_server_metadata,
                      method_args=[id],
                      method_kwargs=kwargs,
                      method_result=server.Server.existing(id=id,
                                                           metadata=kwargs),
                      expected_args=[self.session],
                      expected_kwargs=kwargs,
                      expected_result=kwargs)

    def test_delete_server_metadata(self):
        self._verify2("ecl.compute.v2.server.Server.delete_metadata",
                      self.proxy.delete_server_metadata,
                      expected_result=None,
                      method_args=["value", "key"],
                      expected_args=[self.session, "key"])
