# -*- coding: utf-8 -*-

from . import base
from ecl.network import network_service
from ecl import resource2
from ecl import exceptions


class CommonFunctionGateway(base.NetworkBaseResource):
    resource_key = 'common_function_gateway'
    resources_key = 'common_function_gateways'
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/common_function_gateways'

    _query_mapping = resource2.QueryParameters(
        "common_function_pool_id", "description", "id",
        "name", "network_id", "status", "subnet_id",
        "submet_id", "tenant_id", "sort_key", "sort_dir",
    )

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True

    # properties
    #: Common Function Pool instantiated by this Gateway.
    common_function_pool_id = resource2.Body('common_function_pool_id')
    #: Description of the Common Function Pool Gateway resource.
    description = resource2.Body('description')
    #: Unique ID of the Common Function Pool Gateway resource.
    id = resource2.Body('id')
    #: Name of the Common Function Pool Gateway resource.
    name = resource2.Body('name')
    #: Id of automatically created network connected to this Common Function
    #: Pool Gateway.
    network_id = resource2.Body('network_id')
    #: The Common Function Gateway status.
    status = resource2.Body('status')
    #: Id of automatically created subnet connected to this Common Function Pool
    #: Gateway (using link-local addresation).
    subnet_id = resource2.Body('subnet_id')
    #: Tenant ID of the owner (UUID).
    tenant_id = resource2.Body('tenant_id')

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
