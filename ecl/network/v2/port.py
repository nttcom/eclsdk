# -*- coding: utf-8 -*-

from . import base
from ecl.network import network_service
from ecl import resource2
from ecl import exceptions


class Port(base.NetworkBaseResource):

    resource_key = 'port'
    resources_key = 'ports'
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/ports'

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True

    # query mappings
    _query_mapping = resource2.QueryParameters('description',
                                               'device_id',
                                               'device_owner',
                                               'id', 'mac_address',
                                               'name', 'network_id',
                                               'segmentation_id',
                                               'segmentation_type',
                                               'status', 'tenant_id',
                                               'port_id',
                                               "sort_key", "sort_dir",)

    # properties
    #: admin state of port
    admin_state_up = resource2.Body('admin_state_up')

    #: admin_state displayed by 'UP' or 'DOWN'
    admin_state = resource2.Body('admin_state')

    #: allowed address pairs
    allowed_address_pairs = resource2.Body('allowed_address_pairs')

    #: The port description.
    description = resource2.Body('description')

    #: Device ID of this port.
    device_id = resource2.Body('device_id')

    #: Device owner of this port (e.g. ``network:dhcp``).
    device_owner = resource2.Body('device_owner')

    #: fixed ips of the port.
    fixed_ips = resource2.Body('fixed_ips')

    #: ID of the port.
    id = resource2.Body('id')

    #: The MAC address of the port.
    mac_address = resource2.Body('mac_address')

    #: If the port is managed by service
    managed_by_service = resource2.Body('managed_by_service')

    #: The port name.
    name = resource2.Body('name')

    #: The ID of the attached network.
    network_id = resource2.Body('network_id')

    #: The ID of the project who owns the network. Only administrative
    #: users can specify a project ID other than their own.
    project_id = resource2.Body('tenant_id')

    #: The segmentation ID of ports.
    segmentation_id = resource2.Body('segmentation_id', type=int)

    #: The segmentation type of ports.
    segmentation_type = resource2.Body('segmentation_type')

    #: The port status. Value is ``ACTIVE`` or ``DOWN``.
    status = resource2.Body('status')

    #: tags of the port.
    tags = resource2.Body('tags')

    #: admin_state displayed by 'UP' or 'DOWN'
    @property
    def admin_state(self):
        admin_state_up = resource2.Body('admin_state_up')
        admin_state = 'UP' if admin_state_up else 'DOWN'
        return admin_state

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
