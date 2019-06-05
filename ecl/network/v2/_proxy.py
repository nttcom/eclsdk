# -*- coding: utf-8 -*-

from ecl.network.v2 import common_function_pool as _common_function_pool
from ecl.network.v2 import common_function as _common_function
from ecl.network.v2 import common_function_gateway as _common_function_gateway
from ecl.network.v2 import colocation_space as _colocation_space
from ecl.network.v2 import colocation_physical_link as _colocation_physical_link
from ecl.network.v2 import colocation_logical_link as _colocation_logical_link
from ecl.network.v2 import extension as _extension
from ecl.network.v2 import network as _network
from ecl.network.v2 import subnet as _subnet
from ecl.network.v2 import port as _port
from ecl.network.v2 import physical_port as _physical_port
from ecl.network.v2 import quota as _quota
from ecl.network.v2 import reserved_address as _reserved_address
from ecl.network.v2 import firewall as _firewall
from ecl.network.v2 import firewall_interface as _firewall_if
from ecl.network.v2 import firewall_plan as _firewall_plan
from ecl.network.v2 import firewall_action as _firewall_action
from ecl.network.v2 import load_balancer as _load_balancer
from ecl.network.v2 import load_balancer_interface as _load_balancer_if
from ecl.network.v2 import load_balancer_plan as _load_balancer_plan
from ecl.network.v2 import load_balancer_action as _load_balancer_action
from ecl.network.v2 import load_balancer_syslog_server as _load_balancer_syslog
from ecl.network.v2 import gw_interface as _gwif
from ecl.network.v2 import internet as _internet
from ecl.network.v2 import publicip as _publicip
from ecl.network.v2 import qos_option as _qos_option
from ecl.network.v2 import static_route as _static_route
from ecl.network.v2 import vpn as _vpn
from ecl.network.v2 import interdc as _interdc
from ecl.network.v2 import aws as _aws
from ecl.network.v2 import gcp as _gcp
from ecl.network.v2 import tenant_connection as _tenant_connection
from ecl.network.v2 import azure as _azure
from ecl.network.v2 import fic as _fic

from ecl import proxy2


