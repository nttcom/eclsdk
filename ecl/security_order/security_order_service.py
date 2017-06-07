# -*- coding: utf-8 -*-

from ecl import service_filter


class SecurityOrderService(service_filter.ServiceFilter):
    """The security service."""

    valid_versions = [service_filter.ValidVersion('v1')]

    def __init__(self, version=None):
        """Create a security service."""
        super(SecurityOrderService, self).__init__(service_type='mss-rfg',
                                                   version=version)
