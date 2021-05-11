# -*- coding: utf-8 -*-
from . import base

from ecl import resource2
from ecl.mvna import mvna_service

class Operation(resource2.Resource):
    resource_key = "operation"
    resources_key = "operations"
    service = mvna_service.MVNAService("v1.0")
    base_path = '/' + service.version + '/operations'

    _query_mapping = base.MVNAQueryParameters(
        "id",
        "resource_id",
        "resource_type",
        "request_id",
        "request_type",
        "status",
        "tenant_id",
        "no_deleted",
        "latest"
    )

    # Capabilities
    allow_list = True
    allow_get = True

    # Properties
    #: ID of network appliance's operation
    id = resource2.Body('id')
    #: Target load balancer id of operation.
    resource_id = resource2.Body('resource_id')
    #: resource type of operation.
    resource_type = resource2.Body('resource_type')
    #: Request ID of operation.
    request_id = resource2.Body('request_id')
    #: A string representation of the request type.
    request_types = resource2.Body('request_types')
    #: Request body(JSON String) of operation.
    request_body = resource2.Body('request_body')
    #: Status of operation.
    status = resource2.Body('status')
    #: Reception datetime of operation.
    reception_datetime = resource2.Body('reception_datetime')
    #: Commit datetime of operation.
    commit_datetime = resource2.Body('commit_datetime')
    #: Warning of operation.
    warning = resource2.Body('warning')
    #: Error of operation.
    error = resource2.Body('error')
    #: Tenant ID of operation.
    tenant_id = resource2.Body('tenant_id')
