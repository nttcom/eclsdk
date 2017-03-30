# -*- coding: utf-8 -*-


from ecl.network import network_service
from ecl.network.v2.base import NetworkBaseResource
from ecl import resource2
from ecl import utils


class TenantConnection(NetworkBaseResource):
    resource_key = "tenant_connection"
    resources_key = "tenant_connections"

    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/tenant_connections'

    allow_list = True
    allow_get = True
    allow_create = True
    allow_delete = True
    allow_update = True

    _query_mapping = resource2.QueryParameters(
        "approval_request_id", "interface_type",
        "name", "description", "id", "progress",
        "tenant_id", "sort_key", "sort_dir",
    )

    approval_request_id = resource2.Body("approval_request_id")
    connected_interface = resource2.Body("connected_interface", dict)
    connected_network = resource2.Body("connected_network", dict)
    interface_type = resource2.Body("interface_type")
    description = resource2.Body("description")
    id = resource2.Body("id")
    name = resource2.Body("name")
    progress = resource2.Body("progress")
    tenant_id = resource2.Body("tenant_id")

    def execute(self, session):
        """Preform tenant connection execute."""
        url = utils.urljoin(TenantConnection.base_path, self.id, 'execute')
        headers = {'Accept': ''}
        return session.post(
            url, endpoint_filter=self.service, headers=headers)
