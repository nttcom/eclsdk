# -*- coding: utf-8 -*-

from ecl.provider_connectivity import provider_connectivity_service
from ecl import resource2


class Operation(resource2.Resource):
    resources_key = "operations"
    service = provider_connectivity_service.ProviderConnectivityService("v2.0")
    base_path = '/' + service.version + '/operations'

    # Capabilities
    allow_list = True

    _query_mapping = resource2.QueryParameters(
        "service_type", "resource_type", "resource_id", "latest")

    # Properties
    #: ID of operation.
    id = resource2.Body('id', alternate_id=True)
    #: Service type.
    service_type = resource2.Body('service_type')
    #: ID of resource.
    resource_id = resource2.Body('resource_id')
    #: Reource type.
    resource_type = resource2.Body('resource_type')
    #: Request type.
    request_type = resource2.Body('request_type')
    #: operation phase.
    phase = resource2.Body('phase')
    #: Status of operation.
    operation_status = resource2.Body('operation_status')
    #: reception datetime. YYYY-MM-DD HH:MM:SS format.
    reception_datetime = resource2.Body('reception_datetime')
    #: commit datetime. YYYY-MM-DD HH:MM:SS format.
    commit_datetime = resource2.Body('commit_datetime')
    #: Request body is stored.
    request_body = resource2.Body('request_body')
    #: Note
    notes = resource2.Body('notes')
    #: Tenant ID
    tenant_id = resource2.Body('tenant_id')
    #: If use this query, the latest operation is returned.
    latest = resource2.Body('latest')
