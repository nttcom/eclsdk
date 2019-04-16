# -*- coding: utf-8 -*-


from ecl.network import network_service
from ecl.network.v2.base import NetworkBaseResource
from ecl import exceptions
from ecl import resource2


class QosOption(NetworkBaseResource):

    resource_key = "qos_option"
    resources_key = "qos_options"
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/qos_options'

    allow_list = True
    allow_get = True

    _query_mapping = resource2.QueryParameters(
        "description", "bandwidth", "name",
        "status", "qos_type", "service_type",
        "interdc_service_id", "internet_service_id",
        "vpn_service_id", "sort_key", "sort_dir",
        "fic_service_id",
    )

    description = resource2.Body("description")
    bandwidth = resource2.Body("bandwidth")
    id = resource2.Body("id")
    name = resource2.Body("name")
    status = resource2.Body("status")
    qos_type = resource2.Body("qos_type")
    service_type = resource2.Body("service_type")
    interdc_service_id = resource2.Body("interdc_service_id")
    internet_service_id = resource2.Body("internet_service_id")
    vpn_service_id = resource2.Body("vpn_service_id")
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
