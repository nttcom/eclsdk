# -*- coding: utf-8 -*-

from ecl.compute import compute_service
from ecl import resource2


class Quota(resource2.Resource):
    resource_key = "quota_set"
    resources_key = "quota_sets"
    base_path = '/os-quota-sets'
    service = compute_service.ComputeService()
    
    # capabilities
    allow_get = True
    
    cores = resource2.Body("cores", int)
    fixed_ips = resource2.Body("fixed_ips", int)
    id = resource2.Body("id")
    injected_file_content_bytes = resource2.Body("injected_file_content_bytes", int)
    injected_file_path_bytes = resource2.Body("injected_file_path_bytes", int)
    injected_files = resource2.Body("injected_files", int)
    instances = resource2.Body("instances", int)
    key_pairs = resource2.Body("key_pairs", int)
    metadata_items = resource2.Body("metadata_items", int)
    ram = resource2.Body("ram", int)
    security_group_rules = resource2.Body("security_group_rules", int)
    security_groups = resource2.Body("security_groups", int)
    server_group_members = resource2.Body("server_group_members", int)
    server_groups = resource2.Body("server_groups", int)


class DefaultQuota(resource2.Resource):
    resource_key = "quota_set"
    resources_key = "quota_sets"
    base_path = '/os-quota-sets/%(tenant_id)s/defaults'
    service = compute_service.ComputeService()

    allow_get = True

    tenant_id = resource2.URI("tenant_id")
    cores = resource2.Body("cores", int)
    fixed_ips = resource2.Body("fixed_ips", int)
    id = resource2.Body("id")
    injected_file_content_bytes = resource2.Body("injected_file_content_bytes", int)
    injected_file_path_bytes = resource2.Body("injected_file_path_bytes", int)
    injected_files = resource2.Body("injected_files", int)
    instances = resource2.Body("instances", int)
    key_pairs = resource2.Body("key_pairs", int)
    metadata_items = resource2.Body("metadata_items", int)
    ram = resource2.Body("ram", int)
    security_group_rules = resource2.Body("security_group_rules", int)
    security_groups = resource2.Body("security_groups", int)
    server_group_members = resource2.Body("server_group_members", int)
    server_groups = resource2.Body("server_groups", int)

    def get(self, session, requires_id=False):
        return super(DefaultQuota, self).get(session, False)


class TenantUsage(resource2.Resource):
    resource_key = "tenant_usage"
    resources_key = "tenant_usages"
    base_path = '/os-simple-tenant-usage'
    service = compute_service.ComputeService()

    allow_get = True

    server_usages = resource2.Body("server_usages")
    start = resource2.Body("start")
    stop = resource2.Body("stop")
    tenant_id = resource2.Body("tenant_id")
    total_hours = resource2.Body("total_hours")
    total_local_gb_usage = resource2.Body("total_local_gb_usage")
    total_memory_mb_usage = resource2.Body("total_memory_mb_usage")
    total_vcpus_usage = resource2.Body("total_vcpus_usage")
