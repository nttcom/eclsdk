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

from ecl.dns import dns_service
from ecl import resource2
from ecl import exceptions


class NameServer(resource2.Resource):
    resource_key = None
    resources_key = "nameservers"
    base_path = '/v2/zones/%(zone_id)s/nameservers'
    service = dns_service.DnsService()

    # Capabilities
    allow_list = True

    # Properties
    #: ID for the zone.
    zone_id = resource2.URI('zone_id')
    #: The hostname of the nameserver that the zone should be delegated to.
    hostname = resource2.Body('hostname', alternate_id=True)
    #: The priority of the nameserver. This is used to determine the order of the the nameserver listings,
    #: and which server is used in the SOA record for the zone. This parameter is not currently supported.
    priority = resource2.Body('priority')
