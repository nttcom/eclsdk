# -*- coding: utf-8 -*-

from ecl.security_portal import security_portal_service
from ecl import resource2
from ecl import exceptions
from ecl import utils


class SecurityDevice(resource2.Resource):
    resource_key = "device"
    resources_key = "devices"
    base_path = '/ecl-api/devices'
    service = security_portal_service.SecurityPortalService()

    _query_mapping = resource2.QueryParameters(
        "tenantid",
        "usertoken",
    )

    # Capabilities
    allow_get = True
    allow_list = True

    # Properties
    #: MSA Device External reference.
    msa_device_id = resource2.Body('msa_device_id', alternate_id=True)
    #: MSA Device Type.
    msa_device_type = resource2.Body('msa_device_type')
    #: Server id of Network-based Security devices.
    os_server_id = resource2.Body('os_server_id')
    #: Server name on Openstack.
    os_server_name = resource2.Body('os_server_name')
    #: Availability zone information.
    os_availability_zone = resource2.Body('os_availability_zone')
    #: Name of admin.
    os_admin_username = resource2.Body('os_admin_username')
    #: Server Status.
    os_server_status = resource2.Body('os_server_status')
    #: Interfaces details associated with the Security Device.
    interfaces = resource2.Body('interfaces')

    def get(self, session, server_id):
        uri = self.base_path + '/%s?tenantid=%s&usertoken=%s' \
              % (server_id, session.get_project_id(), session.get_token())
        resp = session.get(uri, endpoint_filter=self.service)
        self._translate_response(resp, has_body=True)
        return self
