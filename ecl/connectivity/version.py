# -*- coding: utf-8 -*-


from ecl.connectivity import connectivity_service
from ecl import resource


class Version(resource.Resource):
    resource_key = 'version'
    resources_key = 'versions'
    base_path = '/'
    service = connectivity_service.ConnectivityService(
        version=connectivity_service.ConnectivityService.UNVERSIONED
    )

    # capabilities
    allow_list = True

    # Properties
    links = resource.prop('links')
    status = resource.prop('status')
    updated = resource.prop('updated')
