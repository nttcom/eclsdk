# -*- coding: utf-8 -*-

from ecl.network import network_service
from ecl import resource2


class Quota(resource2.Resource):
    resource_key = 'quota'
    resources_key = 'quotas'
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/quotas'

    # capabilities
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True

    # Properties
    #: The maximum amount of colocation logical link you can have. *Type: int*
    colocation_logical_link = resource2.Body('colocation_logical_link', type=int)
    #: The maximum amount of common function gateway you can create. *Type: int*
    common_function_gateway = resource2.Body('common_function_gateway', type=int)
    #: The maximum amount of fic gateway you can create. *Type: int*
    fic_gateway = resource2.Body('fic_gateway', type=int)
    #: The maximum amount of firewall you can create. *Type: int*
    firewall = resource2.Body('firewall', type=int)
    #: ID of quota
    id = resource2.Body("id")
    #: The maximum amount of interdc gateway you can create. *Type: int*
    interdc_gateway = resource2.Body('interdc_gateway', type=int)
    #: The maximum amount of internet gateway you can create. *Type: int*
    internet_gateway = resource2.Body('internet_gateway', type=int)
    #: The maximum amount of networks you can create. *Type: int*
    network = resource2.Body('network', type=int)
    #: The maximum amount of load balancer you can create. *Type: int*
    load_balancer = resource2.Body('load_balancer', type=int)
    #: The maximum amount of ports you can create. *Type: int*
    port = resource2.Body('port', type=int)
    #: The ID of the project these quota values are for.
    project_id = resource2.Body('tenant_id')
    #: The maximum amount of subnets you can create. *Type: int*
    subnet = resource2.Body('subnet', type=int)
    #: The maximum amount of vpn gateway you can create. *Type: int*
    vpn_gateway = resource2.Body('vpn_gateway', type=int)
    #: The maximum amount of public ip you can create. *Type: int*
    public_ip = resource2.Body('public_ip', type=int)


class QuotaDefault(Quota):
    base_path = '/quotas/%(project)s/default'

    # capabilities
    allow_retrieve = True
    allow_update = False
    allow_delete = False
    allow_list = False
