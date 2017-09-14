# -*- coding: utf-8 -*-


from ecl.network import network_service
from ecl.network.v2.base import NetworkBaseResource
from ecl import resource2
from ecl import exceptions


class InterDCService(NetworkBaseResource):

    resource_key = "interdc_service"
    resources_key = "interdc_services"
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/interdc_services'

    allow_list = True
    allow_get = True

    _query_mapping = resource2.QueryParameters(
        "description", "id", "zone", "name"
    )

    description = resource2.Body("description")
    id = resource2.Body("id")
    zone = resource2.Body("zone")
    name = resource2.Body("name")


class InterDCGateway(NetworkBaseResource):

    resource_key = "interdc_gateway"
    resources_key = "interdc_gateways"
    base_path = '/v2.0/interdc_gateways'
    service = network_service.NetworkService()

    _query_mapping = resource2.QueryParameters(
        "description", "id", "interdc_service_id",
        "name", "status", "tenant_id",
        "sort_key", "sort_dir",
    )

    allow_list = True
    allow_get = True
    allow_create = True
    allow_update = True
    allow_delete = True

    description = resource2.Body("description")
    id = resource2.Body("id")
    interdc_service_id = resource2.Body("interdc_service_id")
    name = resource2.Body("name")
    status = resource2.Body("status")
    tenant_id = resource2.Body("tenant_id")

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


class InterDCInterface(NetworkBaseResource):

    resource_key = "interdc_interface"
    resources_key = "interdc_interfaces"
    base_path = '/v2.0/interdc_interfaces'
    service = network_service.NetworkService()

    _query_mapping = resource2.QueryParameters(
        "description", "gw_vipv4", "gw_vipv6",
        "id", "interdc_gw_id", "name", "netmask",
        "primary_ipv4", "primary_ipv6",
        "secondary_ipv4", "secondary_ipv6",
        "status", "tenant_id", "vrid",
        "sort_key", "sort_dir",
    )

    allow_list = True
    allow_get = True
    allow_create = True
    allow_update = True
    allow_delete = True

    description = resource2.Body("description")
    gw_vipv4 = resource2.Body("gw_vipv4")
    gw_vipv6 = resource2.Body("gw_vipv6")
    id = resource2.Body("id")
    interdc_gw_id = resource2.Body("interdc_gw_id")
    name = resource2.Body("name")
    netmask = resource2.Body("netmask")
    primary_ipv4 = resource2.Body("primary_ipv4")
    primary_ipv6 = resource2.Body("primary_ipv6")
    secondary_ipv4 = resource2.Body("secondary_ipv4")
    secondary_ipv6 = resource2.Body("secondary_ipv6")
    status = resource2.Body("status")
    tenant_id = resource2.Body("tenant_id")
    vrid = resource2.Body("vrid")

    def wait_for_interface(self, session, status='ACTIVE', failures=['ERROR'],
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
