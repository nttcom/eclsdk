# -*- coding: utf-8 -*-

from ecl.block_store import block_store_service
from ecl import resource


class Metadata(resource.Resource):
    resource_key = "metadata"
    resources_key = "metadata"
    base_path = "/volumes/%(volume_id)s/metadata"
    service = block_store_service.BlockStoreService()

    # capabilities
    allow_list = True
    allow_create = True
    allow_update = True
