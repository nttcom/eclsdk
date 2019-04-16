# -*- coding: utf-8 -*-


from ecl.network import network_service
from ecl.network.v2.base import NetworkBaseResource
from ecl import resource2
from ecl import exceptions


class FICService(NetworkBaseResource):

    resource_key = "fic_service"
    resources_key = "fic_services"
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/fic_services'

    allow_list = True
    allow_get = True

    _query_mapping = resource2.QueryParameters(
        "description", "id",
        "name", "zone",
        "sort_key", "sort_dir",
    )

    description = resource2.Body("description")
    id = resource2.Body("id")
    zone = resource2.Body("zone")
    name = resource2.Body("name")


class FICGateway(NetworkBaseResource):

    resource_key = "fic_gateway"
    resources_key = "fic_gateways"
    base_path = '/v2.0/fic_gateways'
    service = network_service.NetworkService()

    allow_list = True
    allow_get = True
    allow_create = True
    allow_update = True
    allow_delete = True

    _query_mapping = resource2.QueryParameters(
        "description", "id",
        "name", "qos_option_id",
        "status", "tenant_id",
        "fic_service_id",
        "sort_key", "sort_dir",
    )

    description = resource2.Body("description")
    id = resource2.Body("id")
    name = resource2.Body("name")
    qos_option_id = resource2.Body("qos_option_id")
    status = resource2.Body("status")
    tenant_id = resource2.Body("tenant_id")
    fic_service_id = resource2.Body("fic_service_id")

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


class FICInterface(NetworkBaseResource):

    resource_key = "fic_interface"
    resources_key = "fic_interfaces"
    base_path = '/v2.0/fic_interfaces'
    service = network_service.NetworkService()

    allow_list = True
    allow_get = True
    allow_create = True
    allow_update = True
    allow_delete = True

    _query_mapping = resource2.QueryParameters(
        "description", "id",
        "name", "fic_gw_id",
        "status", "tenant_id",
        "sort_key", "sort_dir",
    )

    description = resource2.Body("description")
    id = resource2.Body("id")
    fic_gw_id = resource2.Body("fic_gw_id")
    name = resource2.Body("name")
    status = resource2.Body("status")
    tenant_id = resource2.Body("tenant_id")
    primary = resource2.Body("primary")
    secondary = resource2.Body("secondary")

    def wait_for_interface(self, session, status='ACTIVE', failures=['ERROR'],
                           interval=2, wait=120):
        return resource2.wait_for_status(session, self, status,
                                         failures, interval, wait)
