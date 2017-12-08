# -*- coding: utf-8 -*-

import base
from ecl.virtual_network_appliance import virtual_network_appliance_service
from ecl import resource2


class Operation(base.VirtualNetworkApplianceBaseResource):
    resources_key = "operations"
    resource_key = "operation"
    service = virtual_network_appliance_service.\
        VirtualNetworkApplianceService("v1.0")
    base_path = '/' + service.version + '/operations'

    # Capabilities
    allow_list = True
    allow_get = True

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
    #: Reception datetime of operation.
    reception_datetime = resource2.Body('reception_datetime')
    #: Commit datetime of operation.
    commit_datetime = resource2.Body('commit_datetime')
    #: Request body of operation.
    request_body = resource2.Body('request_body')
    #: Warning of operation.
    warning = resource2.Body('warning')
    #: Error of operation.
    error = resource2.Body('error')
    #: Error details of operation.
    error_details = resource2.Body('error_details')
    #: Tenant ID of operation.
    tenant_id = resource2.Body('tenant_id')
    #: resource type of operation.
    resource_type = resource2.Body('resource_type')
