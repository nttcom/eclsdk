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


class Keypair(resource2.Resource):
    resource_key = 'keypair'
    resources_key = 'keypairs'
    base_path = '/os-keypairs'
    service = baremetal_service.BaremetalService()

    # capabilities
    allow_create = True
    allow_get = True
    allow_delete = True
    allow_list = True

    # Properties
    #: Fingerprint of public key.
    fingerprint = resource2.Body('fingerprint')
    #: The name to associate with the KeyPair. It is a unique name in
    #: the tenant. Available character is 1-255 character of
    #: alphabet(a-zA-Z), number(0-9) and slash(-).
    name = resource2.Body('name', alternate_id=True)
    #: Generated SSH private key.
    #: This parameter is visible only when did not specify public_key
    #: This parameter is only included in the response of Create Keypair.
    private_key = resource2.Body('private_key')
    #: The public RSA or DSA SSH key to import. If not provided,
    #: a key is generated 2048bit RSA key.
    public_key = resource2.Body('public_key')

    def list(self, session, paginated=False):
        resp = session.get(self.base_path, endpoint_filter=self.service,
                           headers={"Accept": "application/json"})
        resp = resp.json()
        resp = resp[self.resources_key]

        for data in resp:
            value = self.existing(**data)
            yield value
