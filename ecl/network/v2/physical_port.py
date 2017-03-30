# -*- coding: utf-8 -*-

from ecl.network import network_service
from ecl import resource2


class PhysicalPort(resource2.Resource):
    resource_key = 'physical_port'
    resources_key = 'physical_ports'
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/physical_ports'

    # capabilities
    allow_get = True
    allow_list = True

    # properties
    #: Physical port description.
    description = resource2.Body('description')
    #: Physical port unique id.
    id = resource2.Body('id')
    #: Physical port name.
    name = resource2.Body('name')
    #: The type of traffic that port will be used.
    plane = resource2.Body('plane')
    #: Ranges of allowed VLAN tags.
    segmentation_ranges = resource2.Body('segmentation_ranges')
    #: The ID of service that owns the physical port.
    service_id = resource2.Body('service_id')
    #: The type of physical port service owner.
    service_owner = resource2.Body('service_owner')
    #: The Physical Port status.
    status = resource2.Body('status')
    #: Port tags.
    tags = resource2.Body('tags')
    #: The owner name of physical port.
    tenant_id = resource2.Body('tenant_id')
