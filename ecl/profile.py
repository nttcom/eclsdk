# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""
:class:`~ecl.profile.Profile` is the class that is used to
define the various preferences for different services.  The preferences that
are currently supported are service name, region, version and interface.
The :class:`~ecl.profile.Profile` and the
:class:`~ecl.connection.Connection` classes are the most important
user facing classes.

Examples
--------


The :class:`~ecl.profile.Profile` class is constructed
with no arguments.

Set Methods
~~~~~~~~~~~

A user's preferences are set based on the service type.  Service type would
normally be something like 'compute', 'identity', 'object-store', etc.::

    from ecl import profile
    prof = profile.Profile()
    prof.set_name('compute', 'matrix')
    prof.set_region(prof.ALL, 'zion')
    prof.set_version('identity', 'v3')
    prof.set_interface('object-store', 'internal')
    for service in prof.get_services():
        print(prof.get_filter(service.service_type)

The resulting preference print out would look something like::

    service_type=compute,region=zion,service_name=matrix
    service_type=network,region=zion
    service_type=database,region=zion
    service_type=image,region=zion
    service_type=metering,region=zion
    service_type=orchestration,region=zion
    service_type=object-store,interface=internal,region=zion
    service_type=identity,region=zion,version=v3
"""

import copy
import logging
import six

from ecl.baremetal import baremetal_service
from ecl.block_store import block_store_service
from ecl.compute import compute_service
from ecl.connectivity import connectivity_service
from ecl.dedicated_hypervisor import dedicated_hypervisor_service
from ecl import exceptions
from ecl.identity import identity_service
from ecl.image import image_service
from ecl import module_loader
from ecl.network import network_service
from ecl.object_store import object_store_service
from ecl.orchestration import orchestration_service
from ecl.provider_connectivity import provider_connectivity_service
from ecl.rca import rca_service
from ecl.storage import storage_service
from ecl.security_order import security_order_service
from ecl.security_portal import security_portal_service
from ecl.sss import sss_service
from ecl.telemetry import telemetry_service
from ecl.database import database_service
from ecl.dns import dns_service
from ecl.virtual_network_appliance import virtual_network_appliance_service


_logger = logging.getLogger(__name__)
_logger.addHandler(logging.StreamHandler())


class Profile(object):

    ALL = "*"
    """Wildcard service identifier representing all services."""

    def __init__(self, plugins=None):
        """User preference for each service.

        :param list plugins: List of entry point namespaces to load.

        Create a new :class:`~ecl.profile.Profile`
        object with no preferences defined, but knowledge of the services.
        Services are identified by their service type, e.g.: 'identity',
        'compute', etc.
        """
        self._services = {}
        self._add_service(compute_service.ComputeService(version="v2"))
        self._add_service(
            connectivity_service.ConnectivityService(version="v1"))
        self._add_service(identity_service.IdentityService(version="v3"))
        self._add_service(image_service.ImageService(version="v2"))
        self._add_service(network_service.NetworkService(version="v2"))
        self._add_service(sss_service.SssService(version="v1"))
        self._add_service(
            object_store_service.ObjectStoreService(version="v1"))
        self._add_service(
            orchestration_service.OrchestrationService(version="v1"))
        self._add_service(
            provider_connectivity_service.ProviderConnectivityService(
                version="v2"))
        self._add_service(telemetry_service.TelemetryService(version="v2"))
        self._add_service(block_store_service.BlockStoreService(version="v2"))
        self._add_service(storage_service.StorageService(version="v1"))
        self._add_service(
            security_order_service.SecurityOrderService(version="v1"))
        self._add_service(
            security_portal_service.SecurityPortalService(version="v1"))
        self._add_service(rca_service.RcaService(version="v1"))
        self._add_service(baremetal_service.BaremetalService(version="v2"))
        self._add_service(
            dedicated_hypervisor_service.DedicatedHypervisorService(
                version="v1"))
        self._add_service(database_service.DatabaseService(version="v1"))
        self._add_service(dns_service.DnsService(version="v2"))
        self._add_service(
            virtual_network_appliance_service.VirtualNetworkApplianceService(
                version="v1"))

        # NOTE: The Metric service is not added here as it currently
        # only retrieves the /capabilities API.

        if plugins:
            for plugin in plugins:
                self._load_plugin(plugin)
        self.service_keys = sorted(self._services.keys())

    def __repr__(self):
        return repr(self._services)

    def _add_service(self, serv):
        serv.interface = None
        self._services[serv.service_type] = serv

    def _load_plugin(self, namespace):
        """Load a service plugin.

        :param str namespace: Entry point namespace
        """
        services = module_loader.load_service_plugins(namespace)
        for service_type in services:
            if service_type in self._services:
                _logger.debug("Overriding %s with %s", service_type,
                              services[service_type])
            self._add_service(services[service_type])

    def get_filter(self, service):
        """Get a service preference.

        :param str service: Desired service type.
        """
        return copy.copy(self._get_filter(service))

    def _get_filter(self, service):
        """Get a service preference.

        :param str service: Desired service type.
        """
        serv = self._services.get(service, None)
        if serv is not None:
            return serv
        msg = ("Service %s not in list of valid services: %s" %
               (service, self.service_keys))
        raise exceptions.SDKException(msg)

    def _get_services(self, service):
        return self.service_keys if service == self.ALL else [service]

    def _setter(self, service, attr, value):
        for service in self._get_services(service):
            setattr(self._get_filter(service), attr, value)

    def get_services(self):
        """Get a list of all the known services."""
        services = []
        for name, service in six.iteritems(self._services):
            services.append(service)
        return services

    def set_name(self, service, name):
        """Set the desired name for the specified service.

        :param str service: Service type.
        :param str name: Desired service name.
        """
        self._setter(service, "service_name", name)

    def set_region(self, service, region):
        """Set the desired region for the specified service.

        :param str service: Service type.
        :param str region: Desired service region.
        """
        self._setter(service, "region", region)

    def set_version(self, service, version):
        """Set the desired version for the specified service.

        :param str service: Service type.
        :param str version: Desired service version.
        """
        self._get_filter(service).version = version

    def set_api_version(self, service, api_version):
        """Set the desired API micro-version for the specified service.

        :param str service: Service type.
        :param str api_version: Desired service API micro-version.
        """
        self._setter(service, "api_version", api_version)

    def set_interface(self, service, interface):
        """Set the desired interface for the specified service.

        :param str service: Service type.
        :param str interface: Desired service interface.
        """
        self._setter(service, "interface", interface)
