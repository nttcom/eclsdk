# -*- coding: utf-8 -*-

import testtools

from ecl.provider_connectivity import provider_connectivity_service


class TestProviderConnectivityService(testtools.TestCase):

    def test_service(self):
        sot = provider_connectivity_service.ProviderConnectivityService()
        self.assertEqual('provider-connectivity', sot.service_type)
        self.assertEqual('public', sot.interface)
        self.assertIsNone(sot.region)
        self.assertIsNone(sot.service_name)
        self.assertEqual(1, len(sot.valid_versions))
        self.assertEqual('v1', sot.valid_versions[0].module)
        self.assertEqual('v1', sot.valid_versions[0].path)
