from . import base

from ecl import resource2
from ecl.mvna import mvna_service


class Listener(base.MVNABaseResource):
    resource_key = "listener"
    resources_key = "listeners"
    service = mvna_service.MVNAService("v1.0")
    base_path = '/' + service.version + '/listeners'

    _query_mapping = base.MVNAQueryParameters(
        "id",
        "name",
        "description",
        "configuration_status",
        "operation_status",
        "ip_address",
        "port",
        "protocol",
        "load_balancer_id",
        "tenant_id"
    )

    # Capabilities
    allow_list = True
    allow_get = True
    allow_create = True
    allow_update = True
    allow_delete = True
    patch_update = True

    # Properties
    #: It identifies connection resource uniquely
    id = resource2.Body('id')
    #: Name of listener
    name = resource2.Body('name')
    #: Description of listener
    description = resource2.Body('description')
    #: Tags of listener
    tags = resource2.Body('tags')
    #: Configuration status of listener
    configuration_status = resource2.Body('configuration_status')
    #: Operation status of listener
    operation_status = resource2.Body('operation_status')
    #: IP Address of listener
    ip_address = resource2.Body('ip_address')
    #: Port of listener
    port = resource2.Body('port')
    #: Protocol of listener
    protocol = resource2.Body('protocol')
    #: Load balancer ID of listener
    load_balancer_id = resource2.Body('load_balancer_id')
    #: Tenant ID of listener
    tenant_id = resource2.Body('tenant_id')
    #: Current configuration of listener
    current = resource2.Body('current')
    #: Staged configuration of listener
    staged = resource2.Body('staged')
