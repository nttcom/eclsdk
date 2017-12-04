# -*- coding: utf-8 -*-

from ecl.virtual_network_appliance import virtual_network_appliance_service
from ecl import resource2


class Operation(resource2.Resource):
    resources_key = "operations"
    service = virtual_network_appliance_service.\
        VirtualNetworkApplianceService("v1.0")
    base_path = '/' + service.version + '/operations'

    # Capabilities
    allow_list = True

    _query_mapping = resource2.QueryParameters("id", "resource_id")

    # Properties
    #: ID of network appliance's operation
    id = resource2.Body('id')
    #: Target network appliance id of this operation.
    resource_id = resource2.Body('resource_id')
    #: request type of operation.
    request_type = resource2.Body('request_type')
    #: Status of operation.
    status = resource2.Body('status')
    #: Tenant ID of operation.
    tenant_id = resource2.Body('tenant_id')
    #: resource type of operation.
    resource_type = resource2.Body('resource_type')
