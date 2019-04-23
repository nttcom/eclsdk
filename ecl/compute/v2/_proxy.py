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

from ecl.compute.v2 import availability_zone as _availability_zone
from ecl.compute.v2 import extension
from ecl.compute.v2 import flavor as _flavor
from ecl.compute.v2 import image as _image
from ecl.compute.v2 import keypair as _keypair
from ecl.compute.v2 import limits
from ecl.compute.v2 import server as _server
from ecl.compute.v2 import server_action as _server_action
from ecl.compute.v2 import server_interface as _server_interface
from ecl.compute.v2 import server_volume as _server_volume
from ecl.compute.v2 import quota as _quota
from ecl.compute.v2 import volume as _volume
from ecl.image.v2 import image

from ecl import proxy2
from ecl import resource2


class Proxy(proxy2.BaseProxy):

    def servers(self, details=True, **query):
        """Retrieve a list of servers

        :param bool details: When set to ``False``
                    :class:`~ecl.compute.v2.server.Server` instances
                    will be returned. The default, ``True``, will cause
                    :class:`~ecl.compute.v2.server.ServerDetail`
                    instances to be returned.
        :param kwargs \*\*query: Optional query parameters to be sent to limit
            the servers being returned.  Available parameters include:

            * changes_since: A time/date stamp for when the server last changed status.
            * image: An image resource or ID.
            * flavor: A flavor resource or ID.
            * name: Name of the server as a string.
            * status: Value of the status of the server so that you can filter on "ACTIVE" for example.
            * host: Name of the host as a string.
            * limit: Requests a specified page size of returned items from the query.
            * marker: Specifies the ID of the last-seen item.
        :returns: A list of :class:`~ecl.compute.v2.server.Server`
        """
        srv = _server.ServerDetail if details else _server.Server
        return list(self._list(srv, paginated=True, **query))

    def create_server(self, flavor_id, name, disk_config=None, image_id=None,
                      min_count=None, max_count=None, availability_zone=None,
                      config_drive=None, key_name=None, user_data=None,
                      block_device_mapping=None, block_device_mapping_v2=None,
                      metadata=None, networks=None, personality=None, admin_pass=None, **attrs):
        """Create a new server from attributes

        :param string flavor_id: ID of server
        :param string name: Name of server
        :param dict disk_config: a single partition which is expanded
                to the size of the flavor selected
        :param string image_id: if block_device_mapping_v2 is not specified,
                it is require
        :param int min_count: minim count of instance
        :param int max_count: maxmum count of instance
        :param string availability_zone: availability zone
        :param boolean config_drive: Enables metadata injection in a server
                through a configuration drive
        :param string key_name: key name
        :param string (Base64 encoded) user_data: user data
        :param array block_device_mapping: block device mapping info
        :param array block_device_mapping_v2:  block device mapping v2 info
        :param dict metadata: metadata of the server
        :param array networks: if a tenant has more than two networks, it is required
        :param array personality: This param will not run for ECL2.0
        :param string admin_pass: the administrator password for the server
        :param kwargs attrs: Keyword arguments which will be used to create
            a :class:`~ecl.compute.v2.server.Server`,
            comprised of the properties on the Server class.
        :returns: :class:`~ecl.compute.v2.server.Server`
        """
        attrs.update({"flavor_id": flavor_id})
        attrs.update({"name": name})
        if disk_config is not None:
            attrs.update({"disk_config": disk_config})
        if image_id is not None:
            attrs.update({"image_id": image_id})
        if min_count:
            attrs.update({"min_count": min_count})
        if max_count:
            attrs.update({"max_count": max_count})
        if availability_zone:
            attrs.update({"availability_zone": availability_zone})
        if config_drive:
            attrs.update({"config_drive": config_drive})
        if key_name:
            attrs.update({"key_name": key_name})
        if user_data:
            attrs.update({"user_data": user_data})
        if block_device_mapping:
            attrs.update({"block_device_mapping": block_device_mapping})
        if block_device_mapping_v2:
            attrs.update({"block_device_mapping_v2": block_device_mapping_v2})
        if metadata:
            attrs.update({"metadata": metadata})
        if networks:
            attrs.update({"networks": networks})
        if personality:
            attrs.update({"personality": personality})
        if admin_pass:
            attrs.update({"admin_pass": admin_pass})
        return self._create(_server.Server, **attrs)

    def delete_server(self, server, ignore_missing=False, force=False):
        """Delete a server

        :param server: The value can be either the ID of a server or a
                       :class:`~ecl.compute.v2.server.Server` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the server does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent server
        :param bool force: When set to ``True``, the server deletion will be
                           forced immediatly.
        :returns: ``None``
        """
        if force:
            server = self._get_resource(_server.Server, server)
            server.force_delete(self.session)
        else:
            self._delete(_server.Server, server, ignore_missing=ignore_missing)

    def find_server(self, name_or_id, ignore_missing=False):
        """Find a single server

        :param string name_or_id: The name or ID of a server.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: :class:`~ecl.compute.v2.server.Server` or None
        """
        return self._find(_server.Server, name_or_id,
                          ignore_missing=ignore_missing)

    def get_server(self, server):
        """Get a single server

        :param server: The value can be the ID of a server or a
                       :class:`~ecl.compute.v2.server.Server` instance.

        :returns: :class:`~ecl.compute.v2.server.Server`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_server.Server, server)

    def update_server(self, server, **body):
        """Update a server

        :param server: Either the ID of a server or a
                       :class:`~ecl.compute.v2.server.Server` instance.
        :param string name: Server name
        :param string access_ipv4: IPv4 address
        :param string access_ipv6: IPv6 address

        :returns: :class:`~ecl.compute.v2.server.Server`
        """
        return self._update(_server.Server, server, **body)

    def wait_for_server(self, server, status='ACTIVE', failures=['ERROR'],
                        interval=2, wait=120):
        """Not supported
        """
        return resource2.wait_for_status(self.session, server, status,
                                         failures, interval, wait)

    def create_image_from_server(self, server, name, metadata=None):
        """Create image from a certain server

        :param server: Either the ID of a server or a
                       :class:`~ecl.compute.v2.server.Server` instance.
        :param string name: Image name (1-255 characters).
        :param dict metadata: Image metadata ({"metadata_key": "metadata_value"})
        :returns: ``None``
        """
        virtual_server = self.get_server(server)
        return virtual_server.create_image(self.session, name, metadata)

    def get_server_console(self, server, vnc_type):
        """Get the console link of server

        :param server: Either the ID of a server or a
                       :class:`~ecl.compute.v2.server.Server` instance.
        :param vnc_type: should be one of these: novnc, rdp-html5, spice-html5, serial
        :return: console link and type info
        :rtype: :class:`~dict {"url": "", "type": ""}`
        """
        virtual_server = self.get_server(server)
        return virtual_server.get_console(self.session, vnc_type)

    def start_server(self, server):
        """Start the server

        :param server: Either the ID of a server or a
                       :class:`~ecl.compute.v2.server.Server` instance.
        :return: <Response 202>
        """
        virtual_server = self.get_server(server)
        return virtual_server.start(self.session)

    def stop_server(self, server):
        """Stop the server

        :param server: Either the ID of a server or a
                       :class:`~ecl.compute.v2.server.Server` instance.
        :return: <Response 202>
        """
        virtual_server = self.get_server(server)
        return virtual_server.stop(self.session)

    def resize_server(self, server, flavor_id):
        """Resize the server to flavor reference

        :param server: Either the ID of a server or a
                       :class:`~ecl.compute.v2.server.Server` instance.
        :param string flavor_id: ID of flavor to resize
        :return: <Response 202>
        """
        virtual_server = self.get_server(server)
        return virtual_server.resize(self.session, flavor_id)

    def get_server_metadata(self, server):
        """Return a dictionary of metadata for a server

        :param server: Either the ID of a server or a
                       :class:`~ecl.compute.v2.server.Server` or
                       :class:`~ecl.compute.v2.server.ServerDetail`
                       instance.

        :returns: A :class:`~ecl.compute.v2.server.Server` with only the
                  server's metadata. All keys and values are Unicode text.
        """
        res = self.get_server(server)
        metadata = res.get_metadata(self.session)
        result = _server.Server.existing(id=res.id, metadata=metadata)
        return result

    def set_server_metadata(self, server, **metadata):
        """Update metadata for a server

        :param server: Either the ID of a server or a
                       :class:`~ecl.compute.v2.server.Server` or
                       :class:`~ecl.compute.v2.server.ServerDetail`
                       instance.
        :param kwargs metadata: Key/value pairs to be updated in the server's
                                metadata. No other metadata is modified
                                by this call. All keys and values are stored
                                as Unicode.
        :returns: A :class:`~ecl.compute.v2.server.Server` with only the
                  server's metadata. All keys and values are Unicode text.
        """
        res = self.get_server(server)
        metadata = res.set_metadata(self.session, **metadata)
        result = _server.Server.existing(id=res.id, metadata=metadata)
        return result

    def delete_server_metadata(self, server, keys):
        """Delete metadata for a server

        Note: This method will do a HTTP DELETE request for every key in keys.

        :param server: Either the ID of a server or a
                       :class:`~ecl.compute.v2.server.Server` or
                       :class:`~ecl.compute.v2.server.ServerDetail`
                       instance.
        :param array keys: The keys to delete
        :returns: ``None``
        """
        res = self.get_server(server)
        return res.delete_metadata(self.session, keys)

    def create_server_interface(self, server, net_id=None, ip_address=None,
                                port_id=None, fixed_ips=None):
        """Create a new server interface from attributes

        :param server: The server can be either the ID of a server or a
                       :class:`~ecl.compute.v2.server.Server` instance
                       that the interface belongs to.
        :param string net_id: ID of network, may need to specify ip address
                        if
        :param string ip_address: ip_address of add interface to the VM instance
        :param string port_id: ID of port of add interface to the VM instance
        :param dict fixed_ips: dict of fixed ips to add to the VM instance
        :returns: :class:`~ecl.compute.v2.server_interface.ServerInterface`
        """
        attrs = {}
        if net_id is not None:
            attrs.update({"net_id": net_id})
        if ip_address is not None:
            attrs.update({
                "fixed_ips": {
                    "ip_address": ip_address
                }
            })
        if port_id is not None:
            attrs.update({"port_id": port_id})
        if fixed_ips is not None:
            attrs.update({"fixed_ips": fixed_ips})
        server_id = resource2.Resource._get_id(server)
        return self._create(_server_interface.ServerInterface,
                            server_id=server_id, **attrs)

    def delete_server_interface(self, server_interface, server=None,
                                ignore_missing=False):
        """Delete a server interface

        :param server_interface:
            The value can be either the ID of a server interface or a
            :class:`~ecl.compute.v2.server_interface.ServerInterface`
            instance.
        :param server: This parameter need to be specified when ServerInterface
                       ID is given as value. It can be either the ID of a
                       server or a :class:`~ecl.compute.v2.server.Server`
                       instance that the interface belongs to.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the server interface does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent server interface.
        :returns: ``None``
        """
        server_id = self._get_uri_attribute(server_interface, server,
                                            "server_id")
        server_interface = resource2.Resource._get_id(server_interface)

        self._delete(_server_interface.ServerInterface,
                     port_id=server_interface,
                     server_id=server_id,
                     ignore_missing=ignore_missing)

    def server_interfaces(self, server):
        """Return a list of server interfaces

        :param server: The server can be either the ID of a server or a
                       :class:`~ecl.compute.v2.server.Server`.
        :returns: A list of
            :class:`~ecl.compute.v2.server_interface.ServerInterface`
        """
        server_id = resource2.Resource._get_id(server)
        return list(self._list(_server_interface.ServerInterface,
                               paginated=False,
                               server_id=server_id))

    def server_actions(self, server):
        """Return a list of server actions

        :param server: The server can be either the ID of a server or a
                       :class:`~ecl.compute.v2.server.Server`.
        :returns: A list of :class:`~ecl.compute.v2.server_action.ServerAction`
        """
        server_id = resource2.Resource._get_id(server)
        return list(self._list(_server_action.ServerAction, paginated=False,
                    instance_uuid=server_id))

    def get_server_action(self, server_action, server=None):
        """Get a single server action

        :param server_action:
            The value can be the request ID of a server action or a
            :class:`~ecl.compute.v2.server_action.ServerAction`
            instance.
        :param server: This parameter need to be specified when ServerAction
                       ID is given as value. It can be either the ID of a
                       server or a :class:`~ecl.compute.v2.server.Server`
                       instance that the action belongs to.
        :returns: Server Action object
            :class:`~ecl.compute.v2.server_action.ServerAction`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        server = self.get_server(server)

        action = resource2.Resource._get_id(server_action)
        return self._get(_server_action.ServerAction, action,
                         instance_uuid=server.id, )

    def server_volumes(self, server):
        """Return a list of server volumes

        :param server: The server can be either the ID of a server or a
                       :class:`~ecl.compute.v2.server.Server`.
        :returns: A list of :class:`~ecl.compute.v2.server_volume.ServerVolume`
        """
        server_id = resource2.Resource._get_id(server)
        return list(self._list(_server_volume.ServerVolume, paginated=False,
                               serverId=server_id))

    def create_server_volume(self, server, volume_id, device=None):
        """Attaches a volume to the specified server

        :param server: The server can be either the ID of a server or a
                       :class:`~ecl.compute.v2.server.Server`
        :param string volume_id: Volume ID to be attached
        :param string device: Device name that satisfies the following
            conditions: ^/dev/x{0,1}[a-z]{0,1}d{0,1})([a-z]+)[0-9]*$
        """
        attrs = {
            "volumeId": volume_id
        }
        if device:
            attrs.update({"device": device})

        server_id = resource2.Resource._get_id(server)
        return self._create(_server_volume.ServerVolume,
                            serverId=server_id, **attrs)

    def delete_server_volume(self, server_volume, server=None,
                                ignore_missing=False):
        """Detach a volume from a server

        :param server_volume:
            The value can be either the ID of a server volume or a
            :class:`~ecl.compute.v2.server_volume.ServerVolume`
            instance.
        :param server: This parameter need to be specified when ServerVolume
                       ID is given as value. It can be either the ID of a
                       server or a :class:`~ecl.compute.v2.server.Server`
                       instance that the volume belongs to.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the server volume does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent server volume.
        :returns: ``None``
        """
        server_id = self._get_uri_attribute(server_volume, server,
                                            "server_id")
        attachment = resource2.Resource._get_id(server_volume)

        self._delete(_server_volume.ServerVolume,
                     id=attachment,
                     serverId=server_id,
                     ignore_missing=ignore_missing)

    def extensions(self):
        """Retrieve a list of extensions

        :returns: A list of :class:`~ecl.compute.v2.extension.Extension`.
        """
        return list(self._list(extension.Extension, paginated=False))

    def find_flavor(self, name_or_id, ignore_missing=False):
        """Find a single flavor

        :param string name_or_id: The name or ID of a flavor.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: :class:`~ecl.compute.v2.flavor.Flavor` or None
        """
        return self._find(_flavor.Flavor, name_or_id,
                          ignore_missing=ignore_missing)

    def get_flavor(self, flavor):
        """Get a single flavor

        :param flavor: The value can be the ID of a flavor or a
                       :class:`~ecl.compute.v2.flavor.Flavor` instance.

        :returns: :class:`~ecl.compute.v2.flavor.Flavor`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_flavor.Flavor, flavor)

    def flavors(self, details=True):
        """Return a list of flavors

        :param bool details: When ``True``, returns
            :class:`~ecl.compute.v2.flavor.FlavorDetail` objects,
            otherwise :class:`~ecl.compute.v2.flavor.Flavor`.
        :returns: A list of :class:`~ecl.compute.v2.flavor.Flavor`
        """
        flv = _flavor.FlavorDetail if details else _flavor.Flavor
        return list(self._list(flv, paginated=True))

    def delete_image(self, image, ignore_missing=False):
        """Delete an image

        :param image: The value can be either the ID of an image or a
                      :class:`~ecl.compute.v2.image.Image` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the image does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent image.
        :returns: ``None``
        """
        self._delete(_image.Image, image, ignore_missing=ignore_missing)

    def find_image(self, name_or_id, ignore_missing=False):
        """Find a single image

        :param string name_or_id: The name or ID of a image.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: :class:`~ecl.compute.v2.image.Image` or None
        """
        return self._find(image.Image, name_or_id,
                          ignore_missing=ignore_missing)

    def get_image(self, image):
        """Get a single image

        :param image: The value can be the ID of an image or a
                      :class:`~ecl.compute.v2.image.Image` instance.

        :returns: :class:`~ecl.compute.v2.image.Image`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_image.Image, image)

    def images(self, details=True, **query):
        """Return a list of images

        :param bool details: When ``True``, returns
            :class:`~ecl.compute.v2.image.ImageDetail` objects,
            otherwise :class:`~ecl.compute.v2.image.Image`.
        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.
        :returns: A list of :class:`~ecl.compute.v2.image.Image`
        """
        img = _image.ImageDetail if details else _image.Image
        return list(self._list(img, paginated=True, **query))

    def _get_base_resource(self, res, base):
        # Metadata calls for Image and Server can work for both those
        # resources but also ImageDetail and ServerDetail. If we get
        # either class, use it, otherwise create an instance of the base.
        if isinstance(res, base):
            return res
        else:
            return base(id=res)

    def get_image_metadata(self, image):
        """Return a dictionary of metadata for an image

        :param image: Either the ID of an image or a
                       :class:`~ecl.compute.v2.image.Image` or
                       :class:`~ecl.compute.v2.image.ImageDetail`
                       instance.

        :returns: A :class:`~ecl.compute.v2.image.Image` with only the
                  image's metadata. All keys and values are Unicode text.
        :rtype: :class:`~ecl.compute.v2.image.Image`
        """
        res = self._get_base_resource(image, _image.Image)
        metadata = res.get_metadata(self.session)
        result = _image.Image.existing(id=res.id, metadata=metadata)
        return result

    def set_image_metadata(self, image, **metadata):
        """Update metadata for an image

        :param image: Either the ID of an image or a
                       :class:`~ecl.compute.v2.image.Image` or
                       :class:`~ecl.compute.v2.image.ImageDetail`
                       instance.
        :param kwargs metadata: Key/value pairs to be updated in the image's
                                metadata. No other metadata is modified
                                by this call. All keys and values are stored
                                as Unicode.
        :returns: A :class:`~ecl.compute.v2.image.Image` with only the
                  image's metadata. All keys and values are Unicode text.
        """
        res = self._get_base_resource(image, _image.Image)
        metadata = res.set_metadata(self.session, **metadata)
        result = _image.Image.existing(id=res.id, metadata=metadata)
        return result

    def delete_image_metadata(self, image, keys):
        """Delete metadata for an image

        :param image: Either the ID of an image or a
                       :class:`~ecl.compute.v2.image.Image` or
                       :class:`~ecl.compute.v2.image.ImageDetail`
                       instance.
        :param array keys: The keys to delete.
        :rtype: ``None``
        """
        res = self._get_base_resource(image, _image.Image)
        return res.delete_metadata(self.session, keys)

    def create_keypair(self, name=None, public_key=None):
        """Create a new keypair from attributes

        :param string name: The name to associate with the keypair.
        :param string public_key: The public ssh key to import.
            If not provided, a key is generated.
        :returns: :class:`~ecl.compute.v2.keypair.Keypair`
        """
        body = {}
        if name is not None:
            body.update({"name": name})
        if public_key is not None:
            body.update({"public_key": public_key})
        return self._create(_keypair.Keypair, **body)

    def delete_keypair(self, keypair, ignore_missing=False):
        """Delete a keypair

        :param keypair: The value can be either the ID of a keypair or a
                        :class:`~ecl.compute.v2.keypair.Keypair`
                        instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the keypair does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent keypair.
        :returns: ``None``
        """
        self._delete(_keypair.Keypair, keypair, ignore_missing=ignore_missing)

    def get_keypair(self, keypair):
        """Get a single keypair

        :param keypair: The value can be the ID of a keypair or a
                        :class:`~ecl.compute.v2.keypair.Keypair`
                        instance.

        :returns: :class:`~ecl.compute.v2.keypair.Keypair`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_keypair.Keypair, keypair)

    def find_keypair(self, name_or_id, ignore_missing=False):
        """Find a single keypair

        :param string name_or_id: The name or ID of a keypair.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: :class:`~ecl.compute.v2.keypair.Keypair` or None
        """
        return self._find(_keypair.Keypair, name_or_id,
                          ignore_missing=ignore_missing)

    def keypairs(self):
        """Return a list of keypairs

        :returns: A list of keypair objects
        :rtype: :class:`~ecl.compute.v2.keypair.Keypair`
        """
        return list(self._list(_keypair.Keypair, paginated=False))

    def get_limits(self):
        """Retrieve limits that are applied to the project's account

        :returns: A Limits object, including both
                  :class:`~ecl.compute.v2.limits.AbsoluteLimits` and
                  :class:`~ecl.compute.v2.limits.RateLimits`
        :rtype: :class:`~ecl.compute.v2.limits.Limits`
        """
        return self._get(limits.Limits)

    def availability_zones(self, details=False):
        """Return a list of availability zones

        :param bool details: Return extra details about the availability
            zones. This defaults to `False` as it generally
            requires extra permission.
        :returns: A list of :class:`~ecl.compute.v2.availability_zone.AvailabilityZone`
        """
        if details:
            az = _availability_zone.AvailabilityZoneDetail
        else:
            az = _availability_zone.AvailabilityZone
        return list(self._list(az, paginated=False))

    def find_availability_zone(self, name_or_id, ignore_missing=False):
        """Find a single availability_zone

        :param string name_or_id: The name or ID of a availability_zone.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: :class:`~ecl.compute.v2.availability_zone.AvailabilityZone` or None
        """
        return self._find(_availability_zone.AvailabilityZone, name_or_id,
                          ignore_missing=ignore_missing)

    def get_quota(self, tenant_id):
        """Get quota info of a tenant

        :param tenant_id: The ID for the tenant for which you want to show
                        quotas. This ID is different from the tenant ID of authentication.
                        That ID is for the admin tenant.

        :returns: :class:`~ecl.compute.v2.quota.Quota`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_quota.Quota, tenant_id)

    def get_default_quota(self, tenant_id):
        """Get default quota info of a tenant

        :param string tenant_id: The ID for the tenant for which you want to show
                        quotas. This ID is different from the tenant ID of authentication.
                        That ID is for the admin tenant.
        :returns: :class:`~ecl.compute.v2.quota.DefaultQuota`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_quota.DefaultQuota, tenant_id=tenant_id)

    def get_tenant_usage(self, tenant_id):
        """Get tenant usage information of a tenant

        :param string tenant_id: The ID for the tenant for which you want to show
                        usage information. This ID is different from the tenant ID of authentication.
                        That ID is for the admin tenant.

        :returns: :class:`~ecl.compute.v2.quota.TenantUsage`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_quota.TenantUsage, tenant_id)

    def volumes(self, details=True):
        """Return a list of volumes

        :param bool details: Return extra details about the volumes
                             This defaults to `False` as it generally
                             requires extra permission.
        :returns: A list of :class:`~ecl.compute.v2.volume.Volume`
        """
        if details:
            vol = _volume.Volume
        else:
            vol = _volume.VolumeDetail

        return list(self._list(vol, paginated=False))

    def get_volume(self, volume):
        """Get a single volume

        :param volume: The value can be the ID of a volume or a
                       :class:`~ecl.compute.v2.volume.Volume` instance.

        :returns: :class:`~ecl.compute.v2.volume.Volume`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_volume.Volume, volume)

    def create_volume(self, size, name=None, description=None,
                      volume_type=None, metadata=None, availability_zone=None,
                      snapshot_id=None):
        """Create a single volume

        :param size: size of volume to create.
        :param name: display name of volume to create.
        :param description: display description of volume to create.
        :param volume_type: volume type of volume to create.
        :param metadata: size of metadata to create.
        :param availability_zone: availability zone of volume to create.
        :param snapshot_id: ID of snapshot to create from.
        :returns: :class:`~ecl.compute.v2.volume.Volume`
        """
        body = {"size": size}
        if name:
            body.update({"name": name})
        if description:
            body.update({"description": description})
        if volume_type:
            body.update({"volume_type": volume_type})
        if metadata:
            body.update({"metadata": metadata})
        if availability_zone:
            body.update({"availability_zone": availability_zone})
        if snapshot_id:
            body.update({"snapshot_id": snapshot_id})
        return self._create(_volume.Volume, **body)

    def delete_volume(self, volume, ignore_missing=False):
        """Delete an volume

        :param volume: The value can be either the ID of an volume or a
                      :class:`~ecl.compute.v2.volume.Volume` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the volume does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent volume.
        :returns: ``None``
        """
        self._delete(_volume.Volume, volume, ignore_missing=ignore_missing)
