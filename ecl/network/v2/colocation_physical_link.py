# -*- coding: utf-8 -*-

from . import base
from ecl.network import network_service
from ecl import resource2


class ColocationPhysicalLink(base.NetworkBaseResource):
    resource_key = 'colocation_physical_link'
    resources_key = 'colocation_physical_links'
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/colocation_physical_links'

    # capabilities
    allow_get = True
    allow_list = True

    # query mappings
    _query_mapping = resource2.QueryParameters('bandwidth',
                                               'colocation_space_id',
                                               'description',
                                               'id',
                                               'name',
                                               'status',
                                               'tenant_id',
                                               'type_a_physical_port_id',
                                               'type_a_rack_id',
                                               'type_b_physical_port_id',
                                               'type_b_rack_id',
                                               'colocation_physical_link_id',
                                               "sort_key", "sort_dir",)

    # properties
    #: The bandwidth of Colocation Physical Link.
    bandwidth = resource2.Body('bandwidth')
    #: Colocation Space ID.
    colocation_space_id = resource2.Body('colocation_space_id')
    #: Colocation Physical Link description.
    description = resource2.Body('description')
    #: Colocation Physical Link unique id.
    id = resource2.Body('id')
    #: Colocation Physical Link name.
    name = resource2.Body('name')
    #: Ranges of allowed VLAN tags.
    segmentation_ranges = resource2.Body('segmentation_ranges')
    #: The Colocation Physical Link status.
    status = resource2.Body('status')
    #: Colocation Physical Link tags.
    tags = resource2.Body('tags')
    #: The owner name of Colocation Physical Link.
    tenant_id = resource2.Body('tenant_id')
    #: Type A Physical Port ID.
    type_a_physical_port_id = resource2.Body('type_a_physical_port_id')
    #: Type A Rack ID.
    type_a_rack_id = resource2.Body('type_a_rack_id')
    #: Type B Physical Port ID.
    type_b_physical_port_id = resource2.Body('type_b_physical_port_id')
    #: Type B Rack ID.
    type_b_rack_id = resource2.Body('type_b_rack_id')
