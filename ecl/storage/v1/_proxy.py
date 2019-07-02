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

import six

from ecl import proxy2
from ecl import session
from ecl.storage.v1 import availability_zone as _availability_zone
from ecl.storage.v1 import storage as _storage
from ecl.storage.v1 import volume as _volume
from ecl.storage.v1 import volume_type as _volume_type
from ecl.storage.v1 import snapshot as _snapshot
from ecl.storage import version as _version


class VersionSession(session.Session):

    def get_endpoint(self, auth=None, interface='public', service_type=None,
                     **kwargs):
        """Override get endpoint to automate endpoint filtering
        This method uses the service catalog to find the root URI of
        each service and then gets all available versions directly
        from the service, not from the service catalog.
        Endpoints are cached per service type and interface combination
        so that they're only requested from the remote service once
        per instance of this class.
        """

        sc_endpoint = super(VersionSession, self).get_endpoint(
            auth, interface, service_type
        )

        if sc_endpoint is None or sc_endpoint == '':
            return sc_endpoint
        segments = sc_endpoint.split('/')
        if len(segments) > 0:
            segments = segments[:-2]
            sc_endpoint = ""
            for segment in segments:
                sc_endpoint += segment + '/'
            sc_endpoint = sc_endpoint[:-1]

        return sc_endpoint


