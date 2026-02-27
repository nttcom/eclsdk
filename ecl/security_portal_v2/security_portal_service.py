# -*- coding: utf-8 -*-

from ecl import service_filter


class SecurityPortalService(service_filter.ServiceFilter):
    """The security service."""

    valid_versions = [service_filter.ValidVersion('v2')]

    def __init__(self, version=None):
        """Create a security service."""
        super(SecurityPortalService, self).__init__(service_type='security-operation',
                                                    version=version)
