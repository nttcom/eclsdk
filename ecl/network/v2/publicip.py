# -*- coding: utf-8 -*-


from ecl.network import network_service
from ecl.network.v2.base import NetworkBaseResource
from ecl import resource2


class PublicIP(NetworkBaseResource):

    resource_key = "public_ip"
    resources_key = "public_ips"
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/public_ips'

    _query_mapping = resource2.QueryParameters(
        "cidr", "description", "id", "internet_gw_id",
        "name", "status", "submask_length", "tenant_id",
        "sort_key", "sort_dir",
    )

    allow_list = True
    allow_get = True
    allow_create = True
    allow_delete = True
    allow_update = True

    cidr = resource2.Body("cidr")
    description = resource2.Body("description")
    id = resource2.Body("id")
    internet_gw_id = resource2.Body("internet_gw_id")
    name = resource2.Body("name")
    status = resource2.Body("status")
    submask_length = resource2.Body("submask_length", int)
    tenant_id = resource2.Body("tenant_id")

    def wait_for_publicip(self, session, status='ACTIVE', failures=['ERROR'],
                          interval=2, wait=120):
        return resource2.wait_for_status(session, self, status,
                                         failures, interval, wait)
