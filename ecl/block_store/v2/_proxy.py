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

from ecl.block_store.v2 import availability_zone as _availability_zone
from ecl.block_store.v2 import extension as _extension
from ecl.block_store.v2 import limit as _limit
from ecl.block_store.v2 import metadata as _metadata
from ecl.block_store.v2 import quota as _quota
from ecl.block_store.v2 import type as _type
from ecl.block_store.v2 import volume as _volume

from ecl import proxy


class Proxy(proxy.BaseProxy):

    def types(self):
        """Return a list of types

        :returns: A list of Type objects
        :rtype: :class:`~ecl.block_store.v2.type.Type`
        """
        return list(self._list(_type.Type, paginated=False))

    def find_volume_type(self, name_or_id, ignore_missing=False):
        """Find a volume type

        :param name_or_id: The name or ID of a volume type.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.block_store.v2.type.Type` or None
        """
        return self._find(_type.Type, name_or_id,
                          ignore_missing=ignore_missing)

    def volumes(self):
        """Return a list of volume

        :returns: A list of Volume objects
        :rtype: :class:`~ecl.block_store.v2.volume.Volume`
        """
        return list(self._list(_volume.Volume, paginated=False))

    def get_volume(self, volume):
        """Get a single volume

        :param volume: The value can be the ID of a volume or a
                       :class:`~ecl.volume.v2.volume.Volume` instance.

        :returns: One :class:`~ecl.volume.v2.volume.Volume`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_volume.Volume, volume)

    def create_volume(self, size, name=None, description=None,
                      availability_zone=None, imageRef=None, metadata=None,
                      snapshot_id=None, volume_type=None, source_volid=None):
        """Create a new volume from attributes

        :param int size: size of volume to create
        :param string name: name of volume to create
        :param string description: description of volume to create
        :param string availability_zone: availability zone of volume to create
        :param string imageRef: image ID of volume to create from
        :param dict metadata: metadata of volume to create
        :param string snapshot_id: snapshot ID of volume to create
        :param string volume_type: type of volume to create
        :param string source_volid: source volume id of volume to create from

        :returns: The results of volume creation
        :rtype: :class:`~ecl.volume.v2.volume.Volume`
        """
        attrs = dict()
        attrs.update({"size": size})
        if name:
            attrs.update({"name": name})
        if description:
            attrs.update({"description": description})
        if availability_zone:
            attrs.update({"availability_zone": availability_zone})
        if imageRef:
            attrs.update({"imageRef": imageRef})
        if metadata:
            attrs.update({"metadata": metadata})
        if snapshot_id:
            attrs.update({"snapshot_id": snapshot_id})
        if volume_type:
            attrs.update({"volume_type": volume_type})
        if source_volid:
            attrs.update({"source_volid": source_volid})
        return self._create(_volume.Volume, **attrs)

    def delete_volume(self, volume, ignore_missing=False):
        """Delete a volume

        :param volume: The value can be either the ID of a volume or a
                       :class:`~ecl.volume.v2.volume.Volume` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the volume does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent volume.

        :returns: ``None``
        """
        self._delete(_volume.Volume, volume, ignore_missing=ignore_missing)

    def update_volume(self, volume, **body):
        """Create a new volume from attributes

        :param volume: The value can be the ID of a volume or a
                       :class:`~ecl.volume.v2.volume.Volume` instance.
        :param string name: name of volume to update
        :param string description: description of volume to update

        :returns: The results of volume update
        :rtype: :class:`~ecl.volume.v2.volume.Volume`
        """
        self._update(_volume.Volume, volume, **body)

    def extend_volume(self, volume, new_size):
        """Extend size of a volume

        :param volume: The value can be the ID of a volume or a
                       :class:`~ecl.volume.v2.volume.Volume` instance.
        :param string new_size: size of volume to extend

        :returns: The results of volume extend size
        :rtype: :class:`~ecl.volume.v2.volume.Volume`
        """
        volume = self._get_resource(_volume.Volume, volume)
        return volume.extend_size(self.session, new_size)

    def upload_to_image(self, volume, container_format=None,
                        disk_format=None, image_name=None,
                        force=False):
        """

        :param volume: The value can be the ID of a volume or a
                       :class:`~ecl.volume.v2.volume.Volume` instance.
        :param string container_format: Select one of the following
                        (bare, ovf, ami, aki, ari)
        :param string disk_format: Select one of the following
                        (raw, vmdk, vdi, qcow2)
        :param string image_name: Name of image to upload
        :param boolean force: Whether to upload a volume of attached state.
                        When the state of volume is available,
                        the value of force option does not affect the operation.
        :return: Object describes detail of volume_upload_image
        """
        volume = self._get_resource(_volume.Volume, volume)
        return volume.upload_to_image(self.session,
                                      container_format=container_format,
                                      disk_format=disk_format,
                                      image_name=image_name,
                                      force=force)

    def update_bootable(self, volume, bootable=False):
        """

        :param volume: The value can be the ID of a volume or a
                       :class:`~ecl.volume.v2.volume.Volume` instance.
        :param boolean bootable: bootable status to update
        :return: None
        """
        volume = self._get_resource(_volume.Volume, volume)
        return volume.update_bootable(self.session, bootable)

    def availability_zones(self):
        """Return a list of availability zones

        :returns: A list of availability zone
        :rtype: :class:`~ecl.block_store.v2.availability_zone.AvailabilityZone`
        """
        return list(self._list(_availability_zone.AvailabilityZone, paginated=False))

    def find_availability_zone(self, name_or_id, ignore_missing=False):
        """Find a single availability_zone

        :param name_or_id: The name or ID of a availability_zone.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.block_store.v2.availability_zone.AvailabilityZone` or None
        """
        return self._find(_availability_zone.AvailabilityZone, name_or_id,
                          ignore_missing=ignore_missing)

    def get_quota(self, tenant_id):
        """Get quota info of a tenant

        :param tenant_id: The ID for the tenant for which you want to show
                        quotas. This ID is different from the tenant ID of authentication.
                        That ID is for the admin tenant.

        :returns: One :class:`~ecl.block_store.v2.quota.Quota`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_quota.Quota, tenant_id)

    def get_quota_detail(self, tenant_id, user_id):
        """Get quota info of a tenant

        :param tenant_id: The ID for the tenant for which you want to show
                        quotas. This ID is different from the tenant ID of authentication.
                        That ID is for the admin tenant.
        :param user_id: The user ID. Specify in the URI as a query string

        :returns: One :class:`~ecl.block_store.v2.quota.DetailQuota`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_quota.DetailQuota, user_id,
                         path_args={"tenant_id": tenant_id})

    def get_default_quota(self, tenant_id):
        """Get default quota of a tenant

        :param tenant_id: The ID for the tenant for which you want to show
                        quotas. This ID is different from the tenant ID of authentication.
                        That ID is for the admin tenant.
        :param user_id: The user ID. Specify in the URI as a query string

        :returns: One :class:`~ecl.block_store.v2.quota.DefaultQuota`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_quota.DefaultQuota, None,
                         path_args={"tenant_id": tenant_id})

    def extensions(self):
        """Return a list of Extensions

        :returns: A list of Extension objects
        :rtype: :class:`~ecl.block_store.v2.extension.Extension`
        """
        return list(self._list(_extension.Extension, paginated=False))

    def limits(self):
        """Return a list of Limit

        :returns: show Limit objects
        :rtype: :class:`~ecl.block_store.v2.limit.Limit`
        """
        return self._get(_limit.Limit, None)

    def update_metadata(self, volume_id, **metadata):
        """
        Updates metadata items by key for a specified volume.

        :param volume_id: volume id to update metadata
        :param metadata: metadata to updata
        :return: :class:`~ecl.block_store.v2.metadata.Metadata
        """
        meta = _metadata.Metadata()
        return meta.update(self.session, volume_id, **metadata)

    def create_metadata(self, volume_id, **metadata):
        """
        Creates or replaces metadata items for a specified volume.
        
        :param volume_id: volume id to create metadata
        :param metadata: metadata to create
        :return: :class:`~ecl.block_store.v2.metadata.Metadata
        """
        meta = _metadata.Metadata()
        return meta.create(self.session, volume_id, **metadata)

    def find_volume(self, name_or_id, ignore_missing=False):
        """Find a single volume

        :param name_or_id: The name or ID of a server.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.compute.v2.volume.Volume` or None
        """
        return self._find(_volume.Volume, name_or_id,
                          ignore_missing=ignore_missing)
