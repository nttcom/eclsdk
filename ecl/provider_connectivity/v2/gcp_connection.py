# -*- coding: utf-8 -*-

from ecl.provider_connectivity import provider_connectivity_service
from ecl.provider_connectivity.v2.base import ProviderConnectivityBaseResource
from ecl import resource2


class GCPConnection(ProviderConnectivityBaseResource):
    resources_key = "gcp_connections"
    resource_key = "gcp_connection"
    service = provider_connectivity_service.ProviderConnectivityService("v2.0")
    base_path = '/' + service.version + '/gcp_connections'

    # Capabilities
    allow_list = True
    allow_get = True
    allow_create = True
    allow_update = True
    allow_delete = True

    # _query_mapping = resource2.QueryParameters()
    # TBD

    # Properties
    #: It identifies connection resource uniquely.
    id = resource2.Body('id')
    #: Name of connection.
    name = resource2.Body('name')
    #: Description of connection.
    description = resource2.Body('description')
    #: Status of connection.
    status = resource2.Body('status')
    #: Status of operation for gcp_connection.
    operation_status = resource2.Body('operation_status')
    #: Pairing Key for Active Cloud Router in GCP.
    pairing_key_primary = resource2.Body('pairing_key_primary')
    #: Pairing Key for Standby Cloud Router in GCP.
    pairing_key_secondary = resource2.Body('pairing_key_secondary')
    #: Tenant ID of the owner.
    tenant_id = resource2.Body('tenant_id')
    #: Bandwidth assigned with this connection.
    bandwidth = resource2.Body('bandwidth')
    #: QoS type assigned with this connection.
    qos_type = resource2.Body('qos_type')
    #: ID of exchange_points.
    exchange_point_id = resource2.Body('exchange_point_id')
    #: VLAN ID.
    vlan = resource2.Body('vlan')
    #: ID of gcp_gateway which gcp_connection connected.
    gcp_gateway_id = resource2.Body('gcp_gateway_id')
    #: ID of gcp_interface which gcp_connection connected.
    gcp_interface_id = resource2.Body('gcp_interface_id')
    #: Name of Region where customer's cloud router exist.
    gcp_region_name = resource2.Body('gcp_region_name')
