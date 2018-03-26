# -*- coding: utf-8 -*-

from ecl.provider_connectivity import provider_connectivity_service
from ecl.provider_connectivity.v2.base import ProviderConnectivityBaseResource
from ecl import resource2


class AWSConnection(ProviderConnectivityBaseResource):
    resources_key = "aws_connections"
    resource_key = "aws_connection"
    service = provider_connectivity_service.ProviderConnectivityService("v2.0")
    base_path = '/' + service.version + '/aws_connections'

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
    #: Tenant ID of the owner.
    tenant_id = resource2.Body('tenant_id')
    #: Bandwidth assigned with this connection.
    bandwidth = resource2.Body('bandwidth')
    #: QoS type assigned with this connection.
    qos_type = resource2.Body('qos_type')
    #: ID of exchange_points.
    exchange_point_id = resource2.Body('exchange_point_id')
    aws_account_id = resource2.Body('aws_account_id')
    connected_network_address = resource2.Body('connected_network_address')
    #: Network params between ECL2.0 and UNO.
    aws_network1 = resource2.Body('aws_network1')
    #: Network params between UNO and AWS.
    aws_network2 = resource2.Body('aws_network2')

    def approve(self, session, connection_id, action):
        """Approve/Disapprove connection between ECL2.0 and AWS."""

        uri = self.base_path + '/' + connection_id + '/action'
        resp = session.put(uri,
                           endpoint_filter=self.service,
                           json={"action": action})
        self._translate_response(resp, has_body=False)
        return self
