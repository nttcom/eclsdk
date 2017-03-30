# -*- coding: utf-8 -*-

from ecl.tests.functional import base


class TestQuota(base.BaseFunctionalTest):

    def test_get(self):
        quota_id = "tenant"
        sot = self.conn.network.get_quota(quota=quota_id)
        self.assertIn('colocation_logical_link', sot)
        self.assertIn('common_function_gateway', sot)
        self.assertIn('firewall', sot)
        self.assertIn('interdc_gateway', sot)
        self.assertIn('internet_gateway', sot)
        self.assertIn('load_balancer', sot)
        self.assertIn('network', sot)
        self.assertIn('port', sot)
        self.assertIn('subnet', sot)
        self.assertIn('vpn_gateway', sot)
