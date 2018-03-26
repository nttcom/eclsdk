# -*- coding: utf-8 -*-

from ecl import service_filter


class ProviderConnectivityService(service_filter.ServiceFilter):
    """The provider connectivity service."""

    valid_versions = [
        service_filter.ValidVersion('v1'),
        service_filter.ValidVersion('v2'),
    ]

    def __init__(self, version=None):
        """Create a provider connectivity service."""
        super(ProviderConnectivityService, self).__init__(
            service_type='provider-connectivity',
            version=version
        )
