# -*- coding: utf-8 -*-


from ecl.connectivity import connectivity_service
from ecl import resource2


class MCIC(resource2.Resource):
    resource_key = None
    resources_key = None
    base_path = '/mCICs'
    service = connectivity_service.ConnectivityService()

    # capabilities
    allow_get = True
    allow_list = True

    _query_mapping = resource2.QueryParameters("tenant_id", "sort_key",
                                               "sort_dir")

    mcic_id = resource2.Body('mcic_id', alternate_id=True)
    mcic_name = resource2.Body('mcic_name')
    mcic_status = resource2.Body('mcic_status')
    tenant_id = resource2.Body('tenant_id')
    tenant_name = resource2.Body('tenant_name')
    service_type = resource2.Body('service_type')
    ngc = resource2.Body('ngc', dict)
    colo = resource2.Body('colo', dict)
    timezone = resource2.Body('timezone')


class MEIC(MCIC):
    mcic_id = resource2.Body('mcic_id', alternate_id=True)
    tenant_name = resource2.Body('tenant_name')
    service_id = resource2.Body('service_id')
    colo = None
    ec = resource2.Body('ec', dict)
