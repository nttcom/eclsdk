# -*- coding: utf-8 -*-


from ecl.network import network_service
from ecl.network.v2.base import NetworkBaseResource
from ecl import resource2
from ecl import exceptions


class InternetService(NetworkBaseResource):

    resource_key = "internet_service"
    resources_key = "internet_services"
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/internet_services'

    allow_list = True
    allow_get = True

    _query_mapping = resource2.QueryParameters(
        "description", "id", "minimal_subnet_length",
        "zone", "name", "sort_key", "sort_dir",
    )

    description = resource2.Body("description")
    id = resource2.Body("id")
    minimal_submask_length = resource2.Body("minimal_submask_length")
    zone = resource2.Body("zone")
    name = resource2.Body("name")

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


class InternetGateway(NetworkBaseResource):

    resource_key = "internet_gateway"
    resources_key = "internet_gateways"
    base_path = '/v2.0/internet_gateways'
    service = network_service.NetworkService()

    allow_list = True
    allow_get = True
    allow_create = True
    allow_update = True
    allow_delete = True

    _query_mapping = resource2.QueryParameters(
        "description", "id", "internet_service_id",
        "name", "qos_option_id", "status", "tenant_id",
        "sort_key", "sort_dir",
    )

    description = resource2.Body("description")
    id = resource2.Body("id")
    internet_service_id = resource2.Body("internet_service_id")
    name = resource2.Body("name")
    qos_option_id = resource2.Body("qos_option_id")
    status = resource2.Body("status")
    tenant_id = resource2.Body("tenant_id")

    def wait_for_gateway(self, session, status='ACTIVE', failures=['ERROR'],
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
