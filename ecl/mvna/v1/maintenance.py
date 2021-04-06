from ecl import resource2
from ecl.mvna import mvna_service


class Maintenance(resource2.Resource):
    resource_key = "maintenance"
    resources_key = "maintenances"
    service = mvna_service.MVNAService("v1.0")
    base_path = '/' + service.version + '/maintenances'

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
    #: Name of maintenance
    name = resource2.Body('name')
    #: Description of maintenance
    description = resource2.Body('description')
    #: href of maintenance
    href = resource2.Body('href')
    #: Publish datetime of maintenance
    publish_datetime = resource2.Body('publish_datetime')
    #: Limit datetime of maintenance
    limit_datetime = resource2.Body('limit_datetime')
    #: Current revision of maintenance
    current_revision = resource2.Body('current_revision')
    #: Next revision of maintenance
    next_revision = resource2.Body('next_revision')
    #: Applicable of maintenance
    applicable = resource2.Body('applicable')
