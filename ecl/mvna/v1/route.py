from . import base

from ecl import resource2
from ecl.mvna import mvna_service


class Route(base.MVNABaseResource):
    resource_key = "route"
    resources_key = "routes"
    service = mvna_service.MVNAService("v1.0")
    base_path = '/' + service.version + '/routes'

    _query_mapping = base.MVNAQueryParameters(
        "id",
        "name",
        "description",
        "configuration_status",
        "operation_status",
        "destination_cidr",
        "next_hop_ip_address",
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
    #: Name of route
    name = resource2.Body('name')
    #: Description of route
    description = resource2.Body('description')
    #: Tags of route
    tags = resource2.Body('tags')
    #: Configuration status of route
    configuration_status = resource2.Body('configuration_status')
    #: Operation status of route
    operation_status = resource2.Body('operation_status')
    #: Destination cidr of route
    destination_cidr = resource2.Body('destination_cidr')
    #: Next hop ip address of route
    next_hop_ip_address = resource2.Body('next_hop_ip_address')
    #: Load balancer ID of route
    load_balancer_id = resource2.Body('load_balancer_id')
    #: Tenant ID of route
    tenant_id = resource2.Body('tenant_id')
    #: Current configuration of route
    current = resource2.Body('current')
    #: Staged configuration of route
    staged = resource2.Body('staged')
