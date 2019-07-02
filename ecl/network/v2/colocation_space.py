# -*- coding: utf-8 -*-

from . import base
from ecl.network import network_service
from ecl import resource2


class ColocationSpace(base.NetworkBaseResource):
    resource_key = 'colocation_space'
    resources_key = 'colocation_spaces'
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/colocation_spaces'

    # capabilities
    allow_get = True
    allow_list = True

    # query mappings
    _query_mapping = resource2.QueryParameters('description', 'id', 'name',
                                               "sort_key", "sort_dir",)

    # properties
    #: Colocation Space description.
    description = resource2.Body('description')
    #: Colocation Space unique id.
    id = resource2.Body('id')
    #: Colocation Space name.
    name = resource2.Body('name')
