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

from ecl.database import database_service
from ecl import resource2


class Flavor(resource2.Resource):
    resource_key = 'flavor'
    resources_key = 'flavors'
    base_path = '/flavors'
    service = database_service.DatabaseService()

    # capabilities
    allow_get = True
    allow_list = True

    _query_mapping = resource2.QueryParameters()

    # Properties
    #: Links pertaining to this flavor. This is a list of dictionaries,
    #: each including keys ``href`` and ``rel``.
    links = resource2.Body('links')
    #: The name of this flavor.
    name = resource2.Body('name')
    #: Size of the disk this flavor offers. *Type: int*
    disk = resource2.Body('disk', type=int)
    #: ``True`` if this is a publicly visible flavor. ``False`` if this is
    #: a private image. *Type: bool*
    is_public = resource2.Body('os-flavor-access:is_public', type=bool)
    #: The amount of RAM (in MB) this flavor offers. *Type: int*
    ram = resource2.Body('ram', type=int)
    #: The number of virtual CPUs this flavor offers. *Type: int*
    vcpus = resource2.Body('vcpus', type=int)
    #: Size of the swap partitions.
    swap = resource2.Body('swap')
    #: Size of the ephemeral data disk attached to this server. *Type: int*
    ephemeral = resource2.Body('ephemeral', type=int)
    #: ``True`` if this flavor is disabled, ``False`` if not. *Type: bool*
    is_disabled = resource2.Body('OS-FLV-DISABLED:disabled', type=bool)
    #: The bandwidth scaling factor this flavor receives on the network.
    rxtx_factor = resource2.Body('rxtx_factor', type=float)
    #: ID
    str_id = resource2.Body('str_id', alternate_id=True)
