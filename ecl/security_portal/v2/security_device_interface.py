# -*- coding: utf-8 -*-

from ecl.security_portal import security_portal_service
from ecl import resource2
from ecl import exceptions
from ecl import utils


class SecurityDeviceInterface(resource2.Resource):
    resource_key = "device_interface"
    resources_key = "device_interfaces"
    base_path = '/ecl-api/devices/%(server_id)s/interfaces'
    service = security_portal_service.SecurityPortalService()

    _query_mapping = resource2.QueryParameters(
        "tenantid",
        "usertoken",
    )

    # Capabilities
    allow_get = True
    allow_list = True

    # Properties
    #: Port id on Openstack.
    os_port_id = resource2.Body('os_port_id', alternate_id=True)
    #: Port IP address (if available).
    os_ip_address = resource2.Body('os_ip_address')
    #: Port id on the Network-based Security devices (registered in MSA).
    msa_port_id = resource2.Body('msa_port_id')
    #: Port name on Openstack.
    os_port_name = resource2.Body('os_port_name')
    #: Network Id to which Port is associated on Openstack.
    os_network_id = resource2.Body('os_network_id')
    #: Port Status on Openstack.
    os_port_status = resource2.Body('os_port_status')
    #: Port MAC address on Openstack.
    os_mac_address = resource2.Body('os_mac_address')
    #: Subnet Id to which Port is associated on Openstack.
    os_subnet_id = resource2.Body('os_subnet_id')
    #: Server id of Network-based Security devices.
    os_server_id = resource2.Body('os_server_id')

    def get(self, session, port_id):
        uri = '/ecl-api/devices/interface/%s?tenantid=%s&usertoken=%s' \
              % (port_id, session.get_project_id(), session.get_token())
        resp = session.get(uri, endpoint_filter=self.service)
        self._translate_response(resp, has_body=True)
        return self
