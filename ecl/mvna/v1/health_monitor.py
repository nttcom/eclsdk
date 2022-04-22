from . import base

from ecl import resource2
from ecl.mvna import mvna_service


class HealthMonitor(base.MVNABaseResource):
    resource_key = "health_monitor"
    resources_key = "health_monitors"
    service = mvna_service.MVNAService("v1.0")
    base_path = '/' + service.version + '/health_monitors'

    _query_mapping = base.MVNAQueryParameters(
        "id",
        "name",
        "description",
        "configuration_status",
        "operation_status",
        "port",
        "protocol",
        "interval",
        "retry",
        "timeout",
        "path",
        "http_status_code",
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
    #: Name of health monitor
    name = resource2.Body('name')
    #: Description of health monitor
    description = resource2.Body('description')
    #: Tags of health monitor
    tags = resource2.Body('tags')
    #: Configuration status of health monitor
    configuration_status = resource2.Body('configuration_status')
    #: Operation status of health monitor
    operation_status = resource2.Body('operation_status')
    #: Port of health monitor
    port = resource2.Body('port')
    #: Protocol of health monitor
    protocol = resource2.Body('protocol')
    #: Interval of health monitor
    interval = resource2.Body('interval')
    #: Retry count of health monitor
    retry = resource2.Body('retry')
    #: Timeout of health monitor
    timeout = resource2.Body('timeout')

    #: Path of health monitor
    path = resource2.Body('path')
    #: HTTP status code of health monitor
    http_status_code = resource2.Body('http_status_code')

    #: Load balancer ID
    load_balancer_id = resource2.Body('load_balancer_id')
    #: Tenant ID of health monitor
    tenant_id = resource2.Body('tenant_id')
    #: Current configuration of health monitor
    current = resource2.Body('current')
    #: Staged configuration of health monitor
    staged = resource2.Body('staged')
