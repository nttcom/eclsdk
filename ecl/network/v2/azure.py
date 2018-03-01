# -*- coding: utf-8 -*-

from ecl.network import network_service
from ecl.network.v2.base import NetworkBaseResource
from ecl import resource2
from ecl import exceptions


class AzureService(NetworkBaseResource):

    resource_key = "azure_service"
    resources_key = "azure_services"
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/azure_services'

    allow_list = True
    allow_get = True

    description = resource2.Body("description")
    id = resource2.Body("id")
    zone = resource2.Body("zone")
    name = resource2.Body("name")


class AzureGateway(NetworkBaseResource):

    resource_key = "azure_gateway"
    resources_key = "azure_gateways"
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/azure_gateways'

    allow_list = True
    allow_get = True

    description = resource2.Body("description")
    id = resource2.Body("id")
    azure_service_id = resource2.Body("azure_service_id")
    name = resource2.Body("name")
    qos_option_id = resource2.Body("qos_option_id")
    status = resource2.Body("status")
    tenant_id = resource2.Body("tenant_id")


class AzureInterface(NetworkBaseResource):

    resource_key = "azure_interface"
    resources_key = "azure_interfaces"
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/azure_interfaces'

    allow_list = True
    allow_get = True

    _query_mapping = resource2.QueryParameters(
        "azure_gw_id",
    )

    azure_gw_id = resource2.Body("azure_gw_id")
    description = resource2.Body("description")
    id = resource2.Body("id")
    name = resource2.Body("name")
    status = resource2.Body("status")
    tenant_id = resource2.Body("tenant_id")
    primary = resource2.Body("primary")
    secondary = resource2.Body("secondary")
