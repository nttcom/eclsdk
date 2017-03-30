# -*- coding: utf-8 -*-

from ecl.compute import compute_service
from ecl import resource2


class Volume(resource2.Resource):
    resource_key = 'volume'
    resources_key = 'volumes'
    base_path = '/os-volumes'
    service = compute_service.ComputeService()

    # capabilities
    allow_create = True
    allow_get = True
    allow_delete = True
    allow_list = True
    allow_update = True

    id = resource2.Body("id")
    name = resource2.Body("displayName")
    description = resource2.Body("displayDescription")
    size = resource2.Body("size")
    volume_type = resource2.Body("volumeType")
    metadata = resource2.Body("metadata", dict)
    availability_zone = resource2.Body("availabilityZone")
    snapshot_id = resource2.Body("snapshotId")
    attachments = resource2.Body("attachments", list)
    created_at = resource2.Body("createdAt")
    status = resource2.Body('status')
    bootable = resource2.Body('bootable')


class VolumeDetail(Volume):
    base_path = '/os-volumes/detail'

    allow_create = False
    allow_get = False
    allow_delete = False
