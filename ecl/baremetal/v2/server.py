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
from ecl import exceptions
from ecl import resource2


class Server(resource2.Resource):
    resources_key = "servers"
    resource_key = "server"
    base_path = '/servers'
    service = baremetal_service.BaremetalService()

    # Capabilities
    allow_get = True
    allow_list = True
    allow_create = True
    allow_delete = True

    # Properties
    #: UUID of the Baremetal server.
    id = resource2.Body('id')
    #: Link of the Baremetal server.
    links = resource2.Body('links')
    #: Name of the Baremetal server.
    name = resource2.Body('name')
    #: Password for the administrator.
    #: This parameter is shown only once, so you have to memo.
    #: Please refer OS specific limitations adminPass raw to know the
    #: required administrator name for each OS.
    adminPass = resource2.Body('adminPass')
    admin_pass = resource2.Body('adminPass')
    #: SSH Keypair name you created on KeyPairs API.
    key_name = resource2.Body('key_name')
    #: Power state: {"RUNNING":"The server is running.",
    #: "SHUTDOWN":"The server was shut down.",
    #: "CRASHED":"The server lost powor controll information temporary.
    #: Status transfer RUNNING/SHUTDOWN Automatically."}
    OS_EXT_STS_power_state = resource2.Body('OS-EXT-STS:power_state')
    power_state = resource2.Body('OS-EXT-STS:power_state')
    #: Task state: {None:"There are no tasks. Only this status can be
    #: received API requests.", "BUILDING":"The task is building the
    #: Baremetal Server. This status is transfered by Create Server.",
    #: "DELETING":"The task is deleting the Baremetal Server. This status
    #: is transfered by Delete Server.", "STOPPING":"The task is stopping
    #: the Baremetal Server. This status is transfered by Stop Server.",
    #: "STARTING":"The task is starting the Baremetal Server. This status
    #: is transfered by Start Server.", "REBOOTING":"The task is rebooting
    #: the Baremetal Server. This status is transfered by Reboot Server."}
    OS_EXT_STS_task_state = resource2.Body('OS-EXT-STS:task_state')
    task_state = resource2.Body('OS-EXT-STS:task_state')
    #: VM state: {"ACTIVE":"The Baremetal server is active.
    #: This status is target of billing.", "BUILD":"The Baremetal server
    #: is built.", "ERROR": "The Baremetal server is outputing a error.
    #: There is necessity to report to our support.", "DELETED":"The
    #: Baremetal server is deleted."}
    OS_EXT_STS_vm_state = resource2.Body('OS-EXT-STS:vm_state')
    vm_state = resource2.Body('OS-EXT-STS:vm_state')
    #: Server's availability zone.
    OS_EXT_AZ_availability_zone = resource2.Body('OS-EXT-AZ:availability_zone')
    availability_zone = resource2.Body('OS-EXT-AZ:availability_zone')
    #: Sever's created time.
    created = resource2.Body('created')
    #: Server's flavor information.
    flavor = resource2.Body('flavor')
    #: Server's host ID.
    hostId = resource2.Body('hostId')
    #: Server's ID.
    image = resource2.Body('image')
    #: Server's image information.
    metadata = resource2.Body('metadata')
    #: Server's links information.
    progress = resource2.Body('progress')
    #: Server's metadata information.
    status = resource2.Body('status')
    #: Server's tenant id.
    tenant_id = resource2.Body('tenant_id')
    #: Server's updated time.
    updated = resource2.Body('updated')
    #: Server's user id.
    user_id = resource2.Body('user_id')
    #: Server's raid arrays information.
    raid_arrays = resource2.Body('raid_arrays')
    #: Server's lvm volume groups information.
    lvm_volume_groups = resource2.Body('lvm_volume_groups')
    #: Server's file system information.
    filesystems = resource2.Body('filesystems')
    #: Server's nic physical ports information.
    nic_physical_ports = resource2.Body('nic_physical_ports')
    #: Server's chassis status information.
    chassis_status = resource2.Body('chassis-status')
    #: managed_by_service
    managed_by_service = resource2.Body('managed_by_service')
    media_attachments = resource2.Body('media_attachments')
    #: key_pair name
    key_name = resource2.Body('key_name')

    def create(self, session, **attrs):
        body = {"server": attrs}
        resp = session.post(
            self.base_path, endpoint_filter=self.service,
            json=body,
            headers={"Accept": "application/json"}
        )
        self._translate_response(resp, has_body=True)
        return self


