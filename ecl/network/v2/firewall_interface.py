# -*- coding: utf-8 -*-

from . import base
from ecl.network import network_service
from ecl import resource2
from ecl import utils


class FirewallInterface(base.NetworkBaseResource):
    resource_key = "firewall_interface"
    resources_key = "firewall_interfaces"
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + "/firewall_interfaces"

    _query_mapping = resource2.QueryParameters(
        "description", "firewall_id", "id",
        "ip_address", "name", "network_id",
        "slot_number", "status", "tenant_id",
        "virtual_ip_address", "sort_key", "sort_dir",
    )

    # Capabilities
    allow_get = True
    allow_list = True
    allow_update = True

    # Properties
    #: Description the Firewall Interface.
    description = resource2.Body("description")
    #: The ID of firewall this firewall_interface belongs to.
    firewall_id = resource2.Body("firewall_id")
    #: Unique ID of the Firewall Interface.
    id = resource2.Body("id")
    #: IP Address.
    ip_address = resource2.Body("ip_address")
    #: Name the Firewall Interface.
    name = resource2.Body("name")
    #: Network ID.
    network_id = resource2.Body("network_id")
    #: Slot Number.
    slot_number = resource2.Body("slot_number")
    #: Firewall interface status.
    status = resource2.Body("status")
    #: Tenant ID of the owner (UUID).
    tenant_id = resource2.Body("tenant_id")
    #: Virtual IP Address.
    virtual_ip_address = resource2.Body("virtual_ip_address")
    #: Properties used for virtual IP address.
    virtual_ip_properties = resource2.Body("virtual_ip_properties")

    #: VRID of Firewall virtual ip properties
    @property
    def vrid(self):
        virtual_ip_properties = self._body['virtual_ip_properties']
        if virtual_ip_properties is None:
            return
        else:
            return virtual_ip_properties['vrid']

    def update(self, session, firewall_id, firewall_interface_id, **attrs):
        """Update a firewall interface."""
        update_path = '/' + self.service.version
        uri = utils.urljoin(update_path, 'firewalls', firewall_id,
                            'firewall_interfaces', firewall_interface_id)
        resp = session.put(
            uri, endpoint_filter=self.service,
            json=attrs
        )
        self._translate_response(resp, has_body=True)
        return self
