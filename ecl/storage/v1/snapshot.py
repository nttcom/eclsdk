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


class Snapshot(resource2.Resource):
    resource_key = 'snapshot'
    resources_key = 'snapshots'
    base_path = '/snapshots'

    service = storage_service.StorageService()

    # capabilities
    allow_list = True
    allow_get = True
    allow_create = True
    allow_delete = True
    allow_update = True

    # query mappings
    _query_mapping = resource2.QueryParameters('volume_id',)

    # Properties
    #: id of snapshot(UUID)
    id = resource2.Body('id')
    #: status of volume
    status = resource2.Body('status')
    #: Name of volume
    name = resource2.Body('name')
    #: Description of snapshot
    description = resource2.Body('description')
    #: Usage of snapshot
    usage = resource2.Body('usage', type=int)
    #: ID (UUID) of parent volume
    volume_id = resource2.Body('volume_id')
    #: ID (UUID) of snapshot type
    snapshot_type_id = resource2.Body('snapshot_type_id')
    #: Creation timestamp of snapshot
    created_at = resource2.Body('created_at')
    #: Update timestamp of snapshot
    updated_at = resource2.Body('updated_at')
    #: Delete timestamp of snapshot
    deleted_at = resource2.Body('deleted_at')
    #: Error message for snapshot
    error_message = resource2.Body('error_message')
    #: Reason of automatic deletion
    delete_reason = resource2.Body('delete_reason')

    def _action(self, session, body):
        """Preform server actions given the message body."""
        # NOTE: This is using Server.base_path instead of self.base_path
        # as both Server and ServerDetail instances can be acted on, but
        # the URL used is sans any additional /detail/ part.
        url = utils.urljoin(Snapshot.base_path, self.id, 'action')
        headers = {'Accept': ''}
        return session.post(
            url, endpoint_filter=self.service, json=body, headers=headers)

    def create(self, session, **attrs):
        body = {"snapshot": attrs}
        resp = session.post(
            self.base_path, endpoint_filter=self.service,
            json=body,
            headers={"Accept": "application/json"}
        )
        self._translate_response(resp, has_body=True)
        return self

    def update(self, session, volume_id, has_body=True, **attrs):
        uri = utils.urljoin(self.base_path, volume_id)
        body = {"snapshot": attrs}
        args = {'json': body}
        resp = session.put(uri, endpoint_filter=self.service, **args)
        self._translate_response(resp, has_body)
        return self

    def restore(self, session):
        """Restore volume from specified snapshot"""
        body = {'restore': None}
        self._action(session, body)

class SnapshotDetail(Snapshot):
    base_path = '/snapshots/detail'
    allow_get = False
    allow_create = False
    allow_delete = False
    allow_update = False
