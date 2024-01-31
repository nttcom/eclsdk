# -*- coding: utf-8 -*-

from ecl import exceptions
from ecl import resource2
from ecl.dedicated_hypervisor import dedicated_hypervisor_service

class CFGWConnection():
    #resource_key = "cfgw_connection"
    #resources_key = "cfgw_connections"
    service = dedicated_hypervisor_service.DedicatedHypervisorService("v1.0")
    base_path = '/' + service.version + '/cfgw_connections'

    allow_list = True
    allow_get = True

    _query_mapping = resource2.QueryParameters(
        "id",
        "cfgw_connection"
    )

    id = resource2.Body("id")
    cfgw_connection = resource2.Body("cfgw_connection")
