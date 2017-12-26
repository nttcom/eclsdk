# -*- coding: utf-8 -*-

import base
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

    # _query_mapping = resource2.QueryParameters()
    # TBD

    # Properties
    #: It identifies connection resource uniquely.
    id = resource2.Body('id')
    #: Name of network appliance plan.
    name = resource2.Body('name')
    #: Description of network appliance plan.
    description = resource2.Body('description')
    #: Appliance type of network appliance plan.
    appliance_type = resource2.Body('appliance_type')
    #: Version of network appliance plan.
    version = resource2.Body('version')
    #: Flavor of network appliance plan.
    flavor = resource2.Body('flavor')
    #: Number of interfaces of network appliance plan.
    number_of_interfaces = resource2.Body('number_of_interfaces')
    #: Enable flag of network appliance plan
    enabled = resource2.Body('enabled')
    #: Max number of allowed address pair of network appliance plan.
    max_number_of_aap = resource2.Body('max_number_of_aap')
    #: License information of interfaces of network appliance plan.
    licenses = resource2.Body('licenses')
