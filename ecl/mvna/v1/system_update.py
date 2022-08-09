from . import base

from ecl import resource2
from ecl.mvna import mvna_service


class SystemUpdate(resource2.Resource):
    resource_key = "system_update"
    resources_key = "system_updates"
    service = mvna_service.MVNAService("v1.0")
    base_path = '/' + service.version + '/system_updates'

    _query_mapping = base.MVNAQueryParameters(
        "id",
        "name",
        "description",
        "href",
        "current_revision",
        "next_revision",
        "applicable",
        "latest"
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
    #: Name of system update
    name = resource2.Body('name')
    #: Description of system update
    description = resource2.Body('description')
    #: href of system update
    href = resource2.Body('href')
    #: Publish datetime of system update
    publish_datetime = resource2.Body('publish_datetime')
    #: Limit datetime of system update
    limit_datetime = resource2.Body('limit_datetime')
    #: Current revision of system update
    current_revision = resource2.Body('current_revision')
    #: Next revision of system update
    next_revision = resource2.Body('next_revision')
    #: Applicable of system update
    applicable = resource2.Body('applicable')
