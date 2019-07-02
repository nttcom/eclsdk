# -*- coding: utf-8 -*-

from . import base

from ecl.virtual_network_appliance import virtual_network_appliance_service
from ecl import resource2
from ecl import utils


class VirtualNetworkAppliance(base.VirtualNetworkApplianceBaseResource):
    resources_key = "virtual_network_appliances"
    resource_key = "virtual_network_appliance"
    service = virtual_network_appliance_service.\
        VirtualNetworkApplianceService("v1.0")
    base_path = '/' + service.version + '/virtual_network_appliances'

    patch_update = True

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
    #: Name of virtual network appliance
    name = resource2.Body('name')
    #: Description of virtual network appliance
    description = resource2.Body('description')
    #: Tags of virtual network appliance
    tags = resource2.Body('tags')
    #: Appliance type of virtual network appliance
    appliance_type = resource2.Body('appliance_type')
    #: Zone of virtual network appliance
    availability_zone = resource2.Body('availability_zone')
    #: Default gateway of virtual network appliance
    default_gateway = resource2.Body('default_gateway')
    #: OS monitoring status of virtual network appliance
    os_monitoring_status = resource2.Body('os_monitoring_status')
    #: OS login status of virtual network appliance
    os_login_status = resource2.Body('os_login_status')
    #: VM status of virtual network appliance
    vm_status = resource2.Body('vm_status')
    #: Operation status of virtual network appliance
    operation_status = resource2.Body('operation_status')
    #: Plan ID of virtual network appliance
    virtual_network_appliance_plan_id = \
        resource2.Body('virtual_network_appliance_plan_id')
    #: Tenant ID of virtual network appliance.
    tenant_id = resource2.Body('tenant_id')
    #: Interface definition of virtual network appliance.
    interfaces = resource2.Body('interfaces')
    #: User name of virtual network appliance.
    username = resource2.Body('username')
    #: Password of virtual network appliance.
    password = resource2.Body('password')
    #: Password(after reset) of virtual network appliance.
    new_password = resource2.Body('new_password')

    def update(self, session, prepend_key=True, has_body=True):
        """Update the remote resource based on this virtual network appliance.

        Reason why override this method manually is,
        virtual network appliance API only allows PATCH method as
        way of updating.

        :param session: The session to use for making this request.
        :type session: :class:`~ecl.session.Session`
        :param prepend_key: A boolean indicating whether the resource_key
            should be prepended in a resource update request.
            Default to True.

        :return: This :class:`Resource` instance.
        :raises: :exc:`~ecl.exceptions.MethodNotSupported` if
                 :data:`Resource.allow_update` is not set to ``True``.
        """
        if not any([self._body.dirty, self._header.dirty]):
            return self

        request = self._prepare_request(prepend_key=prepend_key)

        if 'id' in request.body[self.resource_key]:
            del request.body[self.resource_key]['id']

        response = session.patch(request.uri, endpoint_filter=self.service,
                                 json=request.body,
                                 headers=request.headers)

        self._translate_response(response, has_body=has_body)
        return self

    def _action(self, session, body, postfix='action'):
        """Preform virtual network appliance actions given the message body"""
        url = utils.urljoin(VirtualNetworkAppliance.base_path,
                            self.id, postfix)
        headers = {'Accept': ''}
        return session.post(
            url, endpoint_filter=self.service, json=body, headers=headers)

    def start(self, session):
        """Start virtual network appliance"""
        body = {"os-start": None}
        return self._action(session, body)

    def stop(self, session):
        """Stop virtual network appliance"""
        body = {"os-stop": None}
        return self._action(session, body)

    def restart(self, session):
        """Restart virtual network appliance"""
        body = {'os-restart': None}
        self._action(session, body)

    def reset_password(self, session):
        """Reset virtual network appliance password."""
        body = {}
        resp = self._action(session, body, postfix='reset-password')
        self._translate_response(resp, has_body=True)
        return self

    def get_console(self, session, vnc_type):
        """Get console of virtual network appliance"""
        action = {'type': vnc_type}
        body = {'os-getVNCConsole': action}
        resp = self._action(session, body, postfix='remote-console')
        if resp:
            console_dict = resp.json()
            if console_dict:
                return console_dict.get("console")