class Proxy(proxy2.BaseProxy):

    def availability_zones(self, details=True):
        """Return a list of availability zones

        :param bool details: When ``True``, returns
            :class:`~ecl.storage.v1.availability_zone.AvailabilityZoneDetail`
            objects, otherwise :class:`~ecl.storage.v1.availability_zone.AvailabilityZone`.
        :returns: A list of availability zone objects
        """
        availability_zone = _availability_zone.AvailabilityZoneDetail() \
            if details else _availability_zone.AvailabilityZone()
        return list(availability_zone.list(self.session))

    def find_availability_zone(self, name_or_id, ignore_missing=False):
        """Find a single availability_zone

        :param name_or_id: The name or ID of a availability_zone.
        :param bool ignore_missing: When set to ``False``
                                    :class:`~ecl.exceptions.ResourceNotFound` will be
                                    raised when the resource does not exist.
                                    When set to ``True``, None will be returned when
                                    attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.storage.v1.availability_zone.AvailabilityZone` or None
        """
        return self._find(_availability_zone.AvailabilityZone, name_or_id,
                          ignore_missing=ignore_missing)

    def volume_types(self, details=True):
        """Return a generator of volume types

        :param bool details: When ``True``, returns
                             :class:`~ecl.storage.v1.volume_type.VolumeTypeDetail` objects,
                             otherwise :class:`~ecl.storage.v1.volume_type.VolumeType`.
                             *Default: ``True``*
        :returns: A generator of volume type objects
        """
        volume_type = _volume_type.VolumeTypeDetail if details else _volume_type.VolumeType
        return list(self._list(volume_type, paginated=False))

    def find_volume_type(self, name_or_id, ignore_missing=False):
        """Find a volume type

            :param string name_or_id: The name or ID of a volume type.
            :param bool ignore_missing: When set to ``False``
                        :class:`~ecl.exceptions.ResourceNotFound` will be
                        raised when the resource does not exist.
                        When set to ``True``, None will be returned when
                        attempting to find a nonexistent resource.
            :returns: :class:`~ecl.storage.v1.volume_type.VolumeType` or None
            """
        return self._find(_volume_type.VolumeType, name_or_id,
                          ignore_missing=ignore_missing)

    def get_volume_type(self, volume_type_id):
        """Get a single volume type

        :param volume_type_id: The value is the ID of a volume type
        :returns: One :class:`~ecl.storage.v1.volume_type.VolumeType`
                      :class:`~ecl.exceptions.ResourceNotFound`
                      when no resource can be found.
        """
        return self._get(_volume_type.VolumeType, volume_type_id)

    def storages(self, details=True):
        """Return a generator of storages

        :param bool details: When ``True``, returns
                             :class:`~ecl.storage.v1.storage.StorageDetail` objects,
                             otherwise :class:`~ecl.storage.v1.storage.Storage`.
                             *Default: ``True``*
        :returns: A generator of storage objects
        """
        storage = _storage.StorageDetail if details else _storage.Storage
        return list(self._list(storage, paginated=False))

    def get_storage(self, storage_id):
        """Get a single storage

        :param storage_id: The value is the ID of a storage
        :returns: One :class:`~ecl.storage.v1.storage.Storage`
                      :class:`~ecl.exceptions.ResourceNotFound`
                      when no resource can be found.
        """
        return self._get(_storage.Storage, storage_id)

    def create_storage(self, network_id, subnet_id, ip_addr_pool, name,
                       volume_type_id, description=None, host_routes=None):
        """This API create additional Storage.

        :param network_id: Network ID.
        :param subnet_id: Subnetwork ID.
        :param ip_addr_pool: The pool of IP addresses for storage nodes used by the volume.
                             The IP address range may be overwraped with subnet's allocation_pools.
                             The range should be included in CIDR of the subnet.
        :param name: Name of Virtual Storage.
        :param volume_type_id: volume type ID.
        :param description: Description of Virtual Storage.
        :param host_routes: Static routes settings for each virtual storages.
        :return: :class:`~ecl.storage.v1.storage.Storage`
        """
        body = {"network_id": network_id, "subnet_id": subnet_id, "ip_addr_pool": ip_addr_pool, "name": name,
                "volume_type_id": volume_type_id}
        if description:
            body["description"] = description
        if host_routes:
            body["host_routes"] = host_routes
        storage = _storage.Storage()
        return storage.create(self.session, **body)

    def update_storage(self, storage_id, **body):
        """This API update existing storage

        :param kwargs body: Request parameter to update storage.

            * storage_id: ID for the requested storage.
            * name: Name of Virtual Storage.
            * description: Description of Virtual Storage.
            * ip_addr_pool: The pool of IP addresses for storage nodes used by the volume. The IP address range may be
              overwrapped with subnet's allocation_pools. The range should be included in CIDR of the subnet.
            * host_routes: Static routes settings for each virtual storages.
        :return: :class:`~ecl.storage.v1.storage.Storage`
        """
        storage = _storage.Storage()
        return storage.update(self.session, storage_id, **body)

    def delete_storage(self, storage_id):
        """This API deletes a specified storage.

        :param storage_id: ID for the specified storage.
        :return: ``None``
        """

        return self._delete(_storage.Storage, storage_id)

    def volumes(self, details=True):
        """Return a list of volumes

        :param bool details: When ``True``, returns
                             :class:`~ecl.storage.v1.volume_type.VolumeTypeDetail` objects,
                             otherwise :class:`~ecl.storage.v1.volume_type.VolumeType`.
                             *Default: ``True``*
        :returns: A generator of volume type objects
        """
        volume = _volume.VolumeDetail if details else _volume.Volume
        return list(self._list(volume, paginated=False))

    def get_volume(self, volume_id):
        """Get a single volume

        :param volume_id: The value is the ID of a volume
        :returns: One :class:`~ecl.storage.v1.volume.Volume`
                      :class:`~ecl.exceptions.ResourceNotFound`
                      when no resource can be found.
        """
        return self._get(_volume.Volume, volume_id)

    def create_volume(self, virtual_storage_id, name, size, description=None,
                      iops_per_gb=None, initiator_iqns=None, throughput=None,
                      availability_zone=None):
        """This API create additional Volume.

        :param virtual_storage_id: Virtual Storage ID.
        :param name: Name of volume.
        :param size: Size of volume in Gigabyte.
        :param description: Description of volume.
        :param iops_per_gb: Provisioned IOPS/GB for volume.
        :param throughput: Provisioned throughput for volume.
        :param initiator_iqns: List of initiator IQN who can access to this volume.
        :param availability_zone: Availability zone.
        :return: :class:`~ecl.storage.v1.volume.Volume`
        """
        body = {"virtual_storage_id": virtual_storage_id, "name": name, "size": size}
        if description:
            body["description"] = description
        if iops_per_gb:
            body["iops_per_gb"] = iops_per_gb
        if throughput:
            body["throughput"] = throughput
        if initiator_iqns:
            body["initiator_iqns"] = initiator_iqns
        if availability_zone:
            body["availability_zone"] = availability_zone
        volume = _volume.Volume()
        return volume.create(self.session, **body)

    def update_volume(self, volume_id, **body):
        """This API update existing volume.

        :param kwargs body: Request parameter to update volume.

            * volume_id: ID for the requested volume.
            * name: Name of volume.
            * description: Description of volume.
            * initiator_iqns: List of initiator IQN who can access to this volume.
        :return: :class:`~ecl.storage.v1.volume.Volume`
        """
        volume = _volume.Volume()
        return volume.update(self.session, volume_id, **body)

    def delete_volume(self, volume_id):
        """This API deletes a specified volume.

        :param  volume_id: ID for the specified volume.
        :return: ``None``
        """

        return self._delete(_volume.Volume, volume_id)

    def snapshots(self, details=True, **params):
        """Return a list of snapshots.

        :param bool details: When ``True``, returns
                             :class:`~ecl.storage.v1.snapshot.SnapshotDetail` objects,
                             otherwise :class:`~ecl.storage.v1.snapshot.Snapshot`.
                             *Default: ``True``*
        :param kwargs params: parameter used as query parameter
                              for GET request.
        :returns: A list of snapshot objects
        """
        snapshot = _snapshot.SnapshotDetail if details else _snapshot.Snapshot
        return list(self._list(snapshot, paginated=False, **params))

    def get_snapshot(self, snapshot_id):
        """Get a single snapshot.

        :param snapshot_id: The value is the ID of a snapshot
        :returns: One :class:`~ecl.storage.v1.snapshot.Snapshot`
                      :class:`~ecl.exceptions.ResourceNotFound`
                      when no resource can be found.
        """
        return self._get(_snapshot.Snapshot, snapshot_id)

    def create_snapshot(self, volume_id, name, description=None):
        """This API create snapshot of volume.

        :param volume_id: Parent volume ID.
        :param name: Name of snapshot.
        :param description: Description of snapshot.
        :return: :class:`~ecl.storage.v1.snapshot.Snapshot`
        """
        body = {}
        body["volume_id"] = volume_id
        body["name"] = name
        if description:
            body["description"] = description
        snapshot = _snapshot.Snapshot()
        return snapshot.create(self.session, **body)

    def update_snapshot(self, snapshot_id, **body):
        """This API update existing snapshot.

        :param snapshot_id: ID for the requested snapshot.
        :param name: Name of snapshot.
        :param description: Description of snapshot.
        :return: :class:`~ecl.storage.v1.snapshot.Snapshot`
        """
        snapshot = _snapshot.Snapshot()
        return snapshot.update(self.session, snapshot_id, **body)

    def delete_snapshot(self, snapshot_id):
        """This API deletes a specified snapshot.

        :param  snapshot_id: ID for the specified snapshot.
        :return: ``None``
        """
        return self._delete(_snapshot.Snapshot, snapshot_id)

    def restore_snapshot(self, snapshot_id):
        """Restore volume from snapshot.

        :param snapshot_id: Snapshot ID to utilize as restore source.
        :return: <Response 202>
        """
        snapshot = self.get_snapshot(snapshot_id)
        return snapshot.restore(self.session)

    def get_version(self):
        """
        Show Storage API version.

        :return: :class:`~ecl.storage.version.Version`
        """

        version = _version.Version()
        v_session = VersionSession(
            profile=self.session.profile,
            user_agent=self.session.user_agent,
        )
        for attr, value in six.iteritems(self.session.__dict__):
            v_session.__setattr__(attr, value)

        return version.get_version(session=v_session)

    def versions(self):
        """
        List Storage API version.

        :return: A generator of version objects
        """

        version = _version.Version()
        v_session = VersionSession(
            profile=self.session.profile,
            user_agent=self.session.user_agent,
        )
        for attr, value in six.iteritems(self.session.__dict__):
            v_session.__setattr__(attr, value)

        return list(version.list_version(session=v_session))
