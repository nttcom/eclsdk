# -*- coding: utf-8 -*-

from ecl.provider_connectivity import provider_connectivity_service
from ecl import resource2


class ExchangePoint(resource2.Resource):
    resources_key = "exchange_points"
    service = provider_connectivity_service.ProviderConnectivityService("v1.0")
    base_path = '/' + service.version + '/icc/exchange_points'

    # Capabilities
    allow_list = True

    # Properties
    #: It identifies exchange_point resource uniquely.
    id = resource2.Body('id')
    #: Pair of location name of AWS and ECL2.0.
    location_names = resource2.Body('location_names')
