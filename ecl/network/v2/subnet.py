# -*- coding: utf-8 -*-


from . import base
from ecl.network import network_service
from ecl import resource2
from ecl import exceptions


class Subnet(base.NetworkBaseResource):
    resource_key = 'subnet'
    resources_key = 'subnets'
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/subnets'

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True

    # query mappings
    _query_mapping = resource2.QueryParameters('cidr', 'description',
                                               'gateway_ip', 'id',
                                               'ip_version',
                                               'ipv6_address_mode',
                                               'ipv6_ra_mode',
                                               'name', 'network_id',
                                               'status', 'tenant_id',
                                               'subnet_id', 'sort_key', 'sort_dir',)

    # Properties
    #: The start and end addresses for the allocation pools.
    allocation_pools = resource2.Body('allocation_pools')
    #: The CIDR.
    cidr = resource2.Body('cidr')
    #: The subnet description.
    description = resource2.Body('description')
    #: A list of DNS nameservers.
    dns_nameservers = resource2.Body('dns_nameservers')
    #: The gateway IP address.
    gateway_ip = resource2.Body('gateway_ip')
    #: Subnet unique id.
    id = resource2.Body('id')
    #: A list of host routes.
    host_routes = resource2.Body('host_routes')
    #: A list of ntp servers.
    ntp_servers = resource2.Body('ntp_servers')
    #: The IP version, which is ``4`` or ``6``.
    ip_version = resource2.Body('ip_version')
    #: The IPv6 address modes which are 'dhcpv6-stateful', 'dhcpv6-stateless',
    #: or 'SLAAC'
    ipv6_address_mode = resource2.Body('ipv6_address_mode')
    #: The IPv6 router advertisements modes
    ipv6_ra_mode = resource2.Body('ipv6_ra_mode')
    #: Set to ``True`` if DHCP is enabled and ``False`` if DHCP is disabled.
    #: *Type: bool*
    enable_dhcp = resource2.Body('enable_dhcp', type=bool)
    #: The subnet name.
    name = resource2.Body('name')
    #: The ID of the attached network.
    network_id = resource2.Body('network_id')
    #: The ID of the project this subnet is associated with.
    project_id = resource2.Body('tenant_id')
    #: The status of the subnet
    status = resource2.Body('status')
    #: tags of the subnet
    tags = resource2.Body('tags')

    @classmethod
    def find(cls, session, name_or_id, ignore_missing=False, **params):
        """Find a resource by its name or id.

        :param session: The session to use for making this request.
        :type session: :class:`~ecl.session.Session`
        :param name_or_id: This resource's identifier, if needed by
                           the request. The default is ``None``.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :param dict params: Any additional parameters to be passed into
                            underlying methods, such as to
                            :meth:`~ecl.resource2.Resource.existing`
                            in order to pass on URI parameters.

        :return: The :class:`Resource` object matching the given name or id
                 or None if nothing matches.
        :raises: :class:`ecl.exceptions.DuplicateResource` if more
                 than one resource is found for this request.
        :raises: :class:`ecl.exceptions.ResourceNotFound` if nothing
                 is found and ignore_missing is ``False``.
        """
        # Try to short-circuit by looking directly for a matching ID.

        data = cls.list(session, **params)

        result = cls._get_one_match(name_or_id, data)
        if result is not None:
            return result

        if ignore_missing:
            return None
        raise exceptions.ResourceNotFound(
            "No %s found for %s" % (cls.__name__, name_or_id))
