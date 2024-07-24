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

import mock
import testtools

from keystoneauth1 import exceptions as _exceptions

from ecl import exceptions
from ecl import profile
from ecl import session


class TestSession(testtools.TestCase):



    def test_get_endpoint_cached(self):
        sot = session.Session(None)
        service_type = "compute"
        interface = "public"
        endpoint = "the world wide web"

        sot.endpoint_cache[(service_type, interface)] = endpoint
        rv = sot.get_endpoint(service_type=service_type, interface=interface)
        self.assertEqual(rv, endpoint)

    def test_get_accept_null(self):
        sot = session.Session(None)
        sot.request = mock.Mock()
        sot.request.return_value = type("Server", (object,), {"id": "1234", "name": "test-server"})

        request_headers = {}
        rv = sot.get(url='/server/hoge/', headers=request_headers, dummy='d')

        actual_request_headers = sot.request.call_args_list[0][1].get('headers')

        self.assertEqual(actual_request_headers, {'Accept': 'application/json'})

    def test_get_accept_json(self):
        sot = session.Session(None)
        sot.request = mock.Mock()
        sot.request.return_value = type("Server", (object,), {"id": "1234", "name": "test-server"})

        request_headers = {}
        rv = sot.get(url='/server/hoge/',
                     headers={"Accept": "application/json"},
                     dummy='d')

        actual_request_headers = sot.request.call_args_list[0][1].get('headers')

        self.assertEqual(actual_request_headers, {'Accept': 'application/json'})

    def test_get_accept_octetstream(self):
        sot = session.Session(None)
        sot.request = mock.Mock()
        sot.request.return_value = type("Server", (object,), {"id": "1234", "name": "test-server"})

        request_headers = {}
        rv = sot.get(url='/server/hoge/',
                     headers={"Accept": "application/octet-stream"},
                     dummy='d')

        actual_request_headers = sot.request.call_args_list[0][1].get('headers')

        self.assertEqual(actual_request_headers, {'Accept': 'application/octet-stream'})

    def test_post(self):
        sot = session.Session(None)
        sot.request = mock.Mock()
        sot.request.return_value = type("Server", (object,), {"id": "1234", "name": "test-server"})

        request_headers = {'Accept': ''}
        rv = sot.post(url='/server/hoge/', headers=request_headers, dummy='d')

        actual_request_headers = sot.request.call_args_list[0][1].get('headers')

        self.assertEqual(actual_request_headers, {'Accept': 'application/json'})

    def test_put(self):
        sot = session.Session(None)
        sot.request = mock.Mock()
        sot.request.return_value = type("Server", (object,), {"id": "1234", "name": "test-server"})

        request_headers = {'Accept': ''}
        rv = sot.put(url='/server/hoge/', headers=request_headers, dummy='d')

        actual_request_headers = sot.request.call_args_list[0][1].get('headers')

        self.assertEqual(actual_request_headers, {'Accept': 'application/json'})

    def test_delete(self):
        sot = session.Session(None)
        sot.request = mock.Mock()
        sot.request.return_value = type("Server", (object,), {"id": "1234", "name": "test-server"})

        request_headers = {'Accept': ''}
        rv = sot.delete(url='/server/hoge/', headers=request_headers, dummy='d')

        actual_request_headers = sot.request.call_args_list[0][1].get('headers')

        self.assertEqual(actual_request_headers, {'Accept': 'application/json'})

    def test_patch(self):
        sot = session.Session(None)
        sot.request = mock.Mock()
        sot.request.return_value = type("Server", (object,), {"id": "1234", "name": "test-server"})

        request_headers = {'Accept': ''}
        rv = sot.patch(url='/server/hoge/', headers=request_headers, dummy='d')

        actual_request_headers = sot.request.call_args_list[0][1].get('headers')

        self.assertEqual(actual_request_headers, {'Accept': 'application/json'})
