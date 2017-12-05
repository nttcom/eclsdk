# -*- coding: utf-8 -*-

from ecl.virtual_network_appliance import virtual_network_appliance_service
from ecl import resource2
from ecl import utils


class VirtualNetworkAppliance(resource2.Resource):
    resources_key = "virtual_network_appliances"
    resource_key = "virtual_network_appliance"
    service = virtual_network_appliance_service.\
        VirtualNetworkApplianceService("v1.0")
    base_path = '/' + service.version + '/virtual_network_appliances'

    # Capabilities
    allow_list = True
    allow_get = True
    allow_create = True
    allow_update = True
    allow_delete = True

    # _query_mapping = resource2.QueryParameters()
    # TBD

    # Properties
    #: It identifies connection resource uniquely.
    id = resource2.Body('id')
    #: Name of network appliance.
    name = resource2.Body('name')
    #: Description of network appliance.
    description = resource2.Body('description')
    #: Appliance type of network appliance.
    appliance_type = resource2.Body('appliance_type')
    #: Zone of network appliance.
    availability_zone = resource2.Body('availability_zone')
    #: OS monitoring status of network appliance.
    os_monitoring_status = resource2.Body('os_monitoring_status')
    #: OS login status of network appliance.
    os_login_status = resource2.Body('os_login_status')
    #: OS login status of network appliance.
    os_login_status = resource2.Body('os_login_status')
    #: VM status of network appliance.
    vm_status = resource2.Body('vm_status')
    #: Operation status of network appliance.
    operation_status = resource2.Body('operation_status')
    #: Plan ID of network appliance.
    virtual_network_appliance_plan_id = \
        resource2.Body('virtual_network_appliance_plan_id')
    #: Tenant ID of the owner.
    tenant_id = resource2.Body('tenant_id')
    #: Interface definition of network appliance
    interfaces = resource2.Body('interfaces')

    def _action(self, session, body, postfix='action'):
        """Preform network appliance actions given the message body."""
        url = utils.urljoin(VirtualNetworkAppliance.base_path,
                            self.id, postfix)
        headers = {'Accept': ''}
        return session.post(
            url, endpoint_filter=self.service, json=body, headers=headers)

    def start(self, session):
        """Start network appliance."""
        body = {"os-start": None}
        return self._action(session, body)

    def stop(self, session):
        """Stop network appliance."""
        body = {"os-stop": None}
        return self._action(session, body)

    def reboot(self, session, reboot_type):
        """Reboot network appliance."""
        body = {'reboot': None}
        self._action(session, body)

    def reset_password(self, session, username):
        """Reset network appliance password."""
        body = {'username': username}
        self._action(session, body, postfix='reset_password')

    def get_console(self, session, vnc_type):
        """Get console of network appliance."""
        action = {'type': vnc_type}
        body = {'os-getVNCConsole': action}
        resp = self._action(session, body, postfix='remote-console')
        if resp:
            console_dict = resp.json()
            if console_dict:
                return console_dict.get("console")
