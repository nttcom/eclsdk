# -*- coding: utf-8 -*-

from ecl.network import network_service
from ecl import resource2


class ReservedAddress(resource2.Resource):
    resource_key = 'reserve_address'
    resources_key = 'reserve_addresses'
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/reserve_addresses'

    _query_mapping = resource2.QueryParameters(
        "subnets", "id", "destination", "sort_key", "sort_dir",
    )

    # capabilities
    allow_create = False
    allow_get = True
    allow_update = False
    allow_delete = False
    allow_list = True

    # Properties
    #: id of the reserved address
    id = resource2.Body("id")
    #: subnets cidr of the reserved address
    subnets = resource2.Body("subnets")
    #: tenant id that reserved address belong to
    tenant_id = resource2.Body("tenant_id")
