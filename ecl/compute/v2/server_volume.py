# -*- coding: utf-8 -*-

from ecl.compute import compute_service
from ecl import resource2


class ServerVolume(resource2.Resource):
    resource_key = 'volumeAttachment'
    resources_key = 'volumeAttachments'
    base_path = '/servers/%(serverId)s/os-volume_attachments'
    service = compute_service.ComputeService()

    # capabilities
    allow_create = True
    allow_get = False
    allow_update = False
    allow_delete = True
    allow_list = True

    #: Device name
    device = resource2.Body('device')
    #: Attachment ID
    id = resource2.Body('id')
    #: The ID of the server
    serverId = resource2.URI('serverId')
    #: The ID of the volume
    volumeId = resource2.Body('volumeId')
