# -*- coding: utf-8 -*-

from ecl.network import network_service
from ecl import resource2


class SecurityGroup(resource2.Resource):
    """SecurityGroup Resource"""
    resource_key = 'security_group'
    resources_key = 'security_groups'
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/security-groups'

    # query parameter names
    _query_mapping = resource2.QueryParameters(
        'description', 'id', 'name', 'status', 'tenant_id')

    # capabilities
    allow_list = True
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True

    # Properties
    # Security group description.
    description = resource2.Body('description')
    # Security group unique id.
    id = resource2.Body('id')
    # Security group name.
    name = resource2.Body('name')
    # Security group status.
    status = resource2.Body('status')
    # Security Group tags.
    tags = resource2.Body('tags')
    # The owner name of security group.
    tenant_id = resource2.Body('tenant_id')
    # Security group rules
    security_group_rules = resource2.Body('security_group_rules', type=list)
