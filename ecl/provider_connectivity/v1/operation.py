# -*- coding: utf-8 -*-

from ecl.provider_connectivity import provider_connectivity_service
from ecl import resource2


class Operation(resource2.Resource):
    resources_key = "operations"
    service = provider_connectivity_service.ProviderConnectivityService("v1.0")
    base_path = '/' + service.version + '/icc/operations'

    # Capabilities
    allow_list = True

    _query_mapping = resource2.QueryParameters("connection_id",)

    # Properties
    #: It identifies connection resource uniquely.
    connection_id = resource2.Body('connection_id', alternate_id=True)
    #: order type.
    order_type = resource2.Body('order_type')
    #: operation phase.
    phase = resource2.Body('phase')
    #: Status of phase.
    operation_status = resource2.Body('operation_status')
    #: reception datetime. YYYY-MM-DD HH:MM:SS format.
    reception_datetime = resource2.Body('reception_datetime')
    #: commit datetime. YYYY-MM-DD HH:MM:SS format.
    commit_datetime = resource2.Body('commit_datetime')
    #: Request body is stored.
    request_body = resource2.Body('request_body')
