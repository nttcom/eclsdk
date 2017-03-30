# -*- coding: utf-8 -*-


from ecl.block_store import block_store_service
from ecl import resource


class AvailabilityZone(resource.Resource):
    resources_key = 'availabilityZoneInfo'
    base_path = '/os-availability-zone'

    service = block_store_service.BlockStoreService()

    # capabilities
    allow_list = True

    id_attribute = "name"
    # Properties
    #: name of availability zone
    name = resource.prop('zoneName')
    #: state of availability zone
    state = resource.prop('zoneState')
    #: hosts of availability zone
    hosts = resource.prop('hosts')
