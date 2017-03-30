# -*- coding: utf-8 -*-

from ecl.block_store import block_store_service
from ecl import resource


class Limit(resource.Resource):
    resource_key = "limits"
    resources_key = "limits"
    base_path = "/limits"
    service = block_store_service.BlockStoreService()

    # capabilities
    allow_retrieve = True

    # Properties
    #: A rate representing this Limit.
    rate = resource.prop("rate")
    #: A list of absolute props of the Limit.
    absolute = resource.prop("absolute")
