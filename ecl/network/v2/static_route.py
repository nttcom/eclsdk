# -*- coding: utf-8 -*-


from ecl.network import network_service
from ecl.network.v2.base import NetworkBaseResource
from ecl import resource2


class StaticRoute(NetworkBaseResource):

    resource_key = "static_route"
    resources_key = "static_routes"
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/static_routes'

    allow_list = True
    allow_get = True
    allow_create = True
    allow_delete = True
    allow_update = True

    _query_mapping = resource2.QueryParameters(
        "description", "id", "destination",
        "name", "interdc_gw_id", "internet_gw_id",
        "nexthop", "service_type", "status", "tenant_id",
        "vpn_gw_id", "sort_key", "sort_dir", "aws_gw_id",
        "azure_gw_id", "gcp_gw_id", "fic_gw_id",
    )

    description = resource2.Body("description")
    destination = resource2.Body("destination")
    id = resource2.Body("id")
    interdc_gw_id = resource2.Body("interdc_gw_id")
    internet_gw_id = resource2.Body("internet_gw_id")
    name = resource2.Body("name")
    nexthop = resource2.Body("nexthop")
    service_type = resource2.Body("service_type")
    status = resource2.Body("status")
    tenant_id = resource2.Body("tenant_id")
    vpn_gw_id = resource2.Body("vpn_gw_id")
    aws_gw_id = resource2.Body("aws_gw_id")
    gcp_gw_id = resource2.Body("gcp_gw_id")
    azure_gw_id = resource2.Body("azure_gw_id")
    fic_gw_id = resource2.Body("fic_gw_id")

    def wait_for_create(self, session, status='ACTIVE', failures=['ERROR'],
                         interval=2, wait=120):
        return resource2.wait_for_status(session, self, status,
                                         failures, interval, wait)

