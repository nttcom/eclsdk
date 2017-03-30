# -*- coding: utf-8 -*-

from ecl.block_store import block_store_service
from ecl import resource


class Quota(resource.Resource):
    resource_key = "quota_set"
    resources_key = "quota_sets"
    base_path = '/os-quota-sets'
    service = block_store_service.BlockStoreService()

    # capabilities
    allow_retrieve = True

    id = resource.prop("id")


class DetailQuota(resource.Resource):
    resource_key = "quota_set"
    resources_key = "quota_sets"
    base_path = '/os-quota-sets/%(tenant_id)s/detail'

    service = block_store_service.BlockStoreService()

    # capabilities
    allow_retrieve = True

    id = resource.prop("id")


class DefaultQuota(resource.Resource):
    resource_key = "quota_set"
    resources_key = "quota_sets"
    base_path = '/os-quota-sets/%(tenant_id)s/defaults'

    service = block_store_service.BlockStoreService()

    allow_retrieve = True

    id = resource.prop("id")
