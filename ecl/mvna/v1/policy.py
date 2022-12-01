from . import base

from ecl import resource2
from ecl.mvna import mvna_service


class Policy(base.MVNABaseResource):
    resource_key = "policy"
    resources_key = "policies"
    service = mvna_service.MVNAService("v1.0")
    base_path = '/' + service.version + '/policies'

    _query_mapping = base.MVNAQueryParameters(
        "id",
        "name",
        "description",
        "configuration_status",
        "operation_status",
        "algorithm",
        "persistence",
        "sorry_page_url",
        "source_nat",
        "certificate_id",
        "health_monitor_id",
        "listener_id",
        "default_target_group_id",
        "tls_policy_id",
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
    #: Name of policy
    name = resource2.Body('name')
    #: Description of policy
    description = resource2.Body('description')
    #: Tags of policy
    tags = resource2.Body('tags')
    #: Configuration status of policy
    configuration_status = resource2.Body('configuration_status')
    #: Operation status of policy
    operation_status = resource2.Body('operation_status')
    #: Algorithm of policy
    algorithm = resource2.Body('algorithm')
    #: persistence of policy
    persistence = resource2.Body('persistence')

    #: Sorry page URL of policy
    sorry_page_url = resource2.Body('sorry_page_url')
    #: Source NAT of policy
    source_nat = resource2.Body('source_nat')
    #: Certificate ID of policy
    certificate_id = resource2.Body('certificate_id')
    #: TLS policy ID of policy
    tls_policy_id = resource2.Body('tls_policy_id')

    #: Health monitor ID of policy
    health_monitor_id = resource2.Body('health_monitor_id')
    #: Listener ID of policy
    listener_id = resource2.Body('listener_id')
    #: Default target group ID of policy
    default_target_group_id = resource2.Body('default_target_group_id')
    #: Load balancer ID of policy
    load_balancer_id = resource2.Body('load_balancer_id')
    #: Tenant ID of policy
    tenant_id = resource2.Body('tenant_id')
    #: Current configuration of policy
    current = resource2.Body('current')
    #: Staged configuration of policy
    staged = resource2.Body('staged')