class Proxy(proxy2.BaseProxy):

    def create_network(self, admin_state_up=None, description=None,
                       name=None, plane=None, tenant_id=None,
                       tags=None):
        """Create a new network from attributes

        :param bool admin_state_up: administrative state,
                                     default true
        :param string description: description of network
        :param string name: name of network
        :param string plane: Type of the traffic will be used.
                           value should be "data" or "storage"
        :param string tenant_id: tenant id to create network
        :param dict tags: tags of network

        :returns: The results of network creation
        :rtype: :class:`~ecl.network.v2.network.Network`
        """
        body = dict()
        body.setdefault("admin_state_up", False)

        if admin_state_up:
            body["admin_state_up"] = admin_state_up
        if description:
            body["description"] = description
        if name:
            body["name"] = name
        if tenant_id:
            body["tenant_id"] = tenant_id
        if plane:
            body["plane"] = plane
        if tags:
            body["tags"] = tags
        return self._create(_network.Network, **body)

    def delete_network(self, network, ignore_missing=False):
        """Delete a network

        :param network:
            The value can be either the ID of a network or a
            :class:`~ecl.network.v2.network.Network` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the network does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent network.

        :returns: ``None``
        """
        self._delete(_network.Network, network, ignore_missing=ignore_missing)

    def find_network(self, name_or_id, ignore_missing=False):
        """Find a single network

        :param name_or_id: The name or ID of a network.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.network.v2.network.Network` or None
        """
        return self._find(_network.Network, name_or_id,
                          ignore_missing=ignore_missing)

    def get_network(self, network):
        """Get a single network

        :param network:
            The value can be the ID of a network or a
            :class:`~ecl.network.v2.network.Network` instance.

        :returns: One :class:`~ecl.network.v2.network.Network`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_network.Network, network)

    def networks(self, **params):
        """Return a list of networks
        :param params: The parameters as query string
                       to get networks by specified condition.
        :returns: A list of network objects
        :rtype: list of :class:`~ecl.network.v2.network.Network`
        """
        return list(self._list(_network.Network, paginated=False, **params))

    def update_network(self, network, **params):
        """Update a network

        :param network:
            Either the id of a network or a
            :class:`~ecl.network.v2.network.Network` instance.
        :attrs \*\*params: Parameters for network update.

            * bool admin_state_up: admin state of network to update
            * string name: name of network to update
            * string description: description of network to update
            * dict tags: tags of network to update

        :returns: The updated network
        :rtype: :class:`~ecl.network.v2.network.Network`
        """
        if not isinstance(network, _network.Network):
            network = self._get_resource(_network.Network, network)
            network._body.clean()
        return self._update(_network.Network, network, **params)

    def find_extension(self, name_or_id, ignore_missing=False):
        """Find a single extension

        :param name_or_id: The name or ID of a extension.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.network.v2.extension.Extension`
                  or ``None``
        """
        return self._find(_extension.Extension, name_or_id,
                          ignore_missing=ignore_missing)

    def extensions(self):
        """Return a list of extensions

        :returns: A list of extension objects
        :rtype: :class:`~ecl.network.v2.extension.Extension`
        """
        return list(self._list(_extension.Extension, paginated=False))

    def get_extension(self, extension):
        """Get a single extension

        :param extension:
            The value can be the ID of a extension or a
            :class:`~ecl.network.v2.extension.Extension` instance.

        :returns: One :class:`~ecl.network.v2.extension.Extension`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_extension.Extension, extension)

    def create_port(self, admin_state_up=None, allowed_address_pairs=None,
                    mac_address=None, description=None, device_id=None,
                    device_owner=None, fixed_ips=None, name=None,
                    network_id=None, segmentation_id=None,
                    segmentation_type=None, tags=None):
        """Create a new port from attributes

        :param string admin_state_up: The admin state of port to create
        :param array allowed_address_pairs: allowed address pairs
                        e.g. [{"mac_address": <mac>, "ip_address": <ipv4/cidr>}]
        :param string mac_address: The mac address of port to create
        :param string description: The description of port to create
        :param string device_id: The device id of port to create
        :param string device_owner: The device owner of port to create
        :param array fixed_ips: The fixed ips of port to create
                        e.g. [{"ip_address":<ipv4> , "subnet_id": <uuid> }, ]
        :param string name: The name of port to create
        :param string network_id: The network id of port to create
        :param int segmentation_id: The segmentation id of port to create
        :param string segmentation_type: The segmentation type of port to create
        :param dict tags: tags of port

        :returns: The results of port creation
        :rtype: :class:`~ecl.network.v2.port.Port`
        """
        body = dict()
        if admin_state_up:
            body["admin_state_up"] = admin_state_up
        if allowed_address_pairs:
            body["allowed_address_pairs"] = allowed_address_pairs
        if mac_address:
            body["mac_address"] = mac_address
        if description:
            body["description"] = description
        if device_id:
            body["device_id"] = device_id
        if device_owner:
            body["device_owner"] = device_owner
        if fixed_ips or fixed_ips == []:
            body["fixed_ips"] = fixed_ips
        if name:
            body["name"] = name
        if network_id:
            body["network_id"] = network_id
        if segmentation_id:
            body["segmentation_id"] = segmentation_id
        if segmentation_type:
            body["segmentation_type"] = segmentation_type
        if tags:
            body["tags"] = tags

        return self._create(_port.Port, **body)

    def delete_port(self, port, ignore_missing=False):
        """Delete a port

        :param port: The value can be either the ID of a port or a
                     :class:`~ecl.network.v2.port.Port` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the port does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent port.

        :returns: ``None``
        """
        self._delete(_port.Port, port, ignore_missing=ignore_missing)

    def find_port(self, name_or_id, ignore_missing=False):
        """Find a single port

        :param name_or_id: The name or ID of a port.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.network.v2.port.Port` or None
        """
        return self._find(_port.Port, name_or_id,
                          ignore_missing=ignore_missing)

    def get_port(self, port):
        """Get a single port

        :param port: The value can be the ID of a port or a
                     :class:`~ecl.network.v2.port.Port` instance.

        :returns: One :class:`~ecl.network.v2.port.Port`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_port.Port, port)

    def ports(self, **query):
        """Return a list of ports

        :param query: Query parameters to select results
        :returns: A list of port objects
        :rtype: :class:`~ecl.network.v2.port.Port`
        """
        return list(self._list(_port.Port, paginated=False, **query))

    def update_port(self, port, **params):
        """Update a port

        :param port: Either the id of a port or a
                     :class:`~ecl.network.v2.port.Port` instance.
        :param kwargs \*\*params: Parameters for Port update.

            * string admin_state_up: The admin state of port to update
            * array allowed_address_pairs: allowed address pairs
                e.g. [{"mac_address": <mac>, "ip_address": <ipv4/cidr>}]
            * string mac_address: The mac address of port to update
            * string description: The description of port to update
            * string device_id: The device id of port to update
            * string device_owner: The device owner of port to update
            * array fixed_ips: The fixed ips of port to update
                        e.g. [{"ip_address":<ipv4> , "subnet_id": <uuid> }, ]
            * string name: The name of port to update
            * int segmentation_id: The segmentation id of port to update
            * string segmentation_type: The segmentation type of port to update
            * dict tags: tags of port

        :returns: The updated port
        :rtype: :class:`~ecl.network.v2.port.Port`
        """
        if not isinstance(port, _port.Port):
            port = self._get_resource(_port.Port, port)
            port._body.clean()
        return self._update(_port.Port, port, **params)

    def get_physical_port(self, physical_port):
        """Get a single physical_port

        :param physical_port: The value can be the ID of a physical_port or a
                     :class:`~ecl.network.v2.physical_port.PhysicalPort` instance.

        :returns: One :class:`~ecl.network.v2.port.Port`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_physical_port.PhysicalPort, physical_port)

    def physical_ports(self, **query):
        """
        List all visible physical_ports.

        :param query: Query parameters to select results
        :return: A generator of physical_ports.
        :rtype: :class:`~ecl.network.v2.physical_port.PhysicalPort`
        """
        return list(self._list(_physical_port.PhysicalPort, **query))

    def get_quota(self, quota):
        """Get a quota

        :param quota: The value can be the ID of a quota or a
                      :class:`~ecl.network.v2.quota.Quota` instance.
                      The ID of a quota is the same as the tenant ID
                      for the quota.

        :returns: One :class:`~ecl.network.v2.quota.Quota`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_quota.Quota, quota)

    def create_subnet(self, network_id, cidr, allocation_pools=None,
                      description=None, dns_nameservers=None, enable_dhcp=None,
                      gateway_ip=None, host_routes=None, ip_version=4, name=None,
                      ntp_servers=None, tags=None):
        """Create a new subnet from attributes

        :param string network_id: ID of network that subnet belongs to.
        :param CIDR cidr: cidr of subnet to create
        :param array allocation_pools: allocation pools of subnet to create
        :param string description: description of subnet to create
        :param array dns_nameservers: dns nameservers of subnet to create
        :param bool enable_dhcp: bool value indicating if dhcp is enabled
        :param IPv4 gateway_ip: Gateway IP of subnet to create
        :param array host_routes: host routes of subnet to create
        :param Integer ip_version: support v4 only
        :param string name: name of subnet to create
        :param array ntp_servers: ntp servers of subnet to create
        :param dict tags: tags of subnet to create

        :returns: The results of subnet creation
        :rtype: :class:`~ecl.network.v2.subnet.Subnet`
        """

        body = {
            "network_id": network_id,
            "cidr": cidr,
            "enable_dhcp": enable_dhcp,
            "gateway_ip": gateway_ip
        }

        if allocation_pools:
            body.update({"allocation_pools": allocation_pools})
        if description:
            body.update({"description": description})
        if dns_nameservers:
            body.update({"dns_nameservers": dns_nameservers})
        if host_routes:
            body.update({"host_routes": host_routes})
        if ip_version:
            body.update({"ip_version": ip_version})
        if name:
            body.update({"name": name})
        if ntp_servers:
            body.update({"ntp_servers": ntp_servers})
        if tags:
            body.update({"tags": tags})

        return self._create(_subnet.Subnet, **body)

    def delete_subnet(self, subnet, ignore_missing=False):
        """Delete a subnet

        :param subnet: The value can be either the ID of a subnet or a
                       :class:`~ecl.network.v2.subnet.Subnet` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the subnet does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent subnet.

        :returns: ``None``
        """
        self._delete(_subnet.Subnet, subnet, ignore_missing=ignore_missing)

    def find_subnet(self, name_or_id, ignore_missing=False):
        """Find a single subnet

        :param name_or_id: The name or ID of a subnet.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.network.v2.subnet.Subnet` or None
        """
        return self._find(_subnet.Subnet, name_or_id,
                          ignore_missing=ignore_missing)

    def get_subnet(self, subnet):
        """Get a single subnet

        :param subnet: The value can be the ID of a subnet or a
                       :class:`~ecl.network.v2.subnet.Subnet` instance.

        :returns: One :class:`~ecl.network.v2.subnet.Subnet`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_subnet.Subnet, subnet)

    def subnets(self, **query):
        """Return a list of subnets

        :param query: Query parameters to select results
        :returns: A list of subnet objects
        :rtype: :class:`~ecl.network.v2.subnet.Subnet`
        """
        return list(self._list(_subnet.Subnet, paginated=False, **query))

    def update_subnet(self, subnet, **params):
        """Update a subnet

        :param subnet: Either the id of a subnet or a
                       :class:`~ecl.network.v2.subnet.Subnet` instance.
        :param \*\*params: Parameters for subnet update.

            * string description: description of subnet to create
            * array dns_nameservers: dns nameservers of subnet to create
            * bool enable_dhcp: bool value indicating if dhcp is enabled
            * IPv4 gateway_ip: Gateway IP of subnet to create
            * array host_routes: host routes of subnet to create
            * string name: name of subnet to create
            * array ntp_servers: ntp servers of subnet to create
            * dict tags: tags of subnet to create

        :returns: The updated subnet
        :rtype: :class:`~ecl.network.v2.subnet.Subnet`
        """
        if not isinstance(subnet, _subnet.Subnet):
            subnet = self._get_resource(_subnet.Subnet, subnet)
            subnet._body.clean()

        return self._update(_subnet.Subnet, subnet, **params)

    def reserved_addresses(self, **query):
        """Return a list of reserved addresses

        :returns: A list of reserved addresses objects
        :rtype: list of :class:`~ecl.network.v2.reserved_address.ReservedAddress`
        """
        return list(self._list(_reserved_address.ReservedAddress,
                               aginated=False, **query))

    def get_reserved_address(self, reserved_address):
        """Get a reserved address

        :param reserved_address: The value can be the ID of a reserved address or a
                      :class:`~ecl.network.v2.reserved_address.ReservedAddress` instance.

        :returns: One :class:`~ecl.network.v2.reserved_address.ReservedAddress`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_reserved_address.ReservedAddress, reserved_address)

    def firewalls(self, **query):
        """
        List all visible firewalls.

        :param query: Query parameters to select results
        :return: A generator of firewall instances.
        :rtype: :class:`~ecl.network.v2.firewall.Firewall`
        """
        return list(self._list(_firewall.Firewall, **query))

    def create_firewall(self, firewall_plan_id, availability_zone=None,
                        default_gateway=None, description=None, name=None):
        """
        Create firewall.

        :param firewall_plan_id: Firewall Plan ID.
        :param availability_zone: Get from
            `~ecl.compute.v2.availability_zone.AvailabilityZone`
        :param default_gateway: IP address of default gateway.
        :param description: Description of the Firewall.
        :param name: Name of the Firewall.
        :return: :class:`~ecl.network.v2.firewall.Firewall`
        """
        body = {"firewall_plan_id": firewall_plan_id}
        if availability_zone:
            body["availability_zone"] = availability_zone
        if default_gateway:
            body["default_gateway"] = default_gateway
        if description:
            body["description"] = description
        if name:
            body["name"] = name
        return self._create(_firewall.Firewall, **body)

    def get_firewall(self, firewall_id):
        """
        Get details for firewall.

        :param firewall_id: ID of specified firewall.
        :return: :class:`~ecl.network.v2.firewall.Firewall`
        """
        return self._get(_firewall.Firewall, firewall_id)

    def update_firewall(self, firewall_id, **params):
        """
        Update a specified firewall.

        :param firewall_id: ID of specified firewall.
        :param \*\*params: Parameters for firewall update.

            * default_gateway: IP address of default gateway.
            * description: Description of the Firewall.
            * firewall_plan_id: Firewall Plan ID.
            * name: Name of the Firewall.

        :return: :class:`~ecl.network.v2.firewall.Firewall`
        """
        firewall = _firewall.Firewall()
        return firewall.update(self.session, firewall_id, **params)

    def delete_firewall(self, firewall_id):
        """
        Delete a sepcified firewall.

        :param firewall_id: ID of specified firewall.
        :return: ``None``
        """
        return self._delete(_firewall.Firewall, firewall_id)

    def find_firewall(self, name_or_id, ignore_missing=False):
        """Find a single firewall

        :param name_or_id: The name or ID of a firewall.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.network.v2.firewall.Firewall` or None
        """
        return self._find(_firewall.Firewall, name_or_id,
                          ignore_missing=ignore_missing)

    def firewall_interfaces(self, **query):
        """
        List all visible firewall_interfaces.

        :param query: Query parameters to select results
        :return: A generator of FirewallInterface instances.
        :rtype: :class:`~ecl.network.v2.firewall_interface.FirewallInterface`
        """
        return list(self._list(_firewall_if.FirewallInterface, **query))

    def get_firewall_interface(self, firewall_interface_id):
        """
        Get details for firewall_interface.

        :param firewall_interface_id: ID of specified firewall_interface.
        :return: :class:`~ecl.network.v2.firewall_interface.FirewallInterface`
        """
        return self._get(_firewall_if.FirewallInterface,
                         firewall_interface_id)

    def update_firewall_interface(self, firewall_id,
                                  firewall_interface_id,
                                  **params):
        """
        Update firewall_interface.

        :param firewall_id: ID of parent firewall ID of firewall_interface.
        :param firewall_interface_id: ID of specified firewall_interface.
        :param params: Parameters for update.
        :return: :class:`~ecl.network.v2.firewall_interface.FirewallInterface`
        """
        interface = _firewall_if.FirewallInterface()
        return interface.update(self.session, firewall_id,
                                firewall_interface_id, **params)

    def firewall_plans(self, **query):
        """
        List all visible firewall_plans.

        :param query: Query parameters to select results
        :return: A generator of FirewallPlan instances.
        :rtype: :class:`~ecl.network.v2.firewall_plan.FirewallPlan`
        """
        return list(self._list(_firewall_plan.FirewallPlan, **query))

    def get_firewall_plan(self, firewall_plan_id):
        """
        Get details for firewall_plan.

        :param firewall_plan_id: Specified firewall plan id.
        :return: :class:`~ecl.network.v2.firewall_plan.FirewallPlan`
        """
        return self._get(_firewall_plan.FirewallPlan, firewall_plan_id)

    def find_firewall_plan(self, name_or_id, ignore_missing=False):
        """Find a firewall plan

        :param id_or_name: The name or ID of a firewall plan.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.compute.v2.firewall_plan.FirewallPlan` or None
        """
        return self._find(_firewall_plan.FirewallPlan, name_or_id,
                          ignore_missing=ignore_missing)

    def reboot_firewall(self, firewall_id, type):
        """
        Reboot Firewall.

        :param firewall_id: ID of specified firewall.
        :param type: Type to reboot firewall.
        :return: ``None``
        """
        action = _firewall_action.FirewallAction()
        return action.reboot(self.session, firewall_id, type)

    def reset_password_firewall(self, firewall_id, username):
        """
        Reset password of firewall instance.

        :param firewall_id: ID of specified firewall.
        :param username: Username to change the password.
        :return: :class:`~ecl.network.v2.firewall_action.FirewallAction`
        """
        action = _firewall_action.FirewallAction()
        return action.reset_password(self.session, firewall_id, username)

    def load_balancers(self, **query):
        """
        List all visible load_balancers.

        :param query: Query parameters to select results.
        :return: A generator of LoadBalancer instances.
        :rtype: :class:`~ecl.network.v2.load_balancer.LoadBalancer`
        """
        return list(self._list(_load_balancer.LoadBalancer, 
                               paginated=False, **query))

    def create_load_balancer(self, load_balancer_plan_id,
                             availability_zone=None, description=None,
                             name=None):
        """
        Create a load_balancer.

        :param load_balancer_plan_id: Load Balancer Plan.
        :param availability_zone: Availability Zone.
        :param description: Description of the Load Balancer.
        :param name: Name of the Load Balancer.
        :return: :class:`~ecl.network.v2.load_balancer.LoadBalancer`
        """
        body = {"load_balancer_plan_id": load_balancer_plan_id}
        if availability_zone:
            body["availability_zone"] = availability_zone
        if description:
            body["description"] = description
        if name:
            body["name"] = name
        return self._create(_load_balancer.LoadBalancer, **body)

    def get_load_balancer(self, load_balancer_id):
        """
        Get details for load_balancer.

        :param load_balancer_id: ID of load balancer.
        :return: :class:`~ecl.network.v2.load_balancer.LoadBalancer`
        """
        return self._get(_load_balancer.LoadBalancer, load_balancer_id)

    def delete_load_balancer(self, load_balancer_id):
        """
        Delete load_balancer.

        :param load_balancer_id: ID of load balancer.
        :return: :class:`~ecl.network.v2.load_balancer.LoadBalancer`
        """
        return self._delete(_load_balancer.LoadBalancer, load_balancer_id)

    def find_load_balancer(self, name_or_id, ignore_missing=False):
        """Find a single load_balancer

        :param name_or_id: The name or ID of a load_balancer.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.network.v2.load_balancer.LoadBalancer` or None
        """
        return self._find(_load_balancer.LoadBalancer,
                          name_or_id, ignore_missing=ignore_missing)

    def update_load_balancer(self, load_balancer_id, **params):
        """
        Update a specified firewall.

        :param load_balancer_id: ID of specified load balancer.
        :param \*\*params: Parameters for firewall update.

            * load_balancer_interface_id: ID for specified load_balancer_interface.
            * description: Description the Load Balancer Interface.
            * ip_address: IP Address.
            * name: Name the Load Balancer Interface.
            * network_id: Network ID.
            * virtual_ip_address: Virtual IP Address.
            * virtual_ip_properties: Properties used for virtual IP address.
                                     Available parameters include:
                * protocol: Redundancy Protocol. Enumeration is [‘vrrp’].
                            This parameter is optional.
                * vrid: VRRP group identifier. This parameter is optional.

        :return: :class:`~ecl.network.v2.load_balancer.LoadBalancer`
        """
        load_balancer = _load_balancer.LoadBalancer()
        return load_balancer.update(self.session, load_balancer_id, **params)

    def load_balancer_interfaces(self, **query):
        """
        List all visible load_balancer_interfaces.

        :param query: Query parameters to select results
        :return: A generator of LoadBalancerInterface instances.
        :rtype: :class:`~ecl.network.v2.load_balancer_interface.LoadBalancerInterface`
        """
        return list(self._list(_load_balancer_if.LoadBalancerInterface, **query))

    def get_load_balancer_interface(self, load_balancer_interface_id):
        """
        Get details for load_balancer_interface.

        :param load_balancer_interface_id: ID for specified load_balancer_interface.
        :return: :class:`~ecl.network.v2.load_balancer_interface.LoadBalancerInterface`
        """
        return self._get(_load_balancer_if.LoadBalancerInterface, load_balancer_interface_id)

    def update_load_balancer_interface(self, load_balancer_id,
                                       load_balancer_interface_id, **params):
        """
        Update load_balancer_interface.

        :param load_balancer_id: ID for parent load balancer of
                                 specified load_balancer_interface.
        :param load_balancer_interface_id: ID for specified
                                           load_balancer_interface.
        :param params: Parameters for update.
        :return:
        """
        interface = _load_balancer_if.LoadBalancerInterface()
        return interface.update(self.session, load_balancer_id,
                                load_balancer_interface_id, **params)

    def load_balancer_plans(self, **query):
        """
        List all visible load_balancer_plans.

        :param query: Query parameters to select results.
        :return: A generator of LoadBalancerPlan instances.
        :rtype: :class:`~ecl.network.v2.load_balancer_plan.LoadBalancerPlan`
        """
        return list(self._list(_load_balancer_plan.LoadBalancerPlan, **query))

    def get_load_balancer_plan(self, load_balancer_interface_id):
        """
        Get details for load_balancer_plan.

        :param load_balancer_interface_id: ID of specified load balancer plan.
        :return: :class:`~ecl.network.v2.load_balancer_plan.LoadBalancerPlan`
        """
        return self._get(_load_balancer_plan.LoadBalancerPlan, load_balancer_interface_id)

    def find_load_balancer_plan(self, name_or_id, ignore_missing=False):

        """Find a load_balancer plan

        :param id_or_name: The name or ID of a load balancer plan.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.compute.v2._load_balancer_plan.LoadBalancerPlan` or None
        """
        return self._find(_load_balancer_plan.LoadBalancerPlan, name_or_id,
                          ignore_missing=ignore_missing)

    def reboot_load_balancer(self, load_balancer_id, type):
        """
        Reboot Firewall.

        :param load_balancer_id: ID of specified load_balancer.
        :param type: Type to reboot firewall.
        :return: ``None``
        """
        action = _load_balancer_action.LoadBalancerAction()
        return action.reboot(self.session, load_balancer_id, type)

    def reset_password_load_balancer(self, load_balancer_id, username):
        """
        Reset password of load balancer instance.

        :param load_balancer_id: ID of specified load balancer.
        :param username: Username to change the password.
        :return: :class:`~ecl.network.v2.load_balancer_action.LoadBalancerAction`
        """
        action = _load_balancer_action.LoadBalancerAction()
        return action.reset_password(self.session, load_balancer_id, username)

    def load_balancer_syslog_servers(self, **query):
        """Return a list of Load Balancer Syslog Server

        :returns: A list of Load Balancer Syslog Server objects
        """
        return list(self._list(_load_balancer_syslog.LoadBalancerSyslogServer,
                               paginated=False, **query))

    def get_load_balancer_syslog_server(self, load_balancer_syslog_server):

        """Get a single Load Balancer Syslog Server

        :param load_balancer_syslog_server: The value can be the ID of
                        an Load Balancer Syslog Server or a
                        :class:`~ecl.network.v2.load_balancer_syslog_server.
                        LoadBalancerSyslogServer` instance.
        :returns: One :class:`~ecl.network.v2.load_balancer_syslog_server.
                  LoadBalancerSyslogServer`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_load_balancer_syslog.LoadBalancerSyslogServer,
                         load_balancer_syslog_server)

    def create_load_balancer_syslog_server(self, ip_address, load_balancer_id, name,
                                           acl_logging=None, appflow_logging=None,
                                           date_format=None, description=None,
                                           log_facility=None, log_level=None,
                                           port_number=None, priority=None,
                                           tcp_logging=None, tenant_id=None,
                                           time_zone=None, transport_type=None,
                                           user_configurable_log_messages=None):
        """Create a Load Balancer Syslog Server from properties

        :param string ip_address: IP address of the syslog server
        :param uuid load_balancer_id: ID of load balancer this syslog server belongs to
        :param string name: Name for syslog
        :param enumerate acl_logging: ["ENABLED", "DISABLED"]
        :param enumerate appflow_logging: ["ENABLED", "DISABLED"]
        :param enumerate date_format: ["DDMMYYYY", "MMDDYYYY", "YYYYMMDD"]
        :param string description: Description for syslog
        :param enumerate log_facility: ["LOCAL0", "LOCAL1", "LOCAL2",
                                        "LOCAL3", "LOCAL4", "LOCAL5",
                                        "LOCAL6", "LOCAL7"]
        :param string log_level: "ALL", "NONE", or one or more (join with "|") of
                                        ["ALERT", "CRITICAL", "NOTICE",
                                        "DEBUG", "ERROR", "WARNING", "EMERGENCY",
                                        "INFORMATIONAL"]
        :param int port_number: 1-65536
        :param int priority: 0-255
        :param enumerate tcp_logging: ["NONE", "ALL"]
        :param uuid tenant_id: Tenant ID of the owner
        :param enumerate time_zone: ["GMT_TIME", "LOCAL_TIME"]
        :param enumerate transport_type: ["UDP"]
        :param enumerate user_configurable_log_messages: ["YES", "NO"]

        :return: :class:`~ecl.network.v2.load_balancer_syslog_server.LoadBalancerSyslogServer`
        """
        body = {
            "ip_address": ip_address,
            "load_balancer_id": load_balancer_id,
            "name": name
        }
        if acl_logging is not None:
            body["acl_logging"] = acl_logging
        if appflow_logging is not None:
            body["appflow_logging"] = appflow_logging
        if date_format is not None:
            body["date_format"] = date_format
        if description is not None:
            body["description"] = description
        if log_facility is not None:
            body["log_facility"] = log_facility
        if log_level is not None:
            body["log_level"] = log_level
        if port_number is not None:
            body["port_number"] = port_number
        if priority is not None:
            body["priority"] = priority
        if tcp_logging is not None:
            body["tcp_logging"] = tcp_logging
        if tenant_id is not None:
            body["tenant_id"] = tenant_id
        if time_zone is not None:
            body["time_zone"] = time_zone
        if transport_type is not None:
            body["transport_type"] = transport_type
        if user_configurable_log_messages is not None:
            body["user_configurable_log_messages"] = user_configurable_log_messages
        return self._create(_load_balancer_syslog.LoadBalancerSyslogServer, **body)

    def update_load_balancer_syslog_server(self, load_balancer_syslog_server,
                                           acl_logging=None, appflow_logging=None,
                                           date_format=None, description=None,
                                           log_facility=None, log_level=None,
                                           priority=None, tcp_logging=None,
                                           time_zone=None,
                                           user_configurable_log_messages=None):
        """Update a Load Balancer Syslog Server from properties

        :param load_balancer_syslog_server: The value can be
                            either the ID of an Load Balancer Syslog Server or a
                                   :class:`~ecl.network.v2.load_balancer_syslog_server.
                                   LoadBalancerSyslogServer` instance.
        :param enumerate acl_logging: ["ENABLED", "DISABLED"]
        :param enumerate appflow_logging: ["ENABLED", "DISABLED"]
        :param enumerate date_format: ["DDMMYYYY", "MMDDYYYY", "YYYYMMDD"]
        :param string description: Description for syslog
        :param enumerate log_facility: ["LOCAL0", "LOCAL1", "LOCAL2",
                                        "LOCAL3", "LOCAL4", "LOCAL5",
                                        "LOCAL6", "LOCAL7"]
        :param string log_level: "ALL", "NONE", or one or more (join with "|") of
                                        ["ALERT", "CRITICAL", "NOTICE",
                                        "DEBUG", "ERROR", "WARNING", "EMERGENCY",
                                        "INFORMATIONAL"]
        :param int priority: 0-255
        :param enumerate tcp_logging: ["NONE", "ALL"]
        :param enumerate time_zone: ["GMT_TIME", "LOCAL_TIME"]
        :param enumerate user_configurable_log_messages: ["YES", "NO"]

        :return: :class:`~ecl.network.v2.load_balancer_syslog_server.LoadBalancerSyslogServer`
        """
        body = dict()
        if acl_logging is not None:
            body["acl_logging"] = acl_logging
        if appflow_logging is not None:
            body["appflow_logging"] = appflow_logging
        if date_format is not None:
            body["date_format"] = date_format
        if description is not None:
            body["description"] = description
        if log_facility is not None:
            body["log_facility"] = log_facility
        if log_level is not None:
            body["log_level"] = log_level
        if priority is not None:
            body["priority"] = priority
        if tcp_logging is not None:
            body["tcp_logging"] = tcp_logging
        if time_zone is not None:
            body["time_zone"] = time_zone
        if user_configurable_log_messages is not None:
            body["user_configurable_log_messages"] = user_configurable_log_messages
        if not isinstance(load_balancer_syslog_server,
                          _load_balancer_syslog.LoadBalancerSyslogServer):
            load_balancer_syslog_server = self._get_resource(
                        _load_balancer_syslog.LoadBalancerSyslogServer,
                        load_balancer_syslog_server
            )
            load_balancer_syslog_server._body.clean()
        return self._update(_load_balancer_syslog.LoadBalancerSyslogServer,
                            load_balancer_syslog_server, **body)

    def delete_load_balancer_syslog_server(self, load_balancer_syslog_server,
                                           ignore_missing=False):
        """Delete a load balancer syslog server

        :param load_balancer_syslog_server: The value can be
                either the ID of an Load Balancer Syslog Server or a
                       :class:`~ecl.network.v2.load_balancer_syslog_server.
                       LoadBalancerSyslogServer` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the Load Balancer Syslog Server does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent Load Balancer Syslog Server.
        :returns: ``None``
        """
        return self._delete(_load_balancer_syslog.LoadBalancerSyslogServer,
                            load_balancer_syslog_server,
                            ignore_missing=ignore_missing)

    def internet_services(self, **query):
        """Return a list of Internet Services

        :returns: A list of Internet Service objects
        """
        return list(self._list(_internet.InternetService, paginated=False, **query))

    def get_internet_service(self, internet_service):

        """Get a single Internet Service

        :param internet_service: The value can be the ID of an Internet Service or a
                       :class:`~ecl.network.v2.internet.InternetService` instance.

        :returns: One :class:`~ecl.network.v2.internet.InternetService`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_internet.InternetService, internet_service)

    def find_internet_service(self,name_or_id, ignore_missing=False):
        """Find a single internet_service

        :param name_or_id: The name or ID of an internet_service.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.network.v2.internet.InternetService` or None
        """
        return self._find(_internet.InternetService,
                          name_or_id, ignore_missing=ignore_missing)

    def internet_gateways(self, **query):
        """Return a list of Internet Gateways

        :param query: Query parameters to select results

        :returns: A list of Internet Gateway objects
        """
        return list(self._list(_internet.InternetGateway, paginated=False, **query))

    def get_internet_gateway(self, internet_gateway):

        """Get a single Internet Gateway

        :param internet_gateway: The value can be the ID of an Internet Gateway or a
                       :class:`~ecl.network.v2.internet.InternetGateway` instance.

        :returns: One :class:`~ecl.network.v2.internet.InternetGateway`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_internet.InternetGateway, internet_gateway)

    def create_internet_gateway(self, internet_service_id, qos_option_id,
                                name=None, description=None, tenant_id=None):
        """Create a new Internet Gateway from parameters.

        :param string internet_service_id: ID of Internet Service of gateway to create
        :param string qos_option_id: ID of QoS Option of gateway to create
        :param string name: name of gateway to create
        :param string description: description of gateway to create
        :param string tenant_id: ID of Tenant of gateway to create

        :return: One :class:`~ecl.network.v2.internet.InternetGateway`
        """
        body = {
            "internet_service_id": internet_service_id,
            "qos_option_id": qos_option_id
        }
        if name is not None:
            body.update({"name": name})
        if description is not None:
            body.update({"description": description})
        if tenant_id is not None:
            body.update({"tenant_id": tenant_id})

        return self._create(_internet.InternetGateway, **body)

    def update_internet_gateway(self, inet_gw, **body):
        """Update a new Internet Gateway from parameters.

        :param inet_gw: The value can be the ID of an Internet Gateway or a
                       :class:`~ecl.network.v2.internet.InternetGateway` instance.
        :param string name: name of gateway to update
        :param string description: description of gateway to update
        :param string qos_option_id: ID of QoS Option of gateway to update

        :return: result of update Internet Gateway
        :rtype :class:`~ecl.network.v2.internet.InternetGateway`

        """
        if not isinstance(inet_gw, _internet.InternetGateway):
            inet_gw = self._get_resource(_internet.InternetGateway, inet_gw)
            inet_gw._body.clean()
        return self._update(_internet.InternetGateway, inet_gw, **body)

    def delete_internet_gateway(self, inet_gw, ignore_missing=False):
        """Delete an Internet Gateway

        :param inet_gw: The value can be either the ID of an Internet Gateway or a
                       :class:`~ecl.network.v2.internet.InternetGateway` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the Internet Gateway does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent Internet Gateway.

        :returns: ``None``
        """
        return self._delete(_internet.InternetGateway, inet_gw,
                            ignore_missing=ignore_missing)

    def find_internet_gateway(self, name_or_id, ignore_missing=False):
        """Find a single internet_gateway

        :param name_or_id: The name or ID of an internet_gateway.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.network.v2.internet.InternetGateway` or None
        """
        return self._find(_internet.InternetGateway,
                          name_or_id, ignore_missing=ignore_missing)

    def qos_options(self, **query):
        """Return a list of QoS Options

        :returns: A list of QoS Option objects
        """
        return list(self._list(_qos_option.QosOption, paginated=False,
                               **query))

    def get_qos_option(self, qos_option):
        """Get a single QoS Option

        :param qos_option: The value can be the ID of a QoS Option or a
                       :class:`~ecl.network.v2.qos_option.QoSOption` instance.

        :returns: One :class:`~ecl.network.v2.qos_option.QoSOption`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_qos_option.QosOption, qos_option)

    def find_qos_option(self, name_or_id, ignore_missing=False):
        """Find a single qos_option

        :param name_or_id: The name or ID of a qos_option.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.network.v2.qos_option.QosOption` or None
        """
        return self._find(_qos_option.QosOption,
                          name_or_id, ignore_missing=ignore_missing)

    def public_ips(self, **query):
        """Return a list of Public IPs

        :param query: Query parameters to select results

        :returns: A list of Public IP objects
        """
        return list(self._list(_publicip.PublicIP, paginated=False, **query))

    def get_public_ip(self, publicip):
        """Get a single Public IP

        :param publicip: The value can be the ID of a Public IP or a
                       :class:`~ecl.network.v2.publicip.PublicIP` instance.

        :returns: One :class:`~ecl.network.v2.publicip.PublicIP`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_publicip.PublicIP, publicip)

    def create_public_ip(self, internet_gw_id, submask_length,
                         description=None, name=None, tenant_id=None):
        """Create a Public IP from parameters

        :param string internet_gw_id: ID of Internet Gateway to create public ip
        :param int submask_length: submask length to create public ip pool with
        :param string description: description of public ip to create
        :param string name: name of public ip to create
        :param string tenant_id: tenant ID of public ip

        :return: One :class:`~ecl.network.v2.publicip.PublicIP`
        """

        body = {"internet_gw_id": internet_gw_id,
                "submask_length": submask_length}
        if description:
            body.update({"description": description})
        if name:
            body.update({"name": name})
        if tenant_id:
            body.update({"tenant_id": tenant_id})
        return self._create(_publicip.PublicIP, **body)

    def update_public_ip(self, public_ip, **body):
        """Update a Public IP

        :param public_ip:  The value can be the ID of a Public IP or a
                       :class:`~ecl.network.v2.publicip.PublicIP` instance.
        :param description: description of public ip to update

        :returns: The result of update Public IP
        :rtype: :class:`~ecl.network.v2.publicip.PublicIP`
        """
        if not isinstance(public_ip, _publicip.PublicIP):
            public_ip = self._get_resource(_publicip.PublicIP, public_ip)
            public_ip._body.clean()
        return self._update(_publicip.PublicIP, public_ip, **body)

    def delete_public_ip(self, publicip, ignore_missing=False):
        """Delete a Public Ip

        :param publicip: The value can be either the ID of a Public IP or a
                       :class:`~ecl.network.v2.publicip.PublicIP` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the Public IP does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent Public IP.

        :return: One :class:`~ecl.network.v2.publicip.PublicIP`
        """
        return self._delete(_publicip.PublicIP, publicip,
                            ignore_missing=ignore_missing)

    def gateway_interfaces(self, **query):
        """Return a list of Gateway Interfaces

        :returns: A list of Gateway Interface objects
        """
        return list(self._list(_gwif.GatewayInterface, paginated=False,
                               **query))

    def get_gateway_interface(self, gw_interface):
        """Get a single Gateway Interface

        :param gw_interface: The value can be the ID of a Gateway Interface or a
                       :class:`~ecl.network.v2.gw_interface.GatewayInterface` instance.

        :returns: One :class:`~ecl.network.v2.gw_interface.GatewayInterface`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_gwif.GatewayInterface, gw_interface)

    def create_gateway_interface(self, service_type, network_id, netmask,
                                 primary_ipv4, secondary_ipv4, gw_vipv4, vrid,
                                 name=None, description=None,
                                 primary_ipv6=None, secondary_ipv6=None,
                                 gw_vipv6=None, interdc_gw_id=None,
                                 internet_gw_id=None,
                                 vpn_gw_id=None, aws_gw_id=None, gcp_gw_id=None,
                                 azure_gw_id=None, fic_gw_id=None, tenant_id=None):
        """Create a Gateway Interface from parameters

        :param string service_type: service type of gateway interface to create
        :param string network_id: network ID of gateway interface to create
        :param int netmask: netmask of gateway interface to create
        :param IPv4 primary_ipv4: primary IPv4 of gateway interface to create
        :param IPv4 secondary_ipv4: secondary IPv4 of gateway interface to create
        :param IPv4 gw_vipv4: gateway virtual IPv4 interface to create
        :param int vrid: ID of VRRP of gateway interface to create
        :param string name: name of gateway interface to create
        :param string description: description of gateway interface to create
        :param IPv6 primary_ipv6: primary IPv6 of gateway interface to create
        :param IPv6 secondary_ipv6: secondary IPv6 of gateway interface to create
        :param IPv6 gw_vipv6: gateway virtual IPv6 of gateway interface to create
        :param string interdc_gw_id: InterDC Gateway ID of gateway interface to create
        :param string internet_gw_id: Internet Gateway ID of gateway interface to create
        :param string vpn_gw_id: VPN Gateway ID of gateway interface to create
        :param string fic_gw_id: FIC Gateway ID of gateway interface to create
        :param string tenant_id: tenant ID of gateway interface to create

        :returns: The results of GatewayInterface creation
        :rtype: One :class:`~ecl.network.v2.gwif.GatewayInterface`
        """
        body = {
            "service_type": service_type,
            "network_id": network_id,
            "netmask": netmask,
            "primary_ipv4": primary_ipv4,
            "secondary_ipv4": secondary_ipv4,
            "gw_vipv4": gw_vipv4,
            "vrid": vrid
        }
        if name:
            body.update({"name": name})
        if description:
            body.update({"description": description})
        if primary_ipv6:
            body.update({"primary_ipv6": primary_ipv6})
        if secondary_ipv6:
            body.update({"secondary_ipv6": secondary_ipv6})
        if gw_vipv6:
            body.update({"gw_vipv6": gw_vipv6})
        if interdc_gw_id:
            body.update({"interdc_gw_id": interdc_gw_id})
        if internet_gw_id:
            body.update({"internet_gw_id": internet_gw_id})
        if vpn_gw_id:
            body.update({"vpn_gw_id": vpn_gw_id})
        if aws_gw_id:
            body.update({"aws_gw_id": aws_gw_id})
        if gcp_gw_id:
            body.update({"gcp_gw_id": gcp_gw_id})
        if azure_gw_id:
            body.update({"azure_gw_id": azure_gw_id})
        if fic_gw_id:
            body.update({"fic_gw_id": fic_gw_id})
        if tenant_id:
            body.update({"tenant_id": tenant_id})

        return self._create(_gwif.GatewayInterface, **body)

    def update_gateway_interface(self, gw_interface, **body):
        """Update a Gateway Interface

        :param gw_interface:  The value can be the ID of a Gateway Interface or a
                       :class:`~ecl.network.v2.gw_interface.GatewayInterface` instance.
        :param name: name of gateway interface to update
        :param description: description of gateway interface to update

        :returns: The result of update Gateway Interface
        :rtype: :class:`~ecl.network.v2.gw_interface.GatewayInterface`
        """
        if not isinstance(gw_interface, _gwif.GatewayInterface):
            gw_interface = self._get_resource(_gwif.GatewayInterface, gw_interface)
            gw_interface._body.clean()
        return self._update(_gwif.GatewayInterface, gw_interface, **body)

    def delete_gateway_interface(self, gwif, ignore_missing=False):
        """Delete a Gateway Interface

        :param gwif: The value can be either the ID of a Gateway Interface or a
                       :class:`~ecl.network.v2.gwif.GatewayInterface` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the Gateway Interface does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent Gateway Interface.

        :return: One :class:`~ecl.network.v2.gwif.GatewayInterface`
        """
        return self._delete(_gwif.GatewayInterface, gwif,
                            ignore_missing=ignore_missing)

    def find_gateway_interface(self, name_or_id, ignore_missing=False):
        """Find a single gateway_interface

        :param name_or_id: The name or ID of a common_function_gatway.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.network.v2.gwif.GatewayInterface` or None
        """
        return self._find(_gwif.GatewayInterface,
                          name_or_id, ignore_missing=ignore_missing)

    def static_routes(self, **query):
        """Return a list of Static Routes

        :returns: A list of Static Route objects
        """
        return list(self._list(_static_route.StaticRoute, paginated=False,
                               **query))

    def get_static_route(self, static_route):
        """Get a single Static Route

        :param static_route: The value can be the ID of a  Static Route or a
                       :class:`~ecl.network.v2.static_route.StaticRoute` instance.

        :returns: One :class:`~ecl.network.v2.static_route.StaticRoute`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_static_route.StaticRoute, static_route)

    def create_static_route(self, service_type, destination, nexthop,
                            name=None, description=None,interdc_gw_id=None,
                            internet_gw_id=None, vpn_gw_id=None, aws_gw_id=None,
                            gcp_gw_id=None, azure_gw_id=None, fic_gw_id=None, tenant_id=None):
        """Create a Static Route

        :param service_type: service type of static route to create
        :param destination: destination of static route to create
        :param nexthop: next hop of static route to create
        :param name: name of static route to create
        :param description: description of static route to create
        :param interdc_gw_id: InterDC Gateway ID of static route to create
        :param internet_gw_id: Internet Gateway ID of static route to create
        :param vpn_gw_id: VPN Gateway ID of static route to create
        :param fic_gw_id: FIC Gateway ID of static route to create
        :param tenant_id: tenant ID of static route to create

        :return: The results of StaticRoute creation
        :rtype:  One :class:`~ecl.network.v2.staticroute.StaticRoute`
        """
        body = {
            "service_type": service_type,
            "destination": destination,
            "nexthop": nexthop
        }
        if name:
            body.update({"name": name})
        if description:
            body.update({"description": description})
        if interdc_gw_id:
            body.update({"interdc_gw_id": interdc_gw_id})
        if internet_gw_id:
            body.update({"internet_gw_id": internet_gw_id})
        if vpn_gw_id:
            body.update({"vpn_gw_id": vpn_gw_id})
        if aws_gw_id:
            body.update({"aws_gw_id": aws_gw_id})
        if gcp_gw_id:
            body.update({"gcp_gw_id": gcp_gw_id})
        if azure_gw_id:
            body.update({"azure_gw_id": azure_gw_id})
        if fic_gw_id:
            body.update({"fic_gw_id": fic_gw_id})
        if tenant_id:
            body.update({"tenant_id": tenant_id})

        return self._create(_static_route.StaticRoute, **body)

    def update_static_route(self, static_route, **body):
        """Update a Static Route

        :param static_route:  The value can be the ID of a Static Route or a
                       :class:`~ecl.network.v2.static_route.StaticRoute` instance.
        :param name: name of static route to update
        :param description: description of static route to update

        :returns: The result of update Static Route
        :rtype: :class:`~ecl.network.v2.static_route.StaticRoute`
        """
        if not isinstance(static_route, _static_route.StaticRoute):
            static_route = self._get_resource(_static_route.StaticRoute, static_route)
            static_route._body.clean()
        return self._update(_static_route.StaticRoute, static_route, **body)

    def delete_static_route(self, static_route, ignore_missing=False):
        """Delete a Static Route

        :param static_route: The value can be either the ID of a Static Route or a
                       :class:`~ecl.network.v2.static_route.StaticRoute` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the Static Route does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent Static Route.

        :return: One :class:`~ecl.network.v2.static_route.StaticRoute`
        """
        return self._delete(_static_route.StaticRoute, static_route,
                            ignore_missing=ignore_missing)

    def vpn_services(self, **query):
        """Return a list of VPN Service

        :returns: A list of VPN Service objects
        """
        return list(self._list(_vpn.VPNService, paginated=False,
                               **query))

    def get_vpn_service(self, vpn_service):

        """Get a single VPN Service

        :param vpn_service: The value can be the ID of a VPN Service or a
                       :class:`~ecl.network.v2.vpn.VPNService` instance.

        :returns: One :class:`~ecl.network.v2.vpn.VPNService`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_vpn.VPNService, vpn_service)

    def vpn_gateways(self, **query):
        """Return a list of VPN Gateways

        :param query: Query parameters to select results

        :returns: A list of VPN Gateway objects
        """
        return list(self._list(_vpn.VPNGateway, paginated=False, **query))

    def get_vpn_gateway(self, vpn_gateway):

        """Get a single VPN Gateway

        :param vpn_gateway: The value can be the ID of a VPN Gateway or a
                       :class:`~ecl.network.v2.vpn.VPNGateway` instance.

        :returns: One :class:`~ecl.network.v2.vpn.VPNGateway`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_vpn.VPNGateway, vpn_gateway)

    def find_vpn_gateway(self, name_or_id, ignore_missing=False):
        """Find a single vpn_gateway

        :param name_or_id: The name or ID of a vpn_gateway.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.network.v2.vpn.VPNGateway` or None
        """
        return self._find(_vpn.VPNGateway,
                          name_or_id, ignore_missing=ignore_missing)

    def vpn_interfaces(self, **query):
        """Return a list of VPN Interface

        :returns: A list of VPN Interface objects
        """
        return list(self._list(_vpn.VPNInterface, paginated=False,
                               *query))

    def get_vpn_interface(self, vpn_interface):

        """Get a single VPN Gateway

        :param vpn_interface: The value can be the ID of a VPN Interface or a
                       :class:`~ecl.network.v2.vpn.VPNInterface` instance.

        :returns: One :class:`~ecl.network.v2.vpn.VPNInterface`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_vpn.VPNInterface, vpn_interface)

    def interdc_services(self, **query):
        """Return a list of InterDC Service

        :returns: A list of InterDC Service objects
        """
        return list(self._list(_interdc.InterDCService, paginated=False,
                               **query))

    def get_interdc_service(self, interdc_service):

        """Get a single InterDC Service

        :param interdc_service: The value can be the ID of an InterDC Service or a
                       :class:`~ecl.network.v2.vpn.InterDCService` instance.

        :returns: One :class:`~ecl.network.v2.interdc.InterDCService`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_interdc.InterDCService, interdc_service)

    def interdc_gateways(self, **query):
        """Return a list of InterDC Gateways

        :param query: Query parameters to select results

        :returns: A list of InterDC Gateway objects
        """
        return list(self._list(_interdc.InterDCGateway, paginated=False, **query))

    def get_interdc_gateway(self, interdc_gateway):

        """Get a single InterDC Gateway

        :param interdc_gateway: The value can be the ID of an InterDC Gateway or a
                       :class:`~ecl.network.v2.interdc.InterDCGateway` instance.

        :returns: One :class:`~ecl.network.v2.interdc.InterDCGateway`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_interdc.InterDCGateway, interdc_gateway)

    def find_interdc_gateway(self, name_or_id, ignore_missing=False):
        """Find a single interdc_gateway

        :param name_or_id: The name or ID of an interdc_gateway.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.network.v2.interdc.InternetDC` or None
        """
        return self._find(_interdc.InterDCGateway,
                          name_or_id, ignore_missing=ignore_missing)

    def interdc_interfaces(self, **query):
        """Return a list of InterDC Interface

        :returns: A list of InterDC Interface objects
        """
        return list(self._list(_interdc.InterDCInterface, paginated=False,
                               **query))

    def get_interdc_interface(self, interdc_interface):

        """Get a single InterDC Gateway

        :param interdc_interface: The value can be the ID of an InterDC Interface or a
                       :class:`~ecl.network.v2.interdc.InterDCInterface` instance.

        :returns: One :class:`~ecl.network.v2.interdc.InterDCInterface`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_interdc.InterDCInterface, interdc_interface)

    def create_interdc_interface(self,  interdc_gw_id, netmask,
                                 primary_ipv4, secondary_ipv4, gw_vipv4, vrid,
                                 name=None, description=None,
                                 primary_ipv6=None, secondary_ipv6=None,
                                 gw_vipv6=None, tenant_id=None):
        """Create an InterDC Interface from parameters

        :param string interdc_gw_id: ID of InterDC interface to create
        :param int netmask: netmask of InterDC interface to create
        :param IPv4 primary_ipv4: primary IPv4 of InterDC interface to create
        :param IPv4 secondary_ipv4: secondary IPv4 of InterDC interface to create
        :param IPv4 gw_vipv4: InterDC virtual IPv4 interface to create
        :param int vrid: ID of VRRP of InterDC interface to create
        :param string name: name of InterDC interface to create
        :param string description: description of InterDC interface to create
        :param IPv6 primary_ipv6: primary IPv6 of InterDC interface to create
        :param IPv6 secondary_ipv6: secondary IPv6 of InterDC interface to create
        :param IPv6 gw_vipv6: InterDC virtual IPv6 of InterDC interface to create
        :param string tenant_id: tenant ID of InterDC interface to create

        :returns: The results of InterDCInterface creation
        :rtype: One :class:`~ecl.network.v2.interdc.InterDCInterface`
        """
        body = {
            "interdc_gw_id": interdc_gw_id,
            "netmask": netmask,
            "primary_ipv4": primary_ipv4,
            "secondary_ipv4": secondary_ipv4,
            "gw_vipv4": gw_vipv4,
            "vrid": vrid
        }
        if name:
            body.update({"name": name})
        if description:
            body.update({"description": description})
        if primary_ipv6:
            body.update({"primary_ipv6": primary_ipv6})
        if secondary_ipv6:
            body.update({"secondary_ipv6": secondary_ipv6})
        if gw_vipv6:
            body.update({"gw_vipv6": gw_vipv6})
        if tenant_id:
            body.update({"tenant_id": tenant_id})

        return self._create(_interdc.InterDCInterface, **body)

    def update_interdc_interface(self, interdc_interface, **body):
        """Update an InterDC Interface from parameters

        :param interdc_interface: ID of InterDC interface to update
        :param name: name of InterDC interface to update
        :param description: description of InterDC interface to update

        :returns: The results of InterDCInterface update
        :rtype: One :class:`~ecl.network.v2.interdc.InterDCInterface`
        """
        if not isinstance(interdc_interface, _interdc.InterDCInterface):
            interdc_interface = self._get_resource(_interdc.InterDCInterface, interdc_interface)
            interdc_interface._body.clean()

        return self._update(_interdc.InterDCInterface, interdc_interface, **body)

    def delete_interdc_interface(self, interdc_interface, ignore_missing=False):
        """Delete an InterDC Interface

        :param gwif: The value can be either the ID of an InterDC Interface or a
                       :class:`~ecl.network.v2.gwif.InterDCInterface` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the InterDC Interface does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent InterDC Interface.

        :return: One :class:`~ecl.network.v2.interdc.InterDCInterface`
        """
        return self._delete(_interdc.InterDCInterface, interdc_interface,
                            ignore_missing=ignore_missing)

    def common_function_pools(self, **query):
        """Return a list of common_function_pools

        :returns: A list of common_function_pool objects
        :rtype: list of :class:`~ecl.network.v2.common_function_pool.CommonFunctionPool`
        """
        return list(self._list(_common_function_pool.CommonFunctionPool,
                               paginated=False, **query))

    def get_common_function_pool(self, common_function_pool):
        """Get a single common_function_pool

        :param common_function_pool:
            The value can be the ID of a common_function_pool or a
            :class:`~ecl.network.v2.common_function_pool.CommonFunctionPool` instance.

        :returns: One :class:`~ecl.network.v2.common_function_pool.CommonFunctionPool`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_common_function_pool.CommonFunctionPool,
                         common_function_pool)

    def find_common_function_pool(self, name_or_id, ignore_missing=False):
        """Find a single common_function_pool

        :param name_or_id: The name or ID of a common_function_pool.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.network.v2.common_function_pool.CommonFunctionPool` or None
        """
        return self._find(_common_function_pool.CommonFunctionPool,
                          name_or_id, ignore_missing=ignore_missing)

    def common_functions(self, **query):
        """Return a list of common_functions

        :param query: Query parameters to select results.
        :returns: A list of common_functions objects
        :rtype: list of :class:`~ecl.network.v2.common_function.CommonFunction`
        """
        return list(self._list(_common_function.CommonFunction,
                               paginated=False, **query))

    def get_common_function(self, common_function):
        """Get a single common_function

        :param common_function:
            The value can be the ID of a common_function or a
            :class:`~ecl.network.v2.common_function.CommonFunction` instance.

        :returns: One :class:`~ecl.network.v2.common_function.CommonFunction`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_common_function.CommonFunction,
                         common_function)

    def find_common_function(self, name_or_id, ignore_missing=False):
        """Find a single common_function

        :param name_or_id: The name or ID of a common_function_gatway.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.network.v2.common_function.CommonFunction` or None
        """
        return self._find(_common_function.CommonFunction,
                          name_or_id, ignore_missing=ignore_missing)

    def common_function_gateways(self, **query):
        """Return a list of common_function_gateways

        :param query: Query parameters to select results.
        :returns: A list of common_function_gateways objects
        :rtype: list of :class:`~ecl.network.v2.common_function_gateway.CommonFunctionGateway`
        """
        return list(self._list(_common_function_gateway.CommonFunctionGateway,
                               paginated=False, **query))

    def get_common_function_gateway(self, common_function_gateway):
        """Get a single common_function_gateway

        :param common_function_gateway:
            The value can be the ID of a common_function_gateway or a
            :class:`~ecl.network.v2.common_function_gateway.CommonFunctionGateway` instance.

        :returns: One :class:`~ecl.network.v2.common_function_gateway.CommonFunctionGateway`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_common_function_gateway.CommonFunctionGateway,
                         common_function_gateway)

    def create_common_function_gateway(self, common_function_pool_id,
                                       description=None, name=None):
        """Create a new common_function_gateway from attributes

        :param string common_function_pool_id: Common Function Pool instantiated
            by this Gateway.
        :param string description: Description of the Common Function Pool
            Gateway resource.
        :param string name: Name of the Common Function Pool Gateway resource.

        :returns: The results of common_function_gateway creation
        :rtype: :class:`~ecl.network.v2.common_function_gateway.CommonFunctionGateway`
        """
        body = {"common_function_pool_id" :common_function_pool_id}
        if description:
            body["description"] = description
        if name:
            body["name"] = name
        return self._create(_common_function_gateway.CommonFunctionGateway,
                            **body)

    def update_common_function_gateway(self, common_function_gateway,
                                       **params):
        """Update a common_function_gateway

        :param common_function_gateway: The value can be the ID
            of a common_function_gateway or
            a :class:`~ecl.network.v2.common_function_gateway.CommonFunctionGateway` instance.

        :param kwargs \*\*params: Parameter for Common Function Gateway update.
            * description: Description of the Common Function Pool Gateway
                           resource.
            * name: Name of the Common Function Pool Gateway resource.

        :returns: The result of update common_function_gateway.
        :rtype: :class:`~ecl.network.v2.common_function_gateway.CommonFunctionGateway`
        """
        if not isinstance(common_function_gateway,
            _common_function_gateway.CommonFunctionGateway):
            common_function_gateway = \
                self._get_resource(_common_function_gateway.CommonFunctionGateway,
                    common_function_gateway)
            common_function_gateway._body.clean()
        return self._update(_common_function_gateway.CommonFunctionGateway,
                            common_function_gateway, **params)

    def delete_common_function_gateway(self, common_function_gateway,
                                       ignore_missing=False):
        """Delete a common_function_gateway

        :param common_function_gateway: The value can be either the ID
            of a common_function_gateway Interface or a
            :class:`~ecl.network.v2.common_function_gateway.CommonFunctionGateway` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the common_function_gateway Interface does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent common_function_gateway Interface.

        :return: One :class:`~ecl.network.v2.common_function_gateway.CommonFunctionGateway`
        """
        self._delete(_common_function_gateway.CommonFunctionGateway,
                     common_function_gateway, ignore_missing=ignore_missing)

    def find_common_function_gateway(self, name_or_id, ignore_missing=False):
        """Find a single common_function_gateway

        :param name_or_id: The name or ID of a common_function_gatway.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.network.v2.common_function_gateway.CommonFunctionGateway` or None
        """
        return self._find(_common_function_gateway.CommonFunctionGateway,
                          name_or_id, ignore_missing=ignore_missing)

    def colocation_spaces(self, **query):
        """Return a list of colocation_spaces

        :param query: Query parameters to select results.
        :returns: A list of colocation_spaces objects
        :rtype: list of :class:`~ecl.network.v2.colocation_space.ColocationSpace`
        """
        return list(self._list(_colocation_space.ColocationSpace,
                               paginated=False, **query))

    def get_colocation_space(self, colocation_space):
        """Get a single colocation_space

        :param colocation_space:
            The value can be the ID of a colocation_space or a
            :class:`~ecl.network.v2.colocation_space.ColocationSpace` instance.

        :returns: One :class:`~ecl.network.v2.colocation_space.ColocationSpace`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_colocation_space.ColocationSpace,
                         colocation_space)

    def colocation_physical_links(self, **query):
        """Return a list of colocation_physical_links

        :param query: Query parameters to select results.
        :returns: A list of colocation_physical_links objects
        :rtype: list of :class:`~ecl.network.v2.colocation_physical_link.ColocationPhysicalLink`
        """
        return list(self._list(_colocation_physical_link.ColocationPhysicalLink,
                               paginated=False, **query))

    def get_colocation_physical_link(self, colocation_physical_link):
        """Get a single colocation_physical_link

        :param colocation_physical_link:
            The value can be the ID of a colocation_physical_link or a
            :class:`~ecl.network.v2.colocation_physical_link.ColocationPhysicalLink` instance.

        :returns: One :class:`~ecl.network.v2.colocation_physical_link.ColocationPhysicalLink`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_colocation_physical_link.ColocationPhysicalLink,
                         colocation_physical_link)

    def colocation_logical_links(self, **query):
        """Return a list of colocation_logical_links

        :param query: Query parameters to select results.
        :returns: A list of colocation_logical_links objects
        :rtype: list of :class:`~ecl.network.v2.colocation_logical_link.ColocationLogicalLink`
        """
        return list(self._list(_colocation_logical_link.ColocationLogicalLink,
                               paginated=False, **query))

    def get_colocation_logical_link(self, colocation_logical_link):
        """Get a single colocation_logical_link

        :param colocation_logical_link:
            The value can be the ID of a colocation_logical_link or a
            :class:`~ecl.network.v2.colocation_logical_link.ColocationLogicalLink` instance.

        :returns: One :class:`~ecl.network.v2.colocation_logical_link.ColocationLogicalLink`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_colocation_logical_link.ColocationLogicalLink,
                         colocation_logical_link)

    def create_colocation_logical_link(self, colocation_physical_link_id,
                                       network_id, vlan_id, description=None,
                                       name=None, tags=None):
        """Create a new colocation_logical_link from attributes

        :param string colocation_physical_link_id: Colocation Physical Link ID.
        :param string network_id: Network connected to this link.
        :param string vlan_id: Logical port vlan id.
        :param string description: Colocation Logical Link description.
        :param string name: Colocation Logical Link name.
        :param dict tags: Colocation Logical Link tags.

        :returns: The results of colocation_logical_link creation
        :rtype: :class:`~ecl.network.v2.colocation_logical_link.ColocationLogicalLink`
        """
        body = {
            "colocation_physical_link_id": colocation_physical_link_id,
            "network_id": network_id,
            "vlan_id": vlan_id
        }
        if description:
            body["description"] = description
        if name:
            body["name"] = name
        if tags:
            body["tags"] = tags
        return self._create(_colocation_logical_link.ColocationLogicalLink,
                            **body)

    def update_colocation_logical_link(self, colocation_logical_link,
                                       **params):
        """Update a colocation_logical_link

        :param colocation_logical_link: The value can be the ID
            of a colocation_logical_link or
            a :class:`~ecl.network.v2.colocation_logical_link.ColocationLogicalLink` instance.
        :param kwargs \*\*params: Parameters for Colocation Logical Link update.

            * string description: Colocation Logical Link description.
            * string name: Colocation Logical Link name.
            * dict tags: Colocation Logical Link tags.

        :returns: The result of update colocation_logical_link.
        :rtype: :class:`~ecl.network.v2.colocation_logical_link.ColocationLogicalLink`
        """
        if not isinstance(colocation_logical_link,
            _colocation_logical_link.ColocationLogicalLink):
            colocation_logical_link = \
                self._get_resource(_colocation_logical_link.ColocationLogicalLink,
                    colocation_logical_link)
            colocation_logical_link._body.clean()
        return self._update(_colocation_logical_link.ColocationLogicalLink,
                            colocation_logical_link, **params)

    def delete_colocation_logical_link(self, colocation_logical_link,
                                       ignore_missing=False):
        """Delete a colocation_logical_link

        :param colocation_logical_link: The value can be either the ID
            of a colocation_logical_link Interface or a
            :class:`~ecl.network.v2.colocation_logical_link.ColocationLogicalLink` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the colocation_logical_link Interface does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent colocation_logical_link Interface.

        :return: One :class:`~ecl.network.v2.colocation_logical_link.ColocationLogicalLink`
        """
        self._delete(_colocation_logical_link.ColocationLogicalLink,
                     colocation_logical_link, ignore_missing=ignore_missing)

    def aws_services(self, **params):
        """Return a list of aws_services

        :param params: The parameters as query string
                       to get aws_services by specified condition.
        :returns: A list of aws_services objects
        :rtype: list of :class:`~ecl.network.v2.aws.AWSService`
        """
        return list(self._list(_aws.AWSService, paginated=False, **params))

    def get_aws_service(self, aws_service):
        """Get a single aws_service

        :param aws_service:
            The value can be the ID of a aws_service or a
            :class:`~ecl.network.v2.aws.AWSService` instance.

        :returns: One :class:`~ecl.network.v2.aws.AWSService`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_aws.AWSService, aws_service)

    def find_aws_service(self, name_or_id, ignore_missing=False):
        """Find a single aws_service

        :param name_or_id: The name or ID of a aws_service.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.network.v2.aws.AWSService` or None
        """
        return self._find(_aws.AWSService, name_or_id,
                          ignore_missing=ignore_missing)

    def aws_gateways(self, **params):
        """Return a list of aws_gateways
        :param params: The parameters as query string
                       to get aws_gateways by specified condition.
        :returns: A list of aws_gateways objects
        :rtype: list of :class:`~ecl.network.v2.aws.AWSGateway`
        """
        return list(self._list(_aws.AWSGateway, paginated=False, **params))

    def get_aws_gateway(self, aws_gateway):
        """Get a single aws_gateway

        :param aws_gateway:
            The value can be the ID of a aws_gateway or a
            :class:`~ecl.network.v2.aws.AWSGateway` instance.

        :returns: One :class:`~ecl.network.v2.aws.AWSGateway`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_aws.AWSGateway, aws_gateway)

    def find_aws_gateway(self, name_or_id, ignore_missing=False):
        """Find a single aws_gateway

        :param name_or_id: The name or ID of a aws_gateway.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.network.v2.aws.AWSGateway` or None
        """
        return self._find(_aws.AWSGateway, name_or_id,
                          ignore_missing=ignore_missing)

    def aws_interfaces(self, **params):
        """Return a list of aws_interfaces

        :param params: The parameters as query string
                       to get aws_interfaces by specified condition.
        :returns: A list of aws_interfaces objects
        :rtype: list of :class:`~ecl.network.v2.aws.AWSInterface`
        """
        return list(self._list(_aws.AWSInterface, paginated=False, **params))

    def get_aws_interface(self, aws_interface):
        """Get a single aws_interface

        :param aws_interface:
            The value can be the ID of a aws_interface or a
            :class:`~ecl.network.v2.aws.AWSInterface` instance.

        :returns: One :class:`~ecl.network.v2.aws.AWSInterface`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_aws.AWSInterface, aws_interface)

    def find_aws_interface(self, name_or_id, ignore_missing=False):
        """Find a single aws_interface

        :param name_or_id: The name or ID of a aws_interface.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.network.v2.aws.AWSInterface` or None
        """
        return self._find(_aws.AWSInterface, name_or_id,
                          ignore_missing=ignore_missing)

    def tenant_connections(self, **query):
        """Return a list of tenant_connections

        :param query:  Query parameters to select results.
        :return: A list of tenant_connection objects
        :rtype: list of :class:`~ecl.network.v2.tenant_connection.TenantConnection`
        """
        return list(self._list(_tenant_connection.TenantConnection,
                               paginated=False, **query))

    def get_tenant_connection(self, tenant_connection):
        """Get a single tenant_connection

        :param tenant_connection: The value can be the ID of a TenantConnection
                                  or a :class:`~ecl.network.v2.tenant_connection.TenantConnection`
                                  instance.

        :returns: One :class:`~ecl.network.v2.tenant_connection.TenantConnection`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_tenant_connection.TenantConnection, tenant_connection)

    def create_tenant_connection(self,
                                 connected_network_id, connected_network_tenant_id,
                                 connected_interface_id, connected_interface_ip_address,
                                 interface_type,
                                 name=None, description=None, tenant_id=None,
                                 connected_interface_virtual_ip_address=None,
                                 connected_interface_virtual_ip_vrid=None):
        """Create a TenantConnection from attributes

        :param uuid connected_network_id: ID of the connected network
        :param uuid connected_network_tenant_id: Tenant ID of the Connected Network
        :param uuid connected_interface_id:
                Resource id of the Interface which Connects the Tenant
        :param IPv4 connected_interface_ip_address:
                IP Address of the Interface which Connects the Tenant
        :param IPv4 connected_interface_virtual_ip_address:
                Virtual IP Address of the Interface which Connects the Tenant
        :param integer connected_interface_virtual_ip_vrid:
                VRID of the Interface which Connects the Tenant
        :param string interface_type: Interface Type of the Tenant Connection
        :param string name: Name of the Tenant Connection
        :param string description: Description of the Tenant Connection
        :param uuid tenant_id: Tenant ID of the owner

        :return: results of TenantConnection creation
        :rtype: :class:`~ecl.network.v2.tenant_connection.TenantConnection`
        """
        body = dict()
        connected_interface = dict()
        connected_interface["id"] = connected_interface_id
        connected_interface["ip_address"] = connected_interface_ip_address
        body["connected_interface"] = connected_interface

        connected_network = dict()
        connected_network["id"] = connected_network_id
        connected_network["tenant_id"] = connected_network_tenant_id
        body["connected_network"] = connected_network

        body["interface_type"] = interface_type
        if description:
            body["description"] = description
        if name:
            body["name"] = name
        if tenant_id:
            body["tenant_id"] = tenant_id
        if connected_interface_virtual_ip_address:
            connected_interface["virtual_ip_address"] = \
                connected_interface_virtual_ip_address
        if connected_interface_virtual_ip_vrid:
            connected_interface["virtual_ip_properties"] = \
                {"protocol": "vrrp",
                 "vrid": connected_interface_virtual_ip_vrid}
        return self._create(_tenant_connection.TenantConnection,
                            **body)

    def update_tenant_connection(self, tenant_connection, name=None,
                                 description=None):
        """Update a Tenant Connection from attributes

        :param tenant_connection: The value can be the ID
            of a tenant_connection or
            a :class:`~ecl.network.v2.tenant_connection.TenantConeection` instance.
        :param string name: Name of TenantConnection to update
        :param string description: Description of TenantConnection to update

        :return: results of TenantConnection update
        :rtype: :class:`~ecl.network.v2.tenant_connection.TenantConnection`
        """
        body = dict()
        if name is not None:
            body["name"] = name
        if description is not None:
            body["description"] = description
        if not isinstance(tenant_connection, _tenant_connection.TenantConnection):
            tenant_connection = self._get_resource(
                _tenant_connection.TenantConnection, tenant_connection)
            tenant_connection._body.clean()
        return self._update(_tenant_connection.TenantConnection,
                            tenant_connection, **body)

    def delete_tenant_connection(self, tenant_connection):
        """Delete a Tenant Connection

        :param tenant_connection: The value can be the ID
            of a tenant_connection or
            a :class:`~ecl.network.v2.tenant_connection.TenantConeection` instance.
        :return:
        """
        return self._delete(_tenant_connection.TenantConnection, tenant_connection)

    def execute_tenant_connection(self, tenant_connection):
        if not isinstance(tenant_connection, _tenant_connection.TenantConnection):
            tenant_connection = self._get_resource(
                _tenant_connection.TenantConnection, tenant_connection)
        return tenant_connection.execute(self.session)

    def gcp_services(self, **params):
        """Return a list of gcp_services

        :param params: The parameters as query string
                       to get gcp_services by specified condition.

        :returns: A list of gcp_services objects
        :rtype: list of :class:`~ecl.network.v2.gcp.GCPService`
        """
        return list(self._list(_gcp.GCPService, paginated=False, **params))

    def get_gcp_service(self, gcp_service):
        """Get a single gcp_service

        :param gcp_service:
            The value can be the ID of a gcp_service or a
            :class:`~ecl.network.v2.gcp.GCPService` instance.

        :returns: One :class:`~ecl.network.v2.gcp.GCPService`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_gcp.GCPService, gcp_service)

    def find_gcp_service(self, name_or_id, ignore_missing=False):
        """Find a single gcp_service

        :param name_or_id: The name or ID of a gcp_service.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.

        :returns: One :class:`~ecl.network.v2.gcp.GCPService` or None
        """
        return self._find(_gcp.GCPService, name_or_id,
                          ignore_missing=ignore_missing)

    def gcp_gateways(self, **params):
        """Return a list of gcp_gateways

        :param params: The parameters as query string
                       to get gcp_gateways by specified condition.

        :returns: A list of gcp_gateways objects
        :rtype: list of :class:`~ecl.network.v2.gcp.GCPGateway`
        """
        return list(self._list(_gcp.GCPGateway, paginated=False, **params))

    def get_gcp_gateway(self, gcp_gateway):
        """Get a single gcp_gateway

        :param gcp_gateway:
            The value can be the ID of a gcp_gateway or a
            :class:`~ecl.network.v2.gcp.GCPGateway` instance.


        :returns: One :class:`~ecl.network.v2.gcp.GCPGateway`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_gcp.GCPGateway, gcp_gateway)

    def find_gcp_gateway(self, name_or_id, ignore_missing=False):
        """Find a single gcp_gateway

        :param name_or_id: The name or ID of a gcp_gateway.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.

        :returns: One :class:`~ecl.network.v2.gcp.GCPGateway` or None
        """
        return self._find(_gcp.GCPGateway, name_or_id,
                          ignore_missing=ignore_missing)

    def gcp_interfaces(self, **params):
        """Return a list of gcp_interfaces

        :param params: The parameters as query string
                       to get gcp_interfaces by specified condition.

        :returns: A list of gcp_interfaces objects
        :rtype: list of :class:`~ecl.network.v2.gcp.GCPInterface`
        """
        return list(self._list(_gcp.GCPInterface, paginated=False, **params))

    def get_gcp_interface(self, gcp_interface):
        """Get a single gcp_interface

        :param gcp_interface:
            The value can be the ID of a gcp_interface or a
            :class:`~ecl.network.v2.gcp.GCPInterface` instance.

        :returns: One :class:`~ecl.network.v2.gcp.GCPInterface`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_gcp.GCPInterface, gcp_interface)

    def find_gcp_interface(self, name_or_id, ignore_missing=False):
        """Find a single gcp_interface

        :param name_or_id: The name or ID of a gcp_interface.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.

        :returns: One :class:`~ecl.network.v2.gcp.GCPInterface` or None
        """
        return self._find(_gcp.GCPInterface, name_or_id,
                          ignore_missing=ignore_missing)

    def azure_services(self, **params):
        """Return a list of azure_services

        :param params: The parameters as query string
                       to get azure_services by specified condition.

        :returns: A list of azure_services objects
        :rtype: list of :class:`~ecl.network.v2.azure.AzureService`
        """
        return list(self._list(_azure.AzureService, paginated=False, **params))

    def get_azure_service(self, azure_service):
        """Get a single azure_service

        :param azure_service:
            The value can be the ID of a azure_service or a
            :class:`~ecl.network.v2.azure.AzureService` instance.

        :returns: One :class:`~ecl.network.v2.azure.AzureService`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_azure.AzureService, azure_service)

    def find_azure_service(self, name_or_id, ignore_missing=False):
        """Find a single azure_service

        :param name_or_id: The name or ID of a azure_service.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.

        :returns: One :class:`~ecl.network.v2.azure.AzureService` or None
        """
        return self._find(_azure.AzureService, name_or_id,
                          ignore_missing=ignore_missing)

    def azure_gateways(self, **params):
        """Return a list of azure_gateways

        :param params: The parameters as query string
                       to get azure_gateways by specified condition.

        :returns: A list of azure_gateways objects
        :rtype: list of :class:`~ecl.network.v2.azure.AzureGateway`
        """
        return list(self._list(_azure.AzureGateway, paginated=False, **params))

    def get_azure_gateway(self, azure_gateway):
        """Get a single azure_gateway

        :param azure_gateway:
            The value can be the ID of a azure_gateway or a
            :class:`~ecl.network.v2.azure.AzureGateway` instance.

        :returns: One :class:`~ecl.network.v2.azure.AzureGateway`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_azure.AzureGateway, azure_gateway)

    def find_azure_gateway(self, name_or_id, ignore_missing=False):
        """Find a single azure_gateway

        :param name_or_id: The name or ID of a azure_gateway.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.

        :returns: One :class:`~ecl.network.v2.azure.AzureGateway` or None
        """
        return self._find(_azure.AzureGateway, name_or_id,
                          ignore_missing=ignore_missing)

    def azure_interfaces(self, **params):
        """Return a list of azure_interfaces

        :param params: The parameters as query string
                       to get azure_interfaces by specified condition.

        :returns: A list of azure_interfaces objects
        :rtype: list of :class:`~ecl.network.v2.azure.AzureInterface`
        """
        return list(self._list(_azure.AzureInterface, paginated=False, **params))

    def get_azure_interface(self, azure_interface):
        """Get a single azure_interface

        :param azure_interface:
            The value can be the ID of a azure_interface or a
            :class:`~ecl.network.v2.azure.AzureInterface` instance.

        :returns: One :class:`~ecl.network.v2.azure.AzureInterface`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_azure.AzureInterface, azure_interface)

    def find_azure_interface(self, name_or_id, ignore_missing=False):
        """Find a single azure_interface

        :param name_or_id: The name or ID of a azure_interface.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.

        :returns: One :class:`~ecl.network.v2.azure.AzureInterface` or None
        """
        return self._find(_azure.AzureInterface, name_or_id,
                          ignore_missing=ignore_missing)

    def fic_services(self, **query):
        """Return a list of FIC Service

        :returns: A list of FIC Service objects
        """
        return list(self._list(_fic.FICService, paginated=False,
                               **query))

    def get_fic_service(self, fic_service):

        """Get a single FIC Service

        :param fic_service: The value can be the ID of a FIC Service or a
                       :class:`~ecl.network.v2.fic.FICService` instance.

        :returns: One :class:`~ecl.network.v2.fic.FICService`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_fic.FICService, fic_service)

    def fic_gateways(self, **query):
        """Return a list of FIC Gateways

        :param query: Query parameters to select results

        :returns: A list of FIC Gateway objects
        """
        return list(self._list(_fic.FICGateway, paginated=False, **query))

    def get_fic_gateway(self, fic_gateway):

        """Get a single FIC Gateway

        :param fic_gateway: The value can be the ID of a FIC Gateway or a
                       :class:`~ecl.network.v2.fic.FICGateway` instance.

        :returns: One :class:`~ecl.network.v2.fic.FICGateway`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_fic.FICGateway, fic_gateway)

    def find_fic_gateway(self, name_or_id, ignore_missing=False):
        """Find a single fic_gateway

        :param name_or_id: The name or ID of a fic_gateway.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.network.v2.fic.FICGateway` or None
        """
        return self._find(_fic.FICGateway,
                          name_or_id, ignore_missing=ignore_missing)

    def fic_interfaces(self, **query):
        """Return a list of FIC Interface

        :returns: A list of FIC Interface objects
        """
        return list(self._list(_fic.FICInterface, paginated=False,
                               *query))

    def get_fic_interface(self, fic_interface):

        """Get a single FIC Gateway

        :param fic_interface: The value can be the ID of a FIC Interface or a
                       :class:`~ecl.network.v2.fic.FICInterface` instance.

        :returns: One :class:`~ecl.network.v2.fic.FICInterface`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_fic.FICInterface, fic_interface)
