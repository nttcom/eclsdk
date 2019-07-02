# -*- coding: utf-8 -*-

from . import base
from ecl.network import network_service
from ecl import resource2


class ColocationLogicalLink(base.NetworkBaseResource):
    resource_key = 'colocation_logical_link'
    resources_key = 'colocation_logical_links'
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/colocation_logical_links'

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True

    # query mappings
    _query_mapping = resource2.QueryParameters('bandwidth',
                                               'colocation_physical_link_id',
                                               'description',
                                               'id',
                                               'name',
                                               'network_id',
                                               'status',
                                               'tenant_id',
                                               'type_a_port_id',
                                               'type_b_port_id',
                                               'vlan_id',
                                               "sort_key", "sort_dir",)

    # properties
    #: Colocation Physical Link ID.
    colocation_physical_link_id = resource2.Body('colocation_physical_link_id')
    #: Colocation Logical Link description.
    description = resource2.Body('description')
    #: Colocation Logical Link unique id.
    id = resource2.Body('id')
    #: Colocation Logical Link name.
    name = resource2.Body('name')
    #: Network connected to this link.
    network_id = resource2.Body('network_id')
    #: The Colocation Logical Link status.
    status = resource2.Body('status')
    #: Colocation Logical Link tags.
    tags = resource2.Body('tags')
    #: The owner name of Colocation Logical Link.
    tenant_id = resource2.Body('tenant_id')
    #: Type A Port ID.
    type_a_port_id = resource2.Body('type_a_port_id')
    #: Type B Port ID.
    type_b_port_id = resource2.Body('type_b_port_id')
    #: Logical port vlan id.
    vlan_id = resource2.Body('vlan_id')
