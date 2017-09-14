# -*- coding: utf-8 -*-

import base
from ecl.network import network_service
from ecl import resource2
from ecl import exceptions


class CommonFunction(base.NetworkBaseResource):
    resource_key = 'common_function'
    resources_key = 'common_functions'
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/common_functions'

    _query_mapping = resource2.QueryParameters(
        "description", "id", "link_local_ip_address",
        "name", "status", "sort_key", "sort_dir",
    )

    # capabilities
    allow_get = True
    allow_list = True

    # properties
    #: Description of the Common Function resource.
    description = resource2.Body('description')
    #: Unique ID of the Common Function resource.
    id = resource2.Body('id')
    #: Link-local IP address of Common Function (after NAT).
    link_local_ip_address = resource2.Body('link_local_ip_address')
    #: Name of the Common Function resource.
    name = resource2.Body('name')
    #: Hidden Common Function status.
    status = resource2.Body('status')

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