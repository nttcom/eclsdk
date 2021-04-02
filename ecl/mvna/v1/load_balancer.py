from . import base

from ecl import resource2
from ecl.mvna import mvna_service


class LoadBalancer(base.MVNABaseResource):
    resource_key = "load_balancer"
    resources_key = "load_balancers"
    service = mvna_service.MVNAService("v1.0")
    base_path = '/' + service.version + '/load_balancers'

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
    #: Name of load balancer
    name = resource2.Body('name')
    #: Description of load balancer
    description = resource2.Body('description')
    #: Tags of load balancer
    tags = resource2.Body('tags')
    #: Configuration status of load balancer
    configuration_status = resource2.Body('configuration_status')
    #: Monitoring status of load balancer
    monitoring_status = resource2.Body('monitoring_status')
    #: Operation status of load balancer
    operation_status = resource2.Body('operation_status')
    #: Availability zones of load balancer
    availability_zones = resource2.Body('availability_zones')
    #: Default gateway of load balancer
    default_gateway = resource2.Body('default_gateway')
    #: Revision of load balancer
    revision = resource2.Body('revision')
    #: Plan ID of load balancer
    plan_id = resource2.Body('plan_id')
    #: Tenant ID of load balancer
    tenant_id = resource2.Body('tenant_id')
    #: Syslog servers of load balancer
    syslog_servers = resource2.Body('syslog_servers')
    #: Interfaces of load balancer
    interfaces = resource2.Body('interfaces')
    #: Current configuration of load balancer
    current = resource2.Body('current')
    #: Staged configuration of load balancer
    staged = resource2.Body('staged')

    def action(self, session, resource_id, **body):
        uri = self.base_path + '/%s/action' % resource_id
        session.post(uri, endpoint_filter=self.service, json=body)
