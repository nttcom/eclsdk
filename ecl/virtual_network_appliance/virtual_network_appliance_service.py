# -*- coding: utf-8 -*-

from ecl import service_filter


class VirtualNetworkApplianceService(service_filter.ServiceFilter):
    """The virtual network appliance service."""

    valid_versions = [service_filter.ValidVersion('v1')]

    def __init__(self, version=None):
        """Create a virtual network appliance service."""
        super(VirtualNetworkApplianceService, self).__init__(
            service_type='virtual-network-appliance',
            version=version
        )
