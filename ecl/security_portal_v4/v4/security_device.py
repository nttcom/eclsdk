# -*- coding: utf-8 -*-

from ecl.security_portal_v4 import security_portal_service
from ecl import resource2
from ecl import exceptions
from ecl import utils


class SecurityDevice(resource2.Resource):
    resource_key = "device"
    resources_key = "devices"
    base_path = '/ecl-api/v4/devices'
    service = security_portal_service.SecurityPortalService()

    _query_mapping = resource2.QueryParameters(
        "tenant_id",
    )

    # Capabilities
    allow_get = True
    allow_list = True

    # Properties
    #: MSA Device External reference.
    device_id = resource2.Body('device_id', alternate_id=True)
    #: MSA Device Type.
    device_type = resource2.Body('device_type')
    #: Server id of Network-based Security devices.
    os_server_id = resource2.Body('os_server_id')
    #: Server name on Openstack.
    os_server_name = resource2.Body('os_server_name')
    #: Availability zone information.
    os_availability_zone = resource2.Body('os_availability_zone')
    #: Server Status.
    os_server_status = resource2.Body('os_server_status')
    #: Interfaces details associated with the Security Device.
    interfaces = resource2.Body('interfaces')

    def get(self, session, server_id):
        uri = self.base_path + '/%s?tenant_id=%s' \
              % (server_id, session.get_project_id())
        resp = session.get(uri, endpoint_filter=self.service)
        self._translate_get_response(resp, has_body=True)
        return self

    def _translate_get_response(self, response, has_body=True):
        if has_body:
            body = response.json()
            # "device_id" is returned as a sibling of "device", not nested
            # inside it, so it must be merged in before the resource_key
            # ("device") is unwrapped.
            device_id = body.get('device_id')
            if self.resource_key and self.resource_key in body:
                body = body[self.resource_key]
            if device_id is not None:
                body['device_id'] = device_id

            body = self._filter_component(body, self._body_mapping())
            self._body.attributes.update(body)
            self._body.clean()

        headers = self._filter_component(response.headers,self._header_mapping())
        self._header.attributes.update(headers)
        self._header.clean()
