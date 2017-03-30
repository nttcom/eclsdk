# -*- coding: utf-8 -*-

from ecl.connectivity import connectivity_service
from ecl import resource2


class ServerSegment(resource2.Resource):

    resource_key = None  # Get is not allowed.
    resources_key = 'server_segments'

    base_path = '/ec_services/%(service_id)s/server_segments'
    service = connectivity_service.ConnectivityService()

    # capabilities
    allow_get = False
    allow_list = True

    # _query_mapping = resource2.QueryParameters("mcic_id", "cic_id")

    # Properties
    #: server segment number.
    server_segment_nbr = resource2.Body('server_segment_nbr',
                                        type=int,
                                        alternate_id=True)
    #: server segment name.
    server_segment_name = resource2.Body('server_segment_name')
