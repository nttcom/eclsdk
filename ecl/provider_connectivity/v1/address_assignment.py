# -*- coding: utf-8 -*-

from ecl.provider_connectivity import provider_connectivity_service
from ecl import resource2


class AddressAssignment(resource2.Resource):
    resources_key = "address_assignments"
    resource_key = "address_assignment"

    service = provider_connectivity_service.ProviderConnectivityService("v2.0")
    base_path = '/' + service.version + '/tenant_connection_requests/' \
                                        '%(tenant_connection_request_id)s/address_assignment'

    # capabilities
    allow_list = True
    
    tenant_connection_request_id = resource2.URI("tenant_connection_request_id")

    tenant_connection_id = resource2.Body("tenant_connection_id")

    network_id = resource2.Body("network_id", alternate_id=True)

    mac_address = resource2.Body("mac_address")

