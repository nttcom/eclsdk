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

from ecl.baremetal import baremetal_service
from ecl import resource2


class Metadata(resource2.Resource):
    resource_key = None
    resources_key = None
    base_path = '/servers/%(server_id)s/metadata'
    service = baremetal_service.BaremetalService()

    # Capabilities
    allow_list = True
    allow_show = True
    allow_create = True
    allow_delete = True

    # Properties
    #: Metadata of the server.
    metadata = resource2.Body("metadata")

    def list(self, session, server_id):

        uri = self.base_path % {"server_id" : server_id}
        resp = session.get(uri, endpoint_filter=self.service,
                           headers={"Accept": "application/json"})
        self._translate_response(resp, has_body=True)
        return self

    def get(self, session, server_id, key):
        uri = self.base_path + '/%(key)s'
        uri = uri % {"server_id":server_id, "key":key}
        resp = session.get(uri, endpoint_filter=self.service,
                           headers={"Accept": "application/json"})
        self._translate_response(resp, has_body=True)
        return self

    def delete(self, session, server_id, key):
        uri = self.base_path + '/%(key)s'
        uri = uri % {"server_id": server_id, "key": key}
        resp = session.delete(uri, endpoint_filter=self.service,
                              headers={"Accept": ""})
        self._translate_response(resp, has_body=False)
        return self

    def merge(self, session, server_id, **attrs):
        uri = self.base_path % {"server_id" : server_id}
        body = {"metadata": attrs}
        resp = session.post(
            uri, endpoint_filter=self.service,
            json=body,
            headers={"Accept": "application/json"}
        )
        self._translate_response(resp, has_body=True)
        return self

    def replace(self, session, server_id, **attrs):
        uri = self.base_path % {"server_id" : server_id}
        body = attrs
        resp = session.put(
            uri, endpoint_filter=self.service,
            json=body,
            headers={"Accept": "application/json"}
        )
        self._translate_response(resp, has_body=True)
        return self

    def update(self, session, server_id, key, **attrs):
        uri = self.base_path + '/%(key)s'
        uri = uri % {"server_id": server_id, "key": key}
        body = attrs
        resp = session.put(
            uri, endpoint_filter=self.service,
            json=body,
            headers={"Accept": "application/json"}
        )
        self._translate_response(resp, has_body=True)
        return self
