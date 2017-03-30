# -*- coding: utf-8 -*-

from ecl.connectivity import connectivity_service
from ecl import resource2


class Operation(resource2.Resource):

    resource_key = None
    resources_key = None

    base_path = '/operations'
    service = connectivity_service.ConnectivityService()

    # capabilities
    allow_get = True
    allow_list = True

    _query_mapping = resource2.QueryParameters("mcic_id", "cic_id")

    operation_id = resource2.Body('operation_id', alternate_id=True)
    operation_status = resource2.Body('operation_status')
    operation_type = resource2.Body('operation_type')
    operation_body = resource2.Body('operation_body', dict)
    mcic_id = resource2.Body('mcic_id')
    cic_id = resource2.Body('cic_id')
    user_id = resource2.Body('user_id')
    user_name = resource2.Body('user_name')
    receipt_date = resource2.Body('receipt_date')
    error_messages = resource2.Body('error_messages', list)
