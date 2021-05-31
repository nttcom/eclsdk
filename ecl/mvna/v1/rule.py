from . import base

from ecl import resource2
from ecl.mvna import mvna_service


class Rule(base.MVNABaseResource):
    resource_key = "rule"
    resources_key = "rules"
    service = mvna_service.MVNAService("v1.0")
    base_path = '/' + service.version + '/rules'

    _query_mapping = base.MVNAQueryParameters(
        "id",
        "name",
        "description",
        "configuration_status",
        "operation_status",
        "priority",
        "target_group_id",
        "policy_id",
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
    #: Name of rule
    name = resource2.Body('name')
    #: Description of rule
    description = resource2.Body('description')
    #: Tags of rule
    tags = resource2.Body('tags')
    #: Configuration status of rule
    configuration_status = resource2.Body('configuration_status')
    #: Operation status of rule
    operation_status = resource2.Body('operation_status')
    #: Priority of rule
    priority = resource2.Body('priority')
    #: Target group ID of rule
    target_group_id = resource2.Body('target_group_id')
    #: Policy ID of rule
    policy_id = resource2.Body('policy_id')
    #: Load balancer ID of rule
    load_balancer_id = resource2.Body('load_balancer_id')
    #: Tenant ID of rule
    tenant_id = resource2.Body('tenant_id')
    #: Conditions of rule
    conditions = resource2.Body('conditions')
    #: Current configuration of rule
    current = resource2.Body('current')
    #: Staged configuration of rule
    staged = resource2.Body('staged')
