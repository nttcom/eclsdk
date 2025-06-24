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

from ecl.block_store import block_store_service
from ecl import format
from ecl import resource
from ecl import utils


class Volume(resource.Resource):
    resource_key = "volume"
    resources_key = "volumes"
    base_path = "/volumes"
    service = block_store_service.BlockStoreService()

    # capabilities
    allow_retrieve = True
    allow_create = True
    allow_delete = True
    allow_update = True
    allow_list = True

    # Properties
    #: A ID representing this volume.
    id = resource.prop("id")
    #: The name of this volume.
    name = resource.prop("name")
    #: A list of links associated with this volume. *Type: list*
    links = resource.prop("links", type=list)

    #: The availability zone.
    availability_zone = resource.prop("availability_zone")
    #: To create a volume from an existing volume, specify the ID of
    #: the existing volume. If specified, the volume is created with
    #: same size of the source volume.
    source_volume_id = resource.prop("source_volid")
    #: The volume description.
    description = resource.prop("description")
    #: To create a volume from an existing snapshot, specify the ID of
    #: the existing volume snapshot. If specified, the volume is created
    #: in same availability zone and with same size of the snapshot.
    snapshot_id = resource.prop("snapshot_id")
    #: The size of the volume, in GBs. *Type: int*
    size = resource.prop("size", type=int)
    #: The ID of the image from which you want to create the volume.
    #: Required to create a bootable volume.
    image_id = resource.prop("imageRef")
    #: The name of the associated volume type.
    volume_type = resource.prop("volume_type")
    #: Enables or disables the bootable attribute. You can boot an
    #: instance from a bootable volume. *Type: bool*
    is_bootable = resource.prop("bootable", type=format.BoolStr)
    #: One or more metadata key and value pairs to associate with the volume.
    metadata = resource.prop("metadata")

    #: One of the following values: creating, available, attaching, in-use
    #: deleting, error, error_deleting, backing-up, restoring-backup,
    #: error_restoring. For details on these statuses, see the
    #: Block Storage API documentation.
    status = resource.prop("status")
    #: TODO(briancurtin): This is currently undocumented in the API.
    attachments = resource.prop("attachments")
    #: The timestamp of this volume creation.
    created_at = resource.prop("created_at")

    def _action(self, session, body):
        """Preform server actions given the message body."""
        # NOTE: This is using Server.base_path instead of self.base_path
        # as both Server and ServerDetail instances can be acted on, but
        # the URL used is sans any additional /detail/ part.
        url = utils.urljoin(Volume.base_path, self.id, 'action')
        headers = {'Accept': ''}
        return session.post(
            url, endpoint_filter=self.service, json=body, headers=headers)

    def extend_size(self, session, new_size):
        body = {"os-extend": {"new_size": new_size}}
        return self._action(session, body)

    def upload_to_image(self, session, container_format=None,
                        disk_format=None,
                        image_name=None, force=False):

        body = dict()
        if container_format:
            body.update({"container_format": container_format})
        if disk_format:
            body.update({"disk_format": disk_format})
        if force:
            body.update({"force": force})
        if image_name:
            body.update({"image_name": image_name})
        return self._action(session, {"os-volume_upload_image": body})

    def update_bootable(self, session, bootable=False):
        body = {"os-set_bootable": {
            "bootable": bootable
        }}
        return self._action(session, body)

    def retype(self, session, volume_type, is_dry_run=False):
        """ Volume type change and dry run configuration process. """
        body = {
            'os-retype': {
                'new_type': volume_type,
                'migration_policy': 'on-demand'
            }
        }
        if is_dry_run:
            body['os-retype']['dryRun'] = True
        self._action(session, body)


class VolumeDetail(Volume):

    base_path = "/volumes/detail"

    #: The volume's current back-end.
    host = resource.prop("os-vol-host-attr:host")
    #: The project ID associated with current back-end.
    project_id = resource.prop("os-vol-tenant-attr:tenant_id")
    #: The status of this volume's migration (None means that a migration
    #: is not currently in progress).
    migration_status = resource.prop("os-vol-mig-status-attr:migstat")
    #: The volume ID that this volume's name on the back-end is based on.
    migration_id = resource.prop("os-vol-mig-status-attr:name_id")
    #: Status of replication on this volume.
    replication_status = resource.prop("replication_status")
    #: Extended replication status on this volume.
    extended_replication_status = resource.prop(
        "os-volume-replication:extended_status")
    #: ID of the consistency group.
    consistency_group_id = resource.prop("consistencygroup_id")
    #: Data set by the replication driver
    replication_driver_data = resource.prop(
        "os-volume-replication:driver_data")
    #: ``True`` if this volume is encrypted, ``False`` if not.
    #: *Type: bool*
    is_encrypted = resource.prop("encrypted", type=format.BoolStr)