class ServerDetail(Server):
    base_path = '/servers/detail'

    # capabilities
    allow_create = False
    allow_get = False
    allow_update = False
    allow_delete = False
    allow_list = True



class ServerAction(resource2.Resource):
    resource_key = "console"
    resources_key = None
    base_path = '/servers/%s/action'
    service = baremetal_service.BaremetalService()

    # Properties
    #: Type of the remote console. Valid values are IPMI or IMM.
    type = resource2.Body('type')
    #: URL to access the remote console.
    url = resource2.Body('url')
    #: User ID for sign in to the remote console.
    user_id = resource2.Body('user_id')
    #: Password for sign in to the remote console.
    password = resource2.Body('password')

    def start(self, session, server_id, boot_mode):
        uri = self.base_path % server_id
        body = {"os-start": {"boot_mode": boot_mode}}
        resp = session.post(
            uri,
            endpoint_filter=self.service,
            json=body
        )
        self._translate_response(resp, has_body=False)
        return self

    def stop(self, session, server_id, type):
        uri = self.base_path % server_id
        if type is None:
            body = {"os-stop": None}
        else:
            body = {"os-stop": {"type": type}}
        resp = session.post(
            uri,
            endpoint_filter=self.service,
            json=body
        )
        self._translate_response(resp, has_body=False)
        return self

    def reboot(self, session, server_id, type, boot_mode):
        uri = self.base_path % server_id
        body = {
            "reboot": {
                "type": type,
                "boot_mode": boot_mode,
            }
        }
        resp = session.post(
            uri,
            endpoint_filter=self.service,
            json=body
        )
        self._translate_response(resp, has_body=False)
        return self

    def media_attach(self, session, server_id, image):
        uri = self.base_path % server_id
        body = {
            "media-attach": {
                "imageRef": image
            }
        }
        resp = session.post(
            uri,
            endpoint_filter=self.service,
            json=body
        )
        self._translate_response(resp, has_body=False)
        return self

    def media_detach(self, session, server_id, image):
        uri = self.base_path % server_id
        body = {
            "media-detach": {
                "imageRef": image
            }
        }
        resp = session.post(
            uri,
            endpoint_filter=self.service,
            json=body
        )
        self._translate_response(resp, has_body=False)
        return self

    def get_management_console(self, session, server_id):
        uri = self.base_path % server_id
        body = {
            "os-getManagementConsole": None
        }
        resp = session.post(
            uri,
            endpoint_filter=self.service,
            json=body,
            headers={"Accept": "application/json"}
        )
        self._translate_response(resp, has_body=True)
        return self

    @classmethod
    def find(cls, session, name_or_id, ignore_missing=False, **params):
        """Find a resource by its name or id.

        :param session: The session to use for making this request.
        :type session: :class:`~ecl.session.Session`
        :param name_or_id: This resource's identifier, if needed by
                           the request. The default is ``None``.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :param dict params: Any additional parameters to be passed into
                            underlying methods, such as to
                            :meth:`~ecl.resource2.Resource.existing`
                            in order to pass on URI parameters.

        :return: The :class:`Resource` object matching the given name or id
                 or None if nothing matches.
        :raises: :class:`ecl.exceptions.DuplicateResource` if more
                 than one resource is found for this request.
        :raises: :class:`ecl.exceptions.ResourceNotFound` if nothing
                 is found and ignore_missing is ``False``.
        """
        # Try to short-circuit by looking directly for a matching ID.

        data = cls.list(session, **params)

        result = cls._get_one_match(name_or_id, data)
        if result is not None:
            return result

        if ignore_missing:
            return None
        raise exceptions.ResourceNotFound(
            "No %s found for %s" % (cls.__name__, name_or_id))
