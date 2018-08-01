# -*- coding: utf-8 -*-

from ecl.provider_connectivity import provider_connectivity_service
from ecl.provider_connectivity.v2.base import ProviderConnectivityBaseResource
from ecl import resource2


class TenantConnection(ProviderConnectivityBaseResource):
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

    # query mappings
    _query_mapping = resource2.QueryParameters(
        'tenant_connection_id',
        'tenant_connection_request_id',
        'status',
        'name',
        'tenant_id',
        'name_other',
        'tenant_id_other',
        'network_id',
        'device_type',
        'device_id',
        'device_interface_id',
        'port_id'
    )

    #: tenant_connection unique ID.
    id = resource2.Body("id")

    #: tenant_connection unique ID.
    tenant_connection_id = resource2.Body("id")

    #: tenant_connection request ID.
    tenant_connection_request_id = resource2.Body(
        "tenant_connection_request_id")

    #: Name of tenant_connection.
    name = resource2.Body("name")

    #: Description
    description = resource2.Body("description")

    #: Tags
    tags = resource2.Body("tags")

    #: tenant_id
    tenant_id = resource2.Body("tenant_id")

    #: Name of network owner tenant
    name_other = resource2.Body("name_other")

    #: Description of network owner tenant
    description_other = resource2.Body("description_other")

    #: Tags of network owner tenant
    tags_other = resource2.Body("tags_other")

    #: Network owner tenant ID
    tenant_id_other = resource2.Body("tenant_id_other")

    #: Network ID
    network_id = resource2.Body("network_id")

    #: Device type, baremetal or virutal server
    device_type = resource2.Body("device_type")

    #: Device ID
    device_id = resource2.Body("device_id")

    #: Device interface ID
    device_interface_id = resource2.Body("device_interface_id")

    #: Attachment options of the connection
    attachment_opts = resource2.Body("attachment_opts")

    #: Port ID of the connection
    port_id = resource2.Body("port_id")

    #: Status of tenant_connection
    status = resource2.Body("status")
