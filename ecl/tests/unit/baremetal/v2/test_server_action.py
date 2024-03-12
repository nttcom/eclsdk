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

import testtools

from ecl.baremetal.v2 import server

EXAMPLE = {
    "flavor_name": "General Purpose 2",
    "flavor_id": "fcec5541-81c3-4963-ba6f-dc24773ebf7f",
    "updated": "2012-09-07T16:56:37Z",
    "status": "SUCCESS",
    "message": "",
    "setting": {
        "hoge": {
            "value": "Enabled",
            "default": "Enabled",
            "type": "enum",
            "selection": ["Enabled", "Disabled"]
        },
        "fuga": {
            "value": "Disabled",
            "default": "Enabled",
            "type": "enum",
            "selection": ["Enabled", "Disabled"]
        }
    }
}


class TestSERVER(testtools.TestCase):

    def test_basic(self):
        sot = server.SERVER()
        self.assertEqual('server', sot.resource_key)
        self.assertEqual('server', sot.resources_key)
        self.assertEqual('/servers/%(server_id)s/server', sot.base_path)
        self.assertEqual('baremetal-server', sot.service.service_type)
        self.assertFalse(sot.allow_create)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_update)
        self.assertFalse(sot.allow_delete)
        self.assertFalse(sot.allow_list)

    def test_make_it(self):
        sot = server.SERVER(**EXAMPLE)
        self.assertEqual(EXAMPLE['id'], sot.id)
        self.assertEqual(EXAMPLE['links'], sot.links)
        self.assertEqual(EXAMPLE['name'], sot.name)
        self.assertEqual(EXAMPLE['adminPass'], sot.adminPass)
        self.assertEqual(EXAMPLE['key_name'], sot.key_name)
        self.assertEqual(EXAMPLE['setting'], sot.setting)


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
