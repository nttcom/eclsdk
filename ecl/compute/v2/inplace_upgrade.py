# -*- coding: utf-8 -*-

from ecl.compute import compute_service
from ecl import resource2


class InplaceUpgrade(resource2.Resource):
    resource_key = 'inplace_upgrade'
    resources_key = 'inplace_upgrades'
    base_path = '/servers/%(server_id)s/inplace_upgrades'
    service = compute_service.ComputeService()

    # capabilities
    allow_create = False
    allow_get = False
    allow_delete = False
    allow_list = True
    allow_update = False

    id = resource2.Body("id")
    instance_id = resource2.Body("instance_id")
    status = resource2.Body("status")
    src_os = resource2.Body("src_os")
    dst_os = resource2.Body("dst_os")
    created_at = resource2.Body("created_at")
    upgrade_at = resource2.Body("upgrade_at")
    updated_at = resource2.Body("updated_at")
