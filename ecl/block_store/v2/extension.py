# -*- coding: utf-8 -*-

from ecl.block_store import block_store_service
from ecl import resource


class Extension(resource.Resource):
    resource_key = "extension"
    resources_key = "extensions"
    base_path = "/extensions"
    service = block_store_service.BlockStoreService()

    # capabilities
    allow_list = True

    # Properties
    #: A updated representing this Extension.
    updated = resource.prop("updated")
    #: Name of the extension.
    name = resource.prop("name")
    #: A list of links.
    links = resource.prop("links", type=list)
    #: Namespace of the extension.
    namespace = resource.prop("namespace")
    #: Alias of the extension.
    alias = resource.prop("alias")
    #: Description of the extension.
    description = resource.prop("description")

