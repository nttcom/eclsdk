# -*- coding: utf-8 -*-

from ecl.dedicated_hypervisor import dedicated_hypervisor_service
from ecl import resource2


class Sddc(resource2.Resource):
    resources_key = "sddcs"
    resource_key = "sddc"
    base_path = '/sddcs'
    service = dedicated_hypervisor_service.DedicatedHypervisorService()

    # Capabilities
    allow_list = True
    allow_delete = True

    _query_mapping = resource2.QueryParameters(
        "changes-since", "maker", "limit", "name",)

    # Properties
    #: id of sddc instance.
    id = resource2.Body('id')
    #: name of sddc instance.
    name  = resource2.Body('name')
