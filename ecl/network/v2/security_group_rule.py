# -*- coding: utf-8 -*-

from ecl.network import network_service
from ecl import resource2


class SecurityGroupRule(resource2.Resource):
    """SecurityGroupRule Resource"""
    resource_key = 'security_group_rule'
    resources_key = 'security_group_rules'
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/security-group-rules'

    # capabilities
    allow_list = True
    allow_create = True
    allow_get = True
    allow_delete = True

    # Properties
    # Security group rule description.
    description = resource2.Body('description')
    # Direction in which the security group rule is applied.
    direction = resource2.Body('direction')
    # Addresses represented in CIDR must match the ingress or egress rules.
    ethertype = resource2.Body('ethertype')
    # Security group rule unique id.
    id = resource2.Body('id')
    # The maximum port number in the range that is matched
    # by the security group rule.
    port_range_max = resource2.Body('port_range_max', type=int)
    # The minimum port number in the range that is matched
    # by the security group rule.
    port_range_min = resource2.Body('port_range_min', type=int)
    # Protocol name or number in string format. e.g. "ICMP" or "1"
    protocol = resource2.Body('protocol')
    # The remote group UUID to associate with this security group rule. Only
    # either one of remote_group_id and remote_ip_prefix have to be specified.
    remote_group_id = resource2.Body('remote_group_id')
    # The IP address prefix to associate with this security group rule. Only
    # either one of remote_group_id and remote_ip_prefix have to be specified.
    remote_ip_prefix = resource2.Body('remote_ip_prefix')
    # Security group id.
    security_group_id = resource2.Body('security_group_id')
    # The owner name of security group rule.
    tenant_id = resource2.Body('tenant_id')
