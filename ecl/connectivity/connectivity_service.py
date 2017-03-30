# -*- coding: utf-8 -*-


from ecl import service_filter


class ConnectivityService(service_filter.ServiceFilter):
    """The interconnectivity service."""

    valid_versions = [service_filter.ValidVersion('v1')]

    def __init__(self, version=None):
        """Create a interconnectivity service."""
        super(ConnectivityService, self).__init__(service_type='interconnectivity',
                                                  version=version)
