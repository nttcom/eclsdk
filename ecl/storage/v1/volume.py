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

from ecl import utils
from ecl.storage import storage_service

from ecl import resource2
from ecl.storage import storage_service


class Volume(resource2.Resource):
    resource_key = 'volume'
    resources_key = 'volumes'
    base_path = '/volumes'

    service = storage_service.StorageService()

    # capabilities
    allow_list = True
    allow_get = True
    allow_create = True
    allow_delete = True
    allow_update = True

    # Properties
    #: id of volume(UUID)
    id = resource2.Body('id')
    #: status of volume
    status = resource2.Body('status')
    #: name of volume
    name = resource2.Body('name')
    #: description of volume
    description = resource2.Body('description')
    #: The size of volume in gigabyte
    size = resource2.Body('size', type=int)
    #: The provisioned IOPS/GB for volume
    iops_per_gb = resource2.Body('iops_per_gb', type=int)
    #: Array of initiator IQN who can access to this volume
    initiator_iqns = resource2.Body('initiator_iqns', type=list)
    #: Initiator's secret (password) for CHAP auth of iSCSI
    initiator_secret = resource2.Body('initiator_secret')
    #: Target's secret (password) for CHAP auth of iSCSI
    target_secret = resource2.Body('target_secret')
    #: Array of Snapshot IDs taken from this volume
    snapshot_ids = resource2.Body('snapshot_ids', type=list)
    #: Array of IPv4 addresses of the volume.
    target_ips = resource2.Body('target_ips', type=list)
    #: One or more metadata key and value pairs to associate with the volume.
    metadata = resource2.Body('metadata', type=dict)
    #: storage ID (UUID) volume belongs to
    virtual_storage_id = resource2.Body('virtual_storage_id')
    #: An availability_zone in which the volume belongs to
    availability_zone = resource2.Body('availability_zone')
    #: Creation timestamp of volume
    created_at = resource2.Body('created_at')
    #: update timestamp of volume
    updated_at = resource2.Body('updated_at')
    #: error description of volume
    error_message = resource2.Body('error_message')
    #: The provisioned throughput for volume in MB/s
    throughput = resource2.Body('throughput', type=int)
    #: Array of IPv4 CIDRc who can access to this volume
    export_rules = resource2.Body('export_rules', type=list)
    #: Percentage of Used Snapshots
    percentage_snapshot_reserve_used = \
        resource2.Body('percentage_snapshot_reserve_used', type=int)

    def create(self, session, **attrs):
        body = {"volume":attrs}
        resp = session.post(
            self.base_path, endpoint_filter=self.service,
            json=body,
            headers={"Accept": "application/json"}
        )
        self._translate_response(resp, has_body=True)
        return self

    def update(self, session, volume_id, has_body=True, **attrs):
        uri = utils.urljoin(self.base_path, volume_id)
        body = {"volume": attrs}
        args = {'json': body}
        resp = session.put(uri, endpoint_filter=self.service, **args)
        self._translate_response(resp, has_body)
        return self


class VolumeDetail(Volume):
    base_path = '/volumes/detail'
    allow_get = False
    allow_create = False
    allow_delete = False
    allow_update = False
