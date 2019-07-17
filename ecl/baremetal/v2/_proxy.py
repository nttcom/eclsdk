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

from ecl.baremetal.v2 import flavor as _flavor
from ecl.baremetal.v2 import keypair as _keypair
from ecl.baremetal.v2 import limits as _limits
from ecl.baremetal.v2 import metadata as _metadata
from ecl.baremetal.v2 import uefi as _uefi
from ecl.baremetal.v2 import availability_zone as _zone
from ecl.baremetal.v2 import stock as _stock
from ecl.baremetal.v2 import nic_physical_port as _port
from ecl.baremetal.v2 import server as _server
from ecl.baremetal import version as _version
from ecl import proxy2
from ecl import session


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
    def availability_zones(self):
        """Return a list of availability zones for baremetal servers

        :returns: List of :class:`~ecl.baremetal.v2.availability_zone.AvailabilityZone`
        """
        return list(self._list(_zone.AvailabilityZone))

    def find_availability_zone(self, name_or_id, ignore_missing=False):
        """Find a single availability_zone

        :param string name_or_id: The name or ID of an availability zone.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: :class:`~ecl.baremetal.v2.availability_zone.AvailabilityZone` or ``None``
        """
        return self._find(_zone.AvailabilityZone, name_or_id,
                          ignore_missing=ignore_missing)

    def get_limits(self):
        """This API lists the current limits for the account

        :return: :class:`~ecl.baremetal.v2.limits.Limits`
        """

        limits = _limits.Limits()
        return limits.get(session=self.session)

    def flavors(self, details=True):
        """Lists all Flavor. That hash only id, links and name.
        If you want to get detail flavor information, call List Flavors
        Detail API. A flavor is a hardware configuration for a server.
        Each flavor is a unique combination of disk space and memory
        capacity.

        :return: A List of :class:`~ecl.baremetal.v2.flavor.Flavor`
        """
        flavor = _flavor.FlavorDetail if details else _flavor.Flavor
        return list(self._list(flavor))

    def get_flavor(self, flavor_id):
        """Gets details for a FlavorDetail associated with flavor_id.
        A flavor is a hardware configuration for a server.
        Each flavor is a unique combination of disk space and memory
        capacity.

        :param string flavor_id: ID of a flavor.
        :return: :class:`~ecl.baremetal.v2.flavor.Flavor`
        """
        return self._get(_flavor.Flavor, flavor_id)

    def find_flavor(self, name_or_id, ignore_missing=False):
        """Find a single flavor

        :param string name_or_id: Name or ID of a flavor.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :return: :class:`~ecl.baremetal.v2.flavor.Flavor` or ``None``
        """
        return self._find(_flavor.Flavor, name_or_id, ignore_missing=ignore_missing)

    def keypairs(self):
        """Lists name, public_key and finger_print for all KeyPairs.

        :return: A list of :class:`~ecl.baremetal.v2.keypair.Keypair`
        """
        keypairs = _keypair.Keypair()
        return list(keypairs.list(session=self.session))

    def get_keypair(self, keypair_name):
        """Show a KeyPair associated with keypair_name.

        :param string keypair_name: The name associated with a KeyPair.
        :return: :class:`~ecl.baremetal.v2.keypair.Keypair`
        """
        return self._get(_keypair.Keypair, keypair_name)

    def create_keypair(self, name, public_key=None):
        """Generate or import SSH keys. After generating a KeyPair,
        please specify the key_name parameter in the request body
        in Create Server request to associate the new server with SSH keys.

        :param string name: The name associated with a KeyPair.
        :param string public_key: Keypair's public key.
            If you do not specify this parameter,
            You can get the private key from Responce.
        :return: :class:`~ecl.baremetal.keypair.Keypair`
        """
        attrs = {"name": name}
        if public_key:
            attrs["public_key"] = public_key
        return self._create(_keypair.Keypair, **attrs)

    def delete_keypair(self, keypair_name):
        """Delete KeyPair associated with keypair_name.

        :param string keypair_name: The name associated with a KeyPair.
        :return: ``None``
        """
        return self._delete(_keypair.Keypair, keypair_name)

    def get_uefi(self, server_id):
        """This API shows the UEFI setting information for specified Baremetal server.

        :param string server_id: ID for the requested server.
        :return: :class:`~ecl.baremetal.uefi.UEFI`
        """
        uefi = _uefi.UEFI()
        return uefi.get(self.session, server_id)

    def update_uefi(self, server_id, **attrs):
        """Updates UEFI setting of specified Baremetal server.
        This request will be accepted only when the task_state is None.

        :param string server_id: ID for the requested server.
        :param kwargs attrs: Attributes to be passed onto the
                           :meth:`~ecl.baremetal.uefi.UEFI.update`
                           method to be updated.
        :return: :class:`~ecl.baremetal.uefi.UEFI`
        """
        uefi = _uefi.UEFI()
        return uefi.update(self.session, server_id, **attrs)

    def get_version(self):
        """Show Baremetal Server API version.

        :return: :class:`~ecl.baremetal.version.Version`
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
        """List Baremetal Server API version.

        :return: A list of :class:`~ecl.baremetal.version.Version`
        """
        version = _version.Version()
        v_session = VersionSession(
            profile=self.session.profile,
            user_agent=self.session.user_agent,
        )
        for attr, value in six.iteritems(self.session.__dict__):
            v_session.__setattr__(attr, value)
        return list(version.list_version(session=v_session))

    def get_stock(self, flavor_id, availability_zone=None):
        """This API show which Baremetal server stock is available or not.

        :param string flavor_id: UUID of the flavor for search stock.
        :param string availability_zone: Name of the AvailabilityZone.
            If you specified this parameter, search stock from Baremetal
            server that matching AvailabilityZone and flavor_id.
            If you omit this parameter, stock search from all Baremetal
            server that matching flavor_id.
        :return: :class:`~ecl.baremetal.v2.stock.Stock`
        """
        stock = _stock.Stock()
        return stock.get(self.session, flavor_id, availability_zone=availability_zone)

    def get_nic_physical_port(self, server_id, port_id):
        """This API shows the specified NicPhysicalPort information for
        specified server.

        :param string server_id: ID for the specified server.
        :param string port_id: ID for the specified network interface port.
        :return: :class:`~ecl.baremetal.v2.nic_physical_port.NicPhysicalPort`
        """
        port = _port.NicPhysicalPort()
        return port.get(self.session, server_id, port_id)

    def nic_physical_ports(self, server_id):
        """This API lists all NicPhysicalPort information for the
        specified server.

        :param string server_id: ID for the specified server.
        :return: A list of :class:`~ecl.baremetal.v2.nic_physical_port.NicPhysicalPort`
        """
        port = _port.NicPhysicalPort()
        return list(port.list(self.session, server_id))

    def servers(self, details=True, **attrs):
        """This API lists your Baremetal servers information.

        :param bool details: When set to ``False``
                    :class:`~ecl.baremetal.v2.server.Server` instance
                    will be returned. The default, ``True``, will cause
                    :class:`~ecl.baremetal.v2.server.ServerDetail`
                    instances to be returned.
        :param attrs: Attributes to be passed onto the
                    :meth:`~ecl.baremetal.server.Server.list` method.
        :return: A list of :class:`~ecl.baremetal.v2.server.Server`
        """
        server = _server.ServerDetail if details else _server.Server
        return list(self._list(server, **attrs))

    def get_server(self, server_id):
        """Show your Baremetal server's information.

        :param string server_id: ID for specified server.
        :return: :class:`~ecl.baremetal.v2.server.Server`
        """
        return self._get(_server.Server, server_id)

    def find_server(self, name_or_id, ignore_missing=False):
        """Find a single baremetal server

        :param string name_or_id: Name or ID of a server.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :return: :class:`~ecl.baremetal.v2.server.Server` or ``None``
        """
        return self._find(_server.Server, name_or_id, ignore_missing=ignore_missing)

    def create_server(self, name, networks, flavor, admin_pass=None,
                      image=None, key_name=None, availability_zone=None,
                      user_data=None, raid_arrays=None,
                      lvm_volume_groups=None, filesystems=None,
                      metadata=None, personality=None):
        """This API create additional Baremetal server.

        :param string name: Name of your Baremetal server as a string.
        :param array networks: Network Array.
            If it is specified greater than two, default gateway is
            first network.
        :param string flavor: The flavor reference for the desired flavor for your
            Baremetal server.
        :param string admin_pass: Password for the administrator.
        :param string image: The image reference for the desired image for your
            Baremetal server.
        :param string key_name: SSH Keypair name you created on KeyPairs API.
        :param string availability_zone: The availability zone name in which to launch
            the server.
        :param string user_data: Configuration information or scripts to use upon
            launch. Must be Base64 encoded. Maximum size is 65535 bytes.
        :param array raid_arrays: Raid Arrays information.
        :param array lvm_volume_groups: LVM information. must be sure to specify
            if you have to true lvm parameters Raid Arrays.
        :param array filesystems: Partition filesystem / mount point information.
        :param dict metadata: Metadata key and value pairs. The maximum size of the
            metadata key and value is 255 bytes each.
        :param array personality: File path and contents (text only) to inject into
            your Baremetal server at launch. This parameter is not supported in
            esxi.
        :return: :class:`~ecl.baremetal.v2.server.Server`
        """
        attrs = {"name": name, "networks": networks, "flavorRef": flavor}
        if admin_pass:
            attrs["adminPass"] = admin_pass
        if image:
            attrs["imageRef"] = image
        if key_name:
            attrs["key_name"] = key_name
        if availability_zone:
            attrs["availability_zone"] = availability_zone
        if user_data:
            attrs["user_data"] = user_data
        if raid_arrays:
            attrs["raid_arrays"] = raid_arrays
        if lvm_volume_groups:
            attrs["lvm_volume_groups"] = lvm_volume_groups
        if filesystems:
            attrs["filesystems"] = filesystems
        if metadata:
            attrs["metadata"] = metadata
        if personality:
            attrs["personality"] = personality
        server = _server.Server()
        return server.create(self.session, **attrs)

    def delete_server(self, server_id):
        """This API deletes a specified Baremetal server.

        :param string server_id: ID for the specified server.
        :return: ``None``
        """
        return self._delete(_server.Server, server_id)

    def start_server(self, server_id, boot_mode):
        """Power on the Baremetal Server associated with server_id.
        This request will be accepted only when the task_state is None.

        :param string server_id: ID for the server.
        :param string boot_mode: Baremetal Server boot mode.
            A valid value is DISK, PXE, LEGACY or ISO.
        :return: ``None``
        """
        server = _server.ServerAction()
        return server.start(self.session, server_id, boot_mode)

    def stop_server(self, server_id, type=None):
        """Stop the Baremetal Server associated with server_id.
        This request will be accepted only when the task_state is None.

        :param string server_id: ID for the server.
        :param string type: Baremetal Server shutdown mode.
            A valid value is HARD or SOFT.
        :return: ``None``
        """
        server = _server.ServerAction()
        return server.stop(self.session, server_id, type)

    def reboot_server(self, server_id, type, boot_mode):
        """Reboot the Baremetal Server associated with server_id.
        This request will be accepted only when the task_state is None.

        :param string server_id: ID for the server.
        :param string type: Baremetal Server shutdown mode.
            A valid value is HARD or SOFT. HARD is force restart by IPMI.
            This operations is equal to power down.
            SOFT is restated by ACPI.
        :param string boot_mode: Baremetal Server boot mode.
            A valid value is DISK, PXE, LEGACY or ISO.
        :return: ``None``
        """
        server = _server.ServerAction()
        return server.reboot(self.session, server_id, type, boot_mode)

    def media_attach(self, server_id, image):
        """Attach media to the Baremetal Server associated with server_id.
        This request will be accepted only when the task_state is None.

        :param string server_id: ID for the server.
        :param string image: ID of the image you want to attach.
        :return: ``None``
        """
        server = _server.ServerAction()
        return server.media_attach(self.session, server_id, image)

    def media_detach(self, server_id, image):
        """Detach media from the Baremetal Server associated with server_id.
        This request will be accepted only when the task_state is None.

        :param string server_id: ID for the server.
        :param string image: ID of the image you want to detach.
        :return: ``None``
        """
        server = _server.ServerAction()
        return server.media_detach(self.session, server_id, image)

    def get_management_console(self, server_id):
        """Gets information to access the remote console of Baremetal
        Server. This request will be accepted only when the task_state
        is None.
        This API response console parameters are used at Remote Console
        Access - Get Started. To access your Baremetal Server, you have
        to create VPN user and connect to VPN.

        :param string server_id: ID for the server.
        :return: :class:`~ecl.baremetal.v2.server.ServerAction`
        """
        server = _server.ServerAction()
        return server.get_management_console(self.session, server_id)

    def metadata(self, server_id):
        """This API lists metadata for a specified server.

        :param string server_id: ID for specified server.
        :return: A list of :class:`~ecl.baremetal.v2.metadata.Metadata`
        """
        metadata = _metadata.Metadata()
        return list(metadata.list(self.session, server_id))

    def show_metadata(self, server_id, key):
        """This API shows metadata item (key and value) by specifying key
        for a specified server.

        :param string server_id: ID for specified server.
        :param string key: A string. Maximum length is 255 characters.
        :return: :class:`~ecl.baremetal.v2.metadata.Metadata`
        """
        metadata = _metadata.Metadata()
        return metadata.get(self.session, server_id, key)

    def delete_metadata(self, server_id, key):
        """This API deletes metadata item (key and value) by specifying
        key for a specified server.

        :param string server_id: ID for specified server.
        :param string key: A string. Maximum length is 255 characters.
        :return: ``None``
        """
        metadata = _metadata.Metadata()
        return metadata.delete(self.session, server_id, key)

    def merge_metadata(self, server_id, **attr):
        """This API creates or merges metadata for a specified server.
        This API replaces items which match the specified keys in the
        request. This API does not remove items, unlike Replace Server
        Metadata Items.

        :param string server_id: ID for specified server.
        :param kwargs attr: Keyword arguments which will be used to do update
                     process for :class:`~ecl.baremetal.metadata.Metadata`.
        :return: :class:`~ecl.baremetal.v2.metadata.Metadata`
        """
        metadata = _metadata.Metadata()
        return metadata.merge(self.session, server_id, **attr)

    def replace_metadata(self, server_id, **attr):
        """This API creates or replaces metadata for a specified server.
        All existing metadata items are removed and completely replaced
        by the metadata items in the request. If you don't want to remove
        existing items, please use Merge Server Metadata Items.

        :param string server_id: ID for specified server.
        :param kwargs attr: Keyword arguments which will be used to do update
                     process for :class:`~ecl.baremetal.metadata.Metadata`.
        :return: :class:`~ecl.baremetal.v2.metadata.Metadata`
        """
        metadata = _metadata.Metadata()
        return metadata.replace(self.session, server_id, **attr)

    def update_metadata(self, server_id, key, **attr):
        """This API sets additonal metadata item (key and value) by
        specifying key for a specified server.

        :param string server_id: ID for specified server.
        :param string key: A string. Maximum length is 255 characters.
        :param kwargs attr: Keyword arguments which will be used to do update
                     process for :class:`~ecl.baremetal.metadata.Metadata`.
        :return: :class:`~ecl.baremetal.v2.metadata.Metadata`
        """
        metadata = _metadata.Metadata()
        return metadata.update(self.session, server_id, key, **attr)
