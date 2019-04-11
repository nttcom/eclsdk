# -*- coding: utf-8 -*-

from ecl.fic.v2 import gw_interface as _gwif
from ecl.fic.v2 import qos_option as _qos_option
from ecl.fic.v2 import static_route as _static_route
from ecl.fic.v2 import fic as _fic

from ecl import proxy2


class Proxy(proxy2.BaseProxy):

    def fic_services(self, **query):
        """Return a list of FIC Service

        :returns: A list of FIC Service objects
        """
        return list(self._list(_fic.FICService, paginated=False,
                               **query))

    def get_fic_service(self, fic_service):
        """Get a single FIC Service

        :param fic_service: The value can be the ID of a FIC Service or a
                       :class:`~ecl.fic.v2.fic.FICService` instance.

        :returns: One :class:`~ecl.fic.v2.fic.FICService`
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
                       :class:`~ecl.fic.v2.fic.FICGateway` instance.

        :returns: One :class:`~ecl.fic.v2.fic.FICGateway`
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
        :returns: One :class:`~ecl.fic.v2.fic.FICGateway` or None
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
                       :class:`~ecl.fic.v2.fic.FICInterface` instance.

        :returns: One :class:`~ecl.fic.v2.fic.FICInterface`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_fic.FICInterface, fic_interface)

    def gateway_interfaces(self, **query):
        """Return a list of Gateway Interfaces

        :returns: A list of Gateway Interface objects
        """
        return list(self._list(_gwif.GatewayInterface, paginated=False,
                               **query))

    def get_gateway_interface(self, gw_interface):
        """Get a single Gateway Interface

        :param gw_interface: The value can be the ID of a Gateway Interface or a
                       :class:`~ecl.fic.v2.gw_interface.GatewayInterface` instance.

        :returns: One :class:`~ecl.fic.v2.gw_interface.GatewayInterface`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_gwif.GatewayInterface, gw_interface)

    def create_gateway_interface(self, service_type, network_id,
                                 netmask, gw_vipv4, vrid,
                                 name=None, description=None,
                                 primary_ipv6=None, secondary_ipv6=None,
                                 fic_gw_id=None,tenant_id=None):
        """Create a Gateway Interface from parameters

        :param string service_type: service type of gateway interface to create
        :param string network_id: network ID of gateway interface to create
        :param int netmask: netmask of gateway interface to create
        :param IPv4 gw_vipv4: gateway virtual IPv4 interface to create
        :param int vrid: ID of VRRP of gateway interface to create
        :param string name: name of gateway interface to create
        :param string description: description of gateway interface to create
        :param IPv6 primary_ipv6: primary IPv6 of gateway interface to create
        :param IPv6 secondary_ipv6: secondary IPv6 of gateway interface to create
        :param string fic_gw_id: FIC Gateway ID of gateway interface to create
        :param string tenant_id: tenant ID of gateway interface to create

        :returns: The results of GatewayInterface creation
        :rtype: One :class:`~ecl.fic.v2.gwif.GatewayInterface`
        """
        body = {
            "service_type": service_type,
            "network_id": network_id,
            "netmask": netmask,
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
        if fic_gw_id:
            body.update({"fic_gw_id": fic_gw_id})
        if tenant_id:
            body.update({"tenant_id": tenant_id})

        return self._create(_gwif.GatewayInterface, **body)

    def update_gateway_interface(self, gw_interface, **body):
        """Update a Gateway Interface

        :param gw_interface:  The value can be the ID of a Gateway Interface or a
                       :class:`~ecl.fic.v2.gw_interface.GatewayInterface` instance.
        :param name: name of gateway interface to update
        :param description: description of gateway interface to update

        :returns: The result of update Gateway Interface
        :rtype: :class:`~ecl.fic.v2.gw_interface.GatewayInterface`
        """
        if not isinstance(gw_interface, _gwif.GatewayInterface):
            gw_interface = self._get_resource(_gwif.GatewayInterface, gw_interface)
            gw_interface._body.clean()
        return self._update(_gwif.GatewayInterface, gw_interface, **body)

    def delete_gateway_interface(self, gwif, ignore_missing=False):
        """Delete a Gateway Interface

        :param gwif: The value can be either the ID of a Gateway Interface or a
                       :class:`~ecl.fic.v2.gwif.GatewayInterface` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the Gateway Interface does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent Gateway Interface.

        :return: One :class:`~ecl.fic.v2.gwif.GatewayInterface`
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
        :returns: One :class:`~ecl.fic.v2.gwif.GatewayInterface` or None
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
                       :class:`~ecl.fic.v2.static_route.StaticRoute` instance.

        :returns: One :class:`~ecl.fic.v2.static_route.StaticRoute`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_static_route.StaticRoute, static_route)

    def create_static_route(self, service_type, destination, nexthop,
                            name=None, description=None, fic_gw_id=None,
                            tenant_id=None):
        """Create a Static Route

        :param service_type: service type of static route to create
        :param destination: destination of static route to create
        :param nexthop: next hop of static route to create
        :param name: name of static route to create
        :param description: description of static route to create
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
        if fic_gw_id:
            body.update({"fic_gw_id": fic_gw_id})
        if tenant_id:
            body.update({"tenant_id": tenant_id})

        return self._create(_static_route.StaticRoute, **body)

    def update_static_route(self, static_route, **body):
        """Update a Static Route

        :param static_route:  The value can be the ID of a Static Route or a
                       :class:`~ecl.fic.v2.static_route.StaticRoute` instance.
        :param name: name of static route to update
        :param description: description of static route to update

        :returns: The result of update Static Route
        :rtype: :class:`~ecl.fic.v2.static_route.StaticRoute`
        """
        if not isinstance(static_route, _static_route.StaticRoute):
            static_route = self._get_resource(_static_route.StaticRoute, static_route)
            static_route._body.clean()
        return self._update(_static_route.StaticRoute, static_route, **body)

    def delete_static_route(self, static_route, ignore_missing=False):
        """Delete a Static Route

        :param static_route: The value can be either the ID of a Static Route or a
                       :class:`~ecl.fic.v2.static_route.StaticRoute` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the Static Route does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent Static Route.

        :return: One :class:`~ecl.fic.v2.static_route.StaticRoute`
        """
        return self._delete(_static_route.StaticRoute, static_route,
                            ignore_missing=ignore_missing)
    
    def qos_options(self, **query):
        """Return a list of QoS Options

        :returns: A list of QoS Option objects
        """
        return list(self._list(_qos_option.QosOption, paginated=False,
                               **query))

    def get_qos_option(self, qos_option):
        """Get a single QoS Option

        :param qos_option: The value can be the ID of a QoS Option or a
                       :class:`~ecl.fic.v2.qos_option.QoSOption` instance.

        :returns: One :class:`~ecl.fic.v2.qos_option.QoSOption`
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
        :returns: One :class:`~ecl.fic.v2.qos_option.QosOption` or None
        """
        return self._find(_qos_option.QosOption,
                          name_or_id, ignore_missing=ignore_missing)