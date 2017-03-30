# -*- coding: utf-8 -*-

from ecl.network import network_service
from ecl.network.v2.base import NetworkBaseResource
from ecl import resource2
from ecl import exceptions


class AWSService(NetworkBaseResource):

    resource_key = "aws_service"
    resources_key = "aws_services"
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/aws_services'

    allow_list = True
    allow_get = True

    description = resource2.Body("description")
    id = resource2.Body("id")
    zone = resource2.Body("zone")
    name = resource2.Body("name")


class AWSGateway(NetworkBaseResource):

    resource_key = "aws_gateway"
    resources_key = "aws_gateways"
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/aws_gateways'

    allow_list = True
    allow_get = True

    description = resource2.Body("description")
    id = resource2.Body("id")
    aws_service_id = resource2.Body("aws_service_id")
    name = resource2.Body("name")
    qos_option_id = resource2.Body("qos_option_id")
    status = resource2.Body("status")
    tenant_id = resource2.Body("tenant_id")


class AWSInterface(NetworkBaseResource):

    resource_key = "aws_interface"
    resources_key = "aws_interfaces"
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/aws_interfaces'

    allow_list = True
    allow_get = True

    aws_gw_id = resource2.Body("aws_gw_id")
    description = resource2.Body("description")
    id = resource2.Body("id")
    name = resource2.Body("name")
    status = resource2.Body("status")
    tenant_id = resource2.Body("tenant_id")
    primary = resource2.Body("primary")
    secondary = resource2.Body("secondary")
