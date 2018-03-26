# -*- coding: utf-8 -*-

from ecl.network import network_service
from ecl.network.v2.base import NetworkBaseResource
from ecl import resource2
from ecl import exceptions


class GCPService(NetworkBaseResource):

    resource_key = "gcp_service"
    resources_key = "gcp_services"
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/gcp_services'

    allow_list = True
    allow_get = True

    #: Description of the GCP Service resource.
    description = resource2.Body("description")
    #: Unique ID of the GCP Service resource.
    id = resource2.Body("id")
    #: Name of zone.
    zone = resource2.Body("zone")
    #: Name of the GCP Service resource.
    name = resource2.Body("name")


class GCPGateway(NetworkBaseResource):

    resource_key = "gcp_gateway"
    resources_key = "gcp_gateways"
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/gcp_gateways'

    allow_list = True
    allow_get = True

    #: Description of the GCP Gateway resource.
    description = resource2.Body("description")
    #: Unique ID of the GCP Gateway resource.
    id = resource2.Body("id")
    #: GCP Service instantiated by this Gateway.
    gcp_service_id = resource2.Body("gcp_service_id")
    #: Name of the GCP Gateway resource.
    name = resource2.Body("name")
    #: Quality of Service options selected for this Gateway.
    qos_option_id = resource2.Body("qos_option_id")
    #: The GCP Gateway status.
    status = resource2.Body("status")
    #: Tenant ID of the owner (UUID)
    tenant_id = resource2.Body("tenant_id")


class GCPInterface(NetworkBaseResource):

    resource_key = "gcp_interface"
    resources_key = "gcp_interfaces"
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/gcp_interfaces'

    allow_list = True
    allow_get = True

    #: GCP Gateway to which this interface is connected.
    gcp_gw_id = resource2.Body("gcp_gw_id")
    #: Description of the GCP Interface resource.
    description = resource2.Body("description")
    #: Unique ID of the GCP Interface resource.
    id = resource2.Body("id")
    #: Name of the GCP Interface resource
    name = resource2.Body("name")
    #: The GCP Interface status.
    status = resource2.Body("status")
    #: Tenant ID of the owner (UUID)
    tenant_id = resource2.Body("tenant_id")
    #: Primary router uplink ip configuration.
    primary = resource2.Body("primary")
    #: Secondary router uplink ip configuration.
    secondary = resource2.Body("secondary")
