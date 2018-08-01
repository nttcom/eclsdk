# -*- coding: utf-8 -*-

from ecl.provider_connectivity import provider_connectivity_service
from ecl.provider_connectivity.v1.base import ProviderConnectivityBaseResource
from ecl import resource2


class TenantConnectionRequest(ProviderConnectivityBaseResource):
    resources_key = "tenant_connection_requests"
    resource_key = "tenant_connection_request"
    service = provider_connectivity_service.ProviderConnectivityService("v2.0")
    base_path = '/' + service.version + '/tenant_connection_requests'

    # Capabilities
    allow_list = True
    allow_get = True
    allow_create = True
    allow_update = True
    allow_delete = True

    # query mappings
    _query_mapping = resource2.QueryParameters(
        'tenant_connection_request_id',
        'status',
        'name',
        'tenant_id',
        'name_other',
        'tenant_id_other',
        'network_id',
        'approval_request_id',
        'keystone_user_id',
    )

    #: tenant_connection_request unique ID.
    tenant_connection_request_id = resource2.Body(
        'tenant_connection_request_id', alternate_id=True)

    id = resource2.Body("id")

    #: Name of tenant_connection_request.
    name = resource2.Body('name')

    #: Description
    description = resource2.Body('description')

    #: Status of tenant_connection_request.
    status = resource2.Body('status')

    #: Tags
    tags = resource2.Body('tags')

    #: Keystone User ID who can access to the owner tenant of
    # tenant_connection_request.
    keystone_user_id = resource2.Body('keystone_user_id')

    #: Tenant ID of the owner.
    tenant_id = resource2.Body('tenant_id')

    #: Name for the owner of network
    name_other = resource2.Body('name_other')

    #: Description for the owner of the network
    description_other = resource2.Body('description_other')

    #: Tags for the owner of the network
    tags_other = resource2.Body('tags_other')

    #: The owner tenant of the network
    tenant_id_other = resource2.Body('tenant_id_other')

    #: Network unique ID
    network_id = resource2.Body('network_id')

    #: Approval unique ID
    approval_request_id = resource2.Body('approval_request_id')
