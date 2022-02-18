from . import base

from ecl import resource2
from ecl.mvna import mvna_service


class TargetGroup(base.MVNABaseResource):
    resource_key = "target_group"
    resources_key = "target_groups"
    service = mvna_service.MVNAService("v1.0")
    base_path = '/' + service.version + '/target_groups'

    _query_mapping = base.MVNAQueryParameters(
        "id",
        "name",
        "description",
        "configuration_status",
        "operation_status",
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
    #: Name of target group
    name = resource2.Body('name')
    #: Description of target group
    description = resource2.Body('description')
    #: Tags of target group
    tags = resource2.Body('tags')
    #: Configuration status of target group
    configuration_status = resource2.Body('configuration_status')
    #: Operation status of target group
    operation_status = resource2.Body('operation_status')
    #: Load balancer ID of target group
    load_balancer_id = resource2.Body('load_balancer_id')
    #: Tenant ID of target group
    tenant_id = resource2.Body('tenant_id')
    #: Members of target group
    members = resource2.Body('members')
    #: Current of target group
    current = resource2.Body('current')
    #: Staged of target group
    staged = resource2.Body('staged')
