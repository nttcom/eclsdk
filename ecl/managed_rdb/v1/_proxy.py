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

from ecl.managed_rdb.v1 import database_version as _database_version
from ecl.managed_rdb.v1 import flavor as _flavor
from ecl.managed_rdb.v1 import instance as _instance
from ecl.managed_rdb.v1 import metadata as _metadata
from ecl.managed_rdb.v1 import quota as _quota
from ecl.managed_rdb.v1 import storage_type as _storage_type
from ecl import proxy2


class Proxy(proxy2.BaseProxy):
    def instances(self, details=True, **attrs):
        """This API lists your mRDB instances information.

        :param bool details: When set to ``False``
                    :class:`~ecl.mrdb.v1.instance.Instance` instance
                    will be returned.
                    The default, ``True``, will cause
                    :class:`~ecl.mrdb.v1.instance.InstanceDetail`
                    instances to be returned.
        :param attrs: Attributes to be passed onto the
                    :meth:`~ecl.mrdb.instance.Instance.list` method.
        :return: A list of :class:`~ecl.mrdb.v1.instance.Instance`
        """
        instance = _instance.InstanceDetail if details else _instance.Instance
        return list(self._list(instance, **attrs))

    def get_instance(self, instance_id):
        """Show your mRDB instance's information.

        :param string instance_id: ID for specified instance.
        :return: :class:`~ecl.mrdb.v1.instance.Instance`
        """
        return self._get(_instance.Instance, instance_id)

    def find_instance(self, name_or_id, ignore_missing=False):
        """Find a single mRDB instance

        :param string name_or_id: Name or ID of a instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :return: :class:`~ecl.mrdb.v1.instance.Instance` or ``None``
        """
        return self._find(_instance.Instance, name_or_id, ignore_missing=ignore_missing)

    def create_instance(self, flavor, database_version, storage_type,
                        high_availability, network, name=None, description=None,
                        metadata=None, admin_password=None):
        """This API create additional mRDB instance.

        :param string flavor: Name of flavor. ex) 4CPU-32GB
        :param string database_version: Name of database version. ex) POSTGRES_13_2
        :param string storage_type: Name of storage type. ex) 4IOPS-500GB
        :param boolean high_availability: Needs high availability for your instance.
            True if you want to enable HA configuration.
            False if you don't want to enable HA configuration.
        :param dict network: Network of your instance.
        :param string name: Name of your instance.
            Multibyte characters are available.
        :param string description: Description of your instance.
            Multibyte characters are available.
        :param dict metadata: Metadata of your instance.
        :param string admin_password: Password for DB admin user (e.g. postgres/root).
            If this parameter is blank or null, controller automatically generates
            a password at random.
        :return: :class:`~ecl.mrdb.v1.instance.Instance`
        """
        attrs = {
            "flavor": flavor,
            "database_version": database_version,
            "storage_type": storage_type,
            "high_availability": high_availability,
            "network": network
        }
        if name:
            attrs["name"] = name
        if description:
            attrs["description"] = description
        if metadata:
            attrs["metadata"] = metadata
        if admin_password:
            attrs["admin_password"] = admin_password
        return _instance.Instance().create(self.session, **attrs)

    def delete_instance(self, instance_id):
        """This API deletes a specified mRDB instance.

        :param string instance_id: ID for the specified instance.
        :return: ``None``
        """
        return self._delete(_instance.Instance, instance_id)

    def update_instance(self, instance_id, name=None, description=None):
        """ This API updates the editable attributes of the specified mRDB instance.

        :param string instance_id: ID for the specified instance.
        :param string name: Name of your instance.
            Multibyte characters are available.
        :param string description: Description of your instance.
            Multibyte characters are available.
        :return: :class:`~ecl.mrdb.v1.instance.Instance`
        """
        attrs = {}
        if name:
            attrs["name"] = name
        if description:
            attrs["description"] = description
        instance = _instance.Instance()
        return instance.update(self.session, instance_id, **attrs)

    def change_password(self, instance_id, new_password=None):
        """Change DB admin user's password with instance_id.

        :param string instance_id: ID for the specified instance.
        :param string new_password: New password for DB admin user (e.g. postgres/root).
            If this parameter is blank or null, controller automatically generates
            a password at random.
        :return: ``None``
        """
        attrs = {}
        if new_password:
            attrs['admin_password'] = new_password
        instance = _instance.InstanceAction()
        return instance.change_password(self.session, instance_id, **attrs)

    def metadatas(self, instance_id):
        """This API lists metadata for a specified mRDB instance.

        :param string instance_id: ID for specified mRDB instance.
        :return: A list of :class:`~ecl.baremetal.v2.metadata.Metadata`
        """
        return _metadata.Metadata().list(self.session, instance_id)

    def replace_metadata(self, instance_id, metadata):
        """This API creates or replaces metadata for a specified mRDB instance.
        All existing metadata items are removed and completely replaced
        by the metadata items in the request. If you don't want to remove
        existing items, please use Merge Server Metadata Items.

        :param string instance_id: ID for specified mRDB instance.
        :param dict metadata: Metadata of your instance.
        :param kwargs attr: Keyword arguments which will be used to do update
                     process for :class:`~ecl.baremetal.metadata.Metadata`.
        :return: :class:`~ecl.baremetal.v2.metadata.Metadata`
        """
        return _metadata.Metadata().replace(self.session, instance_id, metadata)

    def flavors(self, **attrs):
        """This API lists your Flavors information.

        :param attrs: Attributes to be passed onto the
                    :meth:`~ecl.mrdb.flavor.Flavor.list` method.
        :return: A list of :class:`~ecl.mrdb.v1.flavor.Flavor`
        """
        return list(self._list(_flavor.Flavor, **attrs))

    def get_flavor(self, flavor_id):
        """Show your Flavor's information.

        :param string flavor_id: ID for specified flavor.
        :return: :class:`~ecl.mrdb.v1.flavor.Flavor`
        """
        return self._get(_flavor.Flavor, flavor_id)

    def database_versions(self, **attrs):
        """This API lists your database versions information.

        :param attrs: Attributes to be passed onto the
                    :meth:`~ecl.mrdb.database_version.DatabaseVersion.list` method.
        :return: A list of :class:`~ecl.mrdb.v1.database_version.DatabaseVersion`
        """
        return list(self._list(_database_version.DatabaseVersion, **attrs))

    def get_database_version(self, database_version_id):
        """Show your database version's information.

        :param string database_version_id: ID for specified database version.
        :return: :class:`~ecl.mrdb.v1.database_version.DatabaseVersion`
        """
        return self._get(_database_version.DatabaseVersion, database_version_id)

    def storage_types(self, **attrs):
        """This API lists your storage types information.

        :param attrs: Attributes to be passed onto the
                    :meth:`~ecl.mrdb.storage_type.StorageType.list` method.
        :return: A list of :class:`~ecl.mrdb.v1.storage_type.StorageType`
        """
        return _storage_type.StorageType().list(self.session)

    def show_quota(self):
        """Show your quota of mRDB service.

        :return: :class:`~ecl.mrdb.v1.quota.Quota`
        """
        return _quota.Quota().show(self.session)
