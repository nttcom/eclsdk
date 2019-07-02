# -*- coding: utf-8 -*-


from . import base
from ecl.network import network_service
from ecl import resource2
from ecl import exceptions


class Network(base.NetworkBaseResource):

    resource_key = 'network'
    resources_key = 'networks'
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/networks'

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True

    # query mappings
    _query_mapping = resource2.QueryParameters('description', 'id', 'name',
                                               'plane', 'status',
                                               'tenant_id', 'network_id',
                                               "sort_key", "sort_dir",)

    # Properties
    #: admin_state_up status of network
    admin_state_up = resource2.Body('admin_state_up')

    #: The network description.
    description = resource2.Body('description')

    #: The network id.
    id = resource2.Body('id')

    #: The network name.
    name = resource2.Body('name')

    #: The plane of network
    plane = resource2.Body('plane')

    #: The ID of the project this network is associated with.
    project_id = resource2.Body('tenant_id')

    #: The boolean shared status of network.
    shared = resource2.Body('shared')

    #: The network status.
    status = resource2.Body('status')

    #: The associated subnet IDs.
    #: *Type: list of strs of the subnet IDs*
    subnets = resource2.Body('subnets', type=list)

    #: tags of the network.
    tags = resource2.Body('tags')

    #: admin_state displayed by 'UP' or 'DOWN'
    @property
    def admin_state(self):
        return 'UP' if self._body.get('admin_state_up') else 'DOWN'

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
