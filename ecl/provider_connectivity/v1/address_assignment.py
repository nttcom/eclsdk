# -*- coding: utf-8 -*-

from ecl.provider_connectivity import provider_connectivity_service
from ecl import resource2
from ecl.network.v2 import network
from ecl.network.v2 import subnet
import hashlib


class AddressAssignment(resource2.Resource):
    resources_key = "address_assignments"
    resource_key = "address_assignment"

    service = provider_connectivity_service.ProviderConnectivityService("v2.0")
    base_path = '/' + service.version + \
                '/tenant_connection_requests/' \
                '%(tenant_connection_request_id)s/address_assignments'

    # capabilities
    allow_list = True

    #: tenant_connection_request unique ID.
    tenant_connection_request_id = resource2.URI(
                                            "tenant_connection_request_id")

    #: tenant_connection unique ID.
    tenant_connection_id = resource2.Body("tenant_connection_id")

    #: Network unique ID
    network_id = resource2.Body("network_id")

    #: mac address assigned with port
    mac_address = resource2.Body("mac_address")

    #: List of fixes IP addresses assign to port.
    fixed_ips = resource2.Body("fixed_ips")

    #: Allowed address pairs
    allowed_address_pairs = resource2.Body("allowed_address_pairs")

    @staticmethod
    def _get_id(value):
        if isinstance(value, resource2.Resource):
            # Don't check _alternate_id unless we need to. It's an uncommon
            # case and it involves looping through the class' dict.
            id = value.id or getattr(
                value, value._alternate_id(),
                hashlib.new('md5', str(value)).hexdigest())
            return id
        else:
            return value

    def __getattribute__(self, name):
        """Return an attribute on this instance

        This is mostly a pass-through except for a specialization on
        the 'id' name, as this can exist under a different name via the
        `alternate_id` argument to resource.Body.
        """
        if name == "id":
            if name in self._body:
                return self._body[name]
            elif self._alternate_id():
                return self._body[self._alternate_id()]
            else:
                return hashlib.new('md5', str(self)).hexdigest()
        else:
            return object.__getattribute__(self, name)


class ICCNetwork(network.Network):

    service = provider_connectivity_service.ProviderConnectivityService("v2.0")
    base_path = '/' + service.version + \
                '/tenant_connection_requests/' \
                '%(tenant_connection_request_id)s/network'

    # Capabilities
    allow_list = False
    allow_create = False
    allow_delete = False
    allow_update = False
    allow_get = True

    def get(self, session, tenant_connection_request_id):
        uri = self.base_path % {
            "tenant_connection_request_id": tenant_connection_request_id
        }
        resp = session.get(uri, endpoint_filter=self.service)
        self._translate_response(resp, has_body=True)
        return self


class ICCSubnet(subnet.Subnet):

    service = provider_connectivity_service.ProviderConnectivityService("v2.0")
    base_path = '/' + service.version + \
                '/tenant_connection_requests/' \
                '%(tenant_connection_request_id)s/subnets'

    id = resource2.Body("id")
    tenant_connection_request_id = resource2.URI(
                                            "tenant_connection_request_id")

    # Capabilities
    allow_list = True
    allow_create = False
    allow_delete = False
    allow_update = False
    allow_get = True

    dhcp_server_address = resource2.Body('dhcp_server_address')

