# -*- coding: utf-8 -*-

import six

from ecl.tests.functional import base


class TestQuota(base.BaseFunctionalTest):

    @classmethod
    def setUpClass(cls):
        super(TestQuota, cls).setUpClass()

    def test_quota(self):
        tenant_id = "3ac7407ad7ab4e2fa0665df71a4886e4"
        quota = self.conn.block_store.get_quota(tenant_id)

        self.assertEqual(quota.id, tenant_id)

    def test_get_detail_quota(self):
        tenant_id = "3ac7407ad7ab4e2fa0665df71a4886e4"
        user_id = tenant_id
        quota = self.conn.block_store.get_quota_detail(tenant_id, user_id)

        self.assertIsInstance(quota.id, six.string_types)

    def test_get_default_quota(self):
        tenant_id = "3ac7407ad7ab4e2fa0665df71a4886e4"
        info = self.conn.block_store.get_default_quota(tenant_id)

        self.assertIsInstance(info.id, six.string_types)
