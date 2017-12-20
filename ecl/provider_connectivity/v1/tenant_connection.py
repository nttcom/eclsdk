# -*- coding: utf-8 -*-

from ecl.provider_connectivity import provider_connectivity_service
from ecl.provider_connectivity.v1.base import TenantConnectionBaseResource
from ecl import resource2


class TenantConnection(TenantConnectionBaseResource):
    resources_key = "tenant_connections"
    resource_key = "tenant_connection"
    service = provider_connectivity_service.ProviderConnectivityService("v2.0")
    base_path = '/' + service.version + '/tenant_connections'

    # Capabilities
    allow_list = True
    allow_get = True
    allow_create = True
    allow_update = True
    allow_delete = True

    id = resource2.Body("id")

    tenant_connection_id = resource2.Body("id")

    tenant_connection_request_id = resource2.Body(
        "tenant_connection_request_id")

    name = resource2.Body("name")

    description = resource2.Body("description")

    tags = resource2.Body("tags")

    tenant_id = resource2.Body("tenant_id")

    name_other = resource2.Body("name_other")

    description_other = resource2.Body("description_other")

    tags_other = resource2.Body("tags_other")

    tenant_id_other = resource2.Body("tenant_id_other")

    network_id = resource2.Body("network_id")

    device_type = resource2.Body("device_type")

    device_id = resource2.Body("device_id")

    device_interface_id = resource2.Body("device_interface_id")

    attachment_opts = resource2.Body("attachment_opts")

    port_id = resource2.Body("port_id")

    status = resource2.Body("status")
