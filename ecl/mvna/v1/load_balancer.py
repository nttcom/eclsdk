from . import base

from ecl import exceptions
from ecl import resource2
from ecl.mvna import mvna_service


class LoadBalancer(base.MVNABaseResource):
    resource_key = "load_balancer"
    resources_key = "load_balancers"
    service = mvna_service.MVNAService("v1.0")
    base_path = '/' + service.version + '/load_balancers'

    _query_mapping = resource2.QueryParameters(
        "id",
        "name",
        "description",
        "configuration_status",
        "monitoring_status",
        "operation_status",
        "availability_zone",
        "default_gateway",
        "revision",
        "plan_id",
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

    def delete_resource(self, session, resource_id, x_mvna_request_id=None,
                        ignore_missing=False):
        uri = self.base_path + '/%s' % resource_id

        try:
            if x_mvna_request_id:
                resp = session.delete(
                    uri, endpoint_filter=self.service,
                    headers={"X-MVNA-Request-Id": x_mvna_request_id})
            else:
                resp = session.delete(uri, endpoint_filter=self.service)
        except exceptions.NotFoundException:
            if ignore_missing:
                return None
            raise exceptions.ResourceNotFound(
                message="No %s found for %s" %
                        (self.__class__.__name__, resource_id))

        self._translate_response(resp, has_body=False)
        return self

    def action(self, session, resource_id, x_mvna_request_id=None, **body):
        uri = self.base_path + '/%s/action' % resource_id
        if x_mvna_request_id:
            session.post(uri, endpoint_filter=self.service,
                         headers={"X-MVNA-Request-Id": x_mvna_request_id},
                         json=body)
        else:
            session.post(uri, endpoint_filter=self.service, json=body)
