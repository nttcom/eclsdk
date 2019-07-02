# -*- coding: utf-8 -*-

from . import base
from ecl.virtual_network_appliance import virtual_network_appliance_service
from ecl import resource2


class VirtualNetworkAppliancePlan(base.VirtualNetworkApplianceBaseResource):
    resources_key = "virtual_network_appliance_plans"
    resource_key = "virtual_network_appliance_plan"
    service = virtual_network_appliance_service.\
        VirtualNetworkApplianceService("v1.0")
    base_path = '/' + service.version + '/virtual_network_appliance_plans'

    # Capabilities
    allow_list = True
    allow_get = True

    _query_mapping = resource2.QueryParameters("details")

    # Properties
    #: It identifies connection resource uniquely.
    id = resource2.Body('id')
    #: Name of virtual network appliance plan.
    name = resource2.Body('name')
    #: Description of virtual network appliance plan.
    description = resource2.Body('description')
    #: Appliance type of virtual network appliance plan.
    appliance_type = resource2.Body('appliance_type')
    #: Version of virtual network appliance plan.
    version = resource2.Body('version')
    #: Flavor of virtual network appliance plan.
    flavor = resource2.Body('flavor')
    #: Number of interfaces of virtual network appliance plan.
    number_of_interfaces = resource2.Body('number_of_interfaces')
    #: Enable flag of virtual network appliance plan.
    enabled = resource2.Body('enabled')
    #: Max number of allowed address pairs of virtual network appliance plan.
    max_number_of_aap = resource2.Body('max_number_of_aap')
    #: License information of virtual network appliance plan.
    licenses = resource2.Body('licenses')
    #: Available zone/group information of virtual network appliance plan.
    availability_zones = resource2.Body('availability_zones')
