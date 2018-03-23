# -*- coding: utf-8 -*-


from ecl.network import network_service
from ecl.network.v2.base import NetworkBaseResource
from ecl import resource2
from ecl import exceptions


class GatewayInterface(NetworkBaseResource):

    resource_key = "gw_interface"
    resources_key = "gw_interfaces"
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/gw_interfaces'

    _query_mapping = resource2.QueryParameters(
        "description", "gw_vipv4", "gw_vipv6",
        "id", "interdc_gw_id", "internet_gw_id",
        "name", "netmask", "network_id",
        "primary_ipv4", "primary_ipv6",
        "secondary_ipv4", "secondary_ipv6",
        "service_type", "vpn_gw_id",
        "status", "tenant_id", "vrid",
        "sort_key", "sort_dir", "aws_gw_id",
        "azure_gw_id", "gcp_gw_id",
    )

    allow_list = True
    allow_get = True
    allow_create = True
    allow_delete = True
    allow_update = True

    description = resource2.Body("description")
    gw_vipv4 = resource2.Body("gw_vipv4")
    gw_vipv6 = resource2.Body("gw_vipv6")
    id = resource2.Body("id")
    interdc_gw_id = resource2.Body("interdc_gw_id")
    internet_gw_id = resource2.Body("internet_gw_id")
    name = resource2.Body("name")
    netmask = resource2.Body("netmask")
    network_id = resource2.Body("network_id")
    primary_ipv4 = resource2.Body("primary_ipv4")
    primary_ipv6 = resource2.Body("primary_ipv6")
    secondary_ipv4 = resource2.Body("secondary_ipv4")
    secondary_ipv6 = resource2.Body("secondary_ipv6")
    service_type = resource2.Body("service_type")
    status = resource2.Body("status")
    tenant_id = resource2.Body("tenant_id")
    vpn_gw_id = resource2.Body("vpn_gw_id")
    aws_gw_id = resource2.Body("aws_gw_id")
    gcp_gw_id = resource2.Body("gcp_gw_id")
    azure_gw_id = resource2.Body("azure_gw_id")
    vrid = resource2.Body("vrid")

    def wait_for_create(self, session, status='ACTIVE', failures=['ERROR'],
                         interval=2, wait=120):
        return resource2.wait_for_status(session, self, status,
                                         failures, interval, wait)

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
