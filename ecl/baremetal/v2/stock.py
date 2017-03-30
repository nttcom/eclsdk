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


class Stock(resource2.Resource):
    resource_key = 'stock'
    base_path = '/stock'
    service = baremetal_service.BaremetalService()

    # Capabilities
    allow_get = True

    # Properties
    #: Flavor UUID of Baremetal server stock search condition.
    flavor_id = resource2.Body('flavor_id', alternate_id=True)
    #: Availability Zone name of Baremetal server stock search condition.
    availability_zone = resource2.Body('availability_zone')
    #: Baremetal server stock is available or not.
    stock = resource2.Body('stock')

    def get(self, session, flavor_id, availability_zone=None):
        uri = self.base_path + "?flavor_id=%s" % flavor_id
        if availability_zone:
            uri += "&availability_zone=%s" % availability_zone
        resp = session.get(uri, endpoint_filter=self.service,
                           headers={"Accept": "application/json"})
        self._translate_response(resp, has_body=True)
        return self
