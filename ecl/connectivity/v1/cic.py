# -*- coding: utf-8 -*-

from ecl import utils
from ecl.connectivity import connectivity_service
from ecl import resource2


class CIC(resource2.Resource):

    resource_key = None
    resources_key = None
    base_path = '/mCICs/%(mcic_id)s/CICs'
    service = connectivity_service.ConnectivityService()

    # capabilities
    allow_get = True
    allow_list = True
    allow_create = True
    allow_delete = True
    allow_update = True

    _query_mapping = resource2.QueryParameters("sort_key", "sort_dir")

    cic_id = resource2.Body("cic_id", alternate_id=True)
    cic_name = resource2.Body("cic_name")
    cic_status = resource2.Body("cic_status")
    network_id = resource2.Body("network_id")
    network_name = resource2.Body("network_name")
    destination_vlan = resource2.Body("destination_vlan", type=int)
    colo_vlan = resource2.Body("colo_vlan", type=int)
    bandwidth = resource2.Body("bandwidth", type=int)
    mcic_id = resource2.URI("mcic_id")

    def update(self, session, mcic_id, cic_id, has_body=True, **attrs):
        uri = self.base_path % ({'mcic_id': mcic_id})
        uri = utils.urljoin(uri, cic_id)
        args = {'json': attrs}
        resp = session.put(uri, endpoint_filter=self.service, **args)
        self._translate_response(resp, has_body=False)
        return self

class EIC(CIC):
    cic_id = resource2.Body("cic_id", alternate_id=True)
    server_segment_nbr = resource2.Body("server_segment_nbr",
                                        type=int)
    server_segment_name = resource2.Body("server_segment_name")
    destination_vlan = None
    colo_vlan = None