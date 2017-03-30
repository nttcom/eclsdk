# -*- coding: utf-8 -*-

import six

from ecl.tests.functional import base


class TestQuota(base.BaseFunctionalTest):

    @classmethod
    def setUpClass(cls):
        super(TestQuota, cls).setUpClass()

    def test_quota(self):
        tenant_id = "3ac7407ad7ab4e2fa0665df71a4886e4"
        quota = self.conn.compute.get_quota(tenant_id)

        self.assertIsInstance(quota.cores, int)
        self.assertIsInstance(quota.fixed_ips, int)
        self.assertIsInstance(quota.id, six.string_types)
        self.assertIsInstance(quota.injected_file_content_bytes, int)
        self.assertIsInstance(quota.injected_file_path_bytes, int)
        self.assertIsInstance(quota.instances, int)
        self.assertIsInstance(quota.key_pairs, int)
        self.assertIsInstance(quota.metadata_items, int)
        self.assertIsInstance(quota.ram, int)
        self.assertIsInstance(quota.security_group_rules, int)
        self.assertIsInstance(quota.security_groups, int)
        self.assertIsInstance(quota.server_group_members, int)
        self.assertIsInstance(quota.server_groups, int)

    def test_get_default_quota(self):
        tenant_id = "3ac7407ad7ab4e2fa0665df71a4886e4"
        quota = self.conn.compute.get_default_quota(tenant_id)

        self.assertIsInstance(quota.cores, int)
        self.assertIsInstance(quota.fixed_ips, int)
        self.assertIsInstance(quota.id, six.string_types)
        self.assertIsInstance(quota.injected_file_content_bytes, int)
        self.assertIsInstance(quota.injected_file_path_bytes, int)
        self.assertIsInstance(quota.instances, int)
        self.assertIsInstance(quota.key_pairs, int)
        self.assertIsInstance(quota.metadata_items, int)
        self.assertIsInstance(quota.ram, int)
        self.assertIsInstance(quota.security_group_rules, int)
        self.assertIsInstance(quota.security_groups, int)
        self.assertIsInstance(quota.server_group_members, int)
        self.assertIsInstance(quota.server_groups, int)

    def test_get_tenant_usage(self):
        tenant_id = "3ac7407ad7ab4e2fa0665df71a4886e4"
        info = self.conn.compute.get_tenant_usage(tenant_id)

        self.assertIsInstance(info.start, six.string_types)
        self.assertIsInstance(info.stop, six.string_types)
        self.assertIsInstance(info.tenant_id, six.string_types)
