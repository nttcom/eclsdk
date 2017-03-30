# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from ecl import exceptions
from ecl import profile
from ecl.tests.unit import base


class TestProfile(base.TestCase):
    def test_init(self):
        prof = profile.Profile()
        expected = [
            'baremetal-server', 
            'compute', 
            'dedicated-hypervisor',
            'identity',
            'image',
            'interconnectivity',
            'metering',
            'network',
            'orchestration',
            'rca',
            'sss',
            'storage',
            'volumev2',
            ]
        self.assertEqual(expected, prof.service_keys)

    def test_default_versions(self):
        prof = profile.Profile()
        self.assertEqual('v2', prof.get_filter('baremetal-server').version)
        self.assertEqual('v2', prof.get_filter('compute').version)
        self.assertEqual('v1', prof.get_filter('dedicated-hypervisor').version)
        self.assertEqual('v3', prof.get_filter('identity').version)
        self.assertEqual('v2', prof.get_filter('image').version)
        self.assertEqual('v1', prof.get_filter('interconnectivity').version)
        self.assertEqual('v2', prof.get_filter('metering').version)
        self.assertEqual('v2', prof.get_filter('network').version)
        self.assertEqual('v1', prof.get_filter('orchestration').version)
        self.assertEqual('v1', prof.get_filter('rca').version)
        self.assertEqual('v1', prof.get_filter('sss').version)
        self.assertEqual('v1', prof.get_filter('storage').version)
        self.assertEqual('v2', prof.get_filter('volumev2').version)

    def test_set(self):
        prof = profile.Profile()
        prof.set_version('compute', 'v2')
        self.assertEqual('v2', prof.get_filter('compute').version)
        prof.set_version('baremetal-server', 'v1')
        self.assertEqual('v1', prof.get_filter('baremetal-server').version)
        prof.set_version('dedicated-hypervisor', 'v3')
        self.assertEqual('v3', prof.get_filter('dedicated-hypervisor').version)
        prof.set_version('identity', 'v4')
        self.assertEqual('v4', prof.get_filter('identity').version)
        prof.set_version('image', 'v5')
        self.assertEqual('v5', prof.get_filter('image').version)
        prof.set_version('interconnectivity', 'v9')
        self.assertEqual('v9', prof.get_filter('interconnectivity').version)
        prof.set_version('metering', 'v6')
        self.assertEqual('v6', prof.get_filter('metering').version)
        prof.set_version('network', 'v7')
        self.assertEqual('v7', prof.get_filter('network').version)
        prof.set_version('orchestration', 'v8')
        self.assertEqual('v8', prof.get_filter('orchestration').version)
        prof.set_version('rca', 'v9')
        self.assertEqual('v9', prof.get_filter('rca').version)
        prof.set_version('sss', 'v10')
        self.assertEqual('v10', prof.get_filter('sss').version)
        prof.set_version('storage', 'v11')
        self.assertEqual('v11', prof.get_filter('storage').version)
        prof.set_version('volumev2', 'v12')
        self.assertEqual('v12', prof.get_filter('volumev2').version)

    def test_set_version_bad_service(self):
        prof = profile.Profile()
        self.assertRaises(exceptions.SDKException, prof.set_version, 'bogus',
                          'v2')

    def test_set_api_version(self):
        # This tests that api_version is effective after explicit setting, or
        # else it defaults to None.
        prof = profile.Profile()
        prof.set_api_version('storage', '1.2')
        svc = prof.get_filter('storage')
        self.assertEqual('1.2', svc.api_version)
        svc = prof.get_filter('compute')
        self.assertIsNone(svc.api_version)

    def test_set_all(self):
        prof = profile.Profile()
        prof.set_name(prof.ALL, 'fee')
        prof.set_region(prof.ALL, 'fie')
        prof.set_interface(prof.ALL, 'public')
        for service in prof.service_keys:
            self.assertEqual('fee', prof.get_filter(service).service_name)
            self.assertEqual('fie', prof.get_filter(service).region)
            self.assertEqual('public', prof.get_filter(service).interface)
