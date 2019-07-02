# -*- coding: utf-8 -*-


from . import base
from ecl import utils
from ecl import exceptions
from ecl import resource2
from ecl.network import network_service


class LoadBalancer(base.NetworkBaseResource):

    resource_key = "load_balancer"
    resources_key = "load_balancers"
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/load_balancers'

    _query_mapping = resource2.QueryParameters(
        "admin_username", "availability_zone", "default_gateway",
        "description", "id", "load_balancer_plan_id", "name",
        "status", "tenant_id", "user_username",
        "sort_key", "sort_dir",
    )

    # Capabilities:
    allow_list = True
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True

    # Properties
    #: Admin's password placeholder.
    admin_password = resource2.Body("admin_password")
    #: Username with admin access to VM instance.
    admin_username = resource2.Body("admin_username")
    #: Availability Zone.
    availability_zone = resource2.Body("availability_zone")
    #: IP address of default gateway.
    default_gateway = resource2.Body("default_gateway")
    #: Description of the Load Balancer.
    description = resource2.Body("description")
    #: Unique ID of the Load Balancer.
    id = resource2.Body("id")
    #: Load Balancer Plan
    load_balancer_plan_id = resource2.Body("load_balancer_plan_id")
    #: Name of the Load Balancer
    name = resource2.Body("name")
    #: The load_balancer status.
    status = resource2.Body("status")
    #: Tenant ID of the owner (UUID)
    tenant_id = resource2.Body("tenant_id")
    #: Username with user access to VM instance
    user_username = resource2.Body("user_username")
    #: User's password placeholder
    user_password = resource2.Body("user_password")
    #: Attached interfaces:
    #: interfaces.id: Unique ID of the Load Balancer Interface
    #: interfaces.ip_address: IP Address
    #: interfaces.name: Name the Load Balancer Interface
    #: interfaces.network_id: Network
    #: interfaces.slot_number: Slot Number
    #: interfaces.status: Load Balancer Interface status
    #: interfaces.type: Load Balancer Interface Type
    #: interfaces.virtual_ip_address: Virtual IP Address
    #: interfaces.virtual_ip_properties: Properties used for virtual IP address.
    interfaces = resource2.Body("interfaces")

    def update(self, session, load_balancer_id, **attrs):
        """Update a load balancer."""

        uri = utils.urljoin(self.base_path, load_balancer_id)
        resp = session.put(
            uri, endpoint_filter=self.service,
            json=attrs
        )
        self._translate_response(resp, has_body=True)
        return self

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
