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


class Chassis(resource2.Resource):
    """Chassis Resource"""

    resource_key = 'chassis'
    resources_key = 'chassis'
    base_path = '/chassis'
    service = baremetal_service.BaremetalService()

    # Capabilities
    allow_get = True
    allow_list = True

    # Properties
    #: The ID for the chassis, which is a unique integer value.
    id = resource2.Body('id')
    #: The name of availability zone where chassis exists.
    availability_zone = resource2.Body('availability_zone')
    #: The name of flavor of chassis.
    flavor_name = resource2.Body('flavor_name')
    #: The object of summarized hardware spec. That has cpus, disks and rams.
    hardware_summary = resource2.Body('hardware_summary', type=dict)
    #: The status of chassis.
    status = resource2.Body('status')
    #: The ID of server attached to chassis. If no server is attached to chassis, the value is null.
    server_id = resource2.Body('server_id')
    #: The name of server attached to chassis. If no server is attached to chassis, the value is null.
    server_name = resource2.Body('server_name')
    #: The minimum contract period of your chassis.
    contract_year = resource2.Body('contract_year', type=int)
    #: The date that you start to use the chassis.
    start_time = resource2.Body('start_time')

    # Properties (for Detail)
    #: The spec of all cpus installed in chassis.
    cpus = resource2.Body('cpus', type=list)
    #: The spec of all disks installed in chassis.
    disks = resource2.Body('disks', type=list)
    #: The spec of all rams installed in chassis.
    rams = resource2.Body('rams', type=list)


class ChassisDetail(Chassis):
    """ChassisDetail Resource"""

    base_path = '/chassis/detail'

    # Capabilities
    allow_get = False
