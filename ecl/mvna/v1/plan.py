from . import base

from ecl import resource2
from ecl.mvna import mvna_service


class Plan(resource2.Resource):
    resource_key = "plan"
    resources_key = "plans"
    service = mvna_service.MVNAService("v1.0")
    base_path = '/' + service.version + '/plans'

    _query_mapping = base.MVNAQueryParameters(
        "id",
        "name",
        "description",
        "bandwidth",
        "redundancy",
        "max_number_of_interfaces",
        "max_number_of_health_monitors",
        "max_number_of_listeners",
        "max_number_of_policies",
        "max_number_of_routes",
        "max_number_of_target_groups",
        "max_number_of_rules",
        "max_number_of_conditions",
        "max_number_of_members",
        "enabled"
    )

    # Capabilities
    allow_list = True
    allow_get = True
    allow_create = False
    allow_update = False
    allow_delete = False
    patch_update = False

    # Properties
    #: It identifies connection resource uniquely
    id = resource2.Body('id')
    #: Name of plan
    name = resource2.Body('name')
    #: Description of plan
    description = resource2.Body('description')
    #: Bandwidth of plan
    bandwidth = resource2.Body('bandwidth')
    #: Redundancy of plan
    redundancy = resource2.Body('redundancy')
    #: Max number of interfaces
    max_number_of_interfaces = resource2.Body('max_number_of_interfaces')
    #: Max number of health monitors
    max_number_of_health_monitors = \
        resource2.Body('max_number_of_health_monitors')
    #: Max number of listeners
    max_number_of_listeners = resource2.Body('max_number_of_listeners')
    #: Max number of policies
    max_number_of_policies = resource2.Body('max_number_of_policies')
    #: Max numbers of routes
    max_number_of_routes = resource2.Body('max_number_of_routes')
    #: Max number of target groups
    max_number_of_target_groups = resource2.Body('max_number_of_target_groups')
    #: Max number of rules
    max_number_of_rules = resource2.Body('max_number_of_rules')
    #: Max number of conditions
    max_number_of_conditions = resource2.Body('max_number_of_conditions')
    #: Max number of members
    max_number_of_members = resource2.Body('max_number_of_members')
    #: Enabled or disabled
    enabled = resource2.Body('enabled')
