# -*- coding: utf-8 -*-

from . import base
from ecl import utils
from ecl import resource2
from ecl.network import network_service


class LoadBalancerInterface(base.NetworkBaseResource):

    resources_key = "load_balancer_interfaces"
    resource_key = "load_balancer_interface"
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + "/load_balancer_interfaces"

    _query_mapping = resource2.QueryParameters(
        "description", "id", "ip_address", "load_balancer_id",
        "name", "network_id", "slot_number", "status", "tenant_id",
        "virtual_ip_address", "sort_key", "sort_dir",
    )

    # Capabilities
    allow_list = True
    allow_get = True
    allow_update = True

    # Properties
    #: Description of the Load Balancer Interface.
    description = resource2.Body("description")
    #: Unique ID of the Load Balancer Interface.
    id = resource2.Body("id")
    #: IP Address
    ip_address = resource2.Body("ip_address")
    #: The ID of load_balancer this load_balancer_interface belongs to.
    load_balancer_id = resource2.Body("load_balancer_id")
    #: Name of the Load Balancer
    name = resource2.Body("name")
    #: Network
    network_id = resource2.Body("network_id")
    #: Slot Number
    slot_number = resource2.Body("slot_number")
    #: The load_balancer status.
    status = resource2.Body("status")
    #: Tenant ID of the owner (UUID)
    tenant_id = resource2.Body("tenant_id")
    #: Virtual IP Address
    virtual_ip_address = resource2.Body("virtual_ip_address")
    #: Properties used for virtual IP address.
    #: virtual_ip_properties.protocol: Redundancy Protocol.
    #: virtual_ip_properties.vrid: VRRP group identifier.
    virtual_ip_properties = resource2.Body("virtual_ip_properties")

    def update(self, session, load_balancer_id,
               load_balancer_interface_id, **attrs):
        """Update a load balancer interface."""
        update_path = '/' + self.service.version
        uri = utils.urljoin(update_path, 'load_balancers',
                            load_balancer_id,
                            'load_balancer_interfaces',
                            load_balancer_interface_id)
        resp = session.put(
            uri, endpoint_filter=self.service,
            json=attrs
        )
        self._translate_response(resp, has_body=True)
        return self
