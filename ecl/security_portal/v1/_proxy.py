# -*- coding: utf-8 -*-

from ecl.security_portal.v1 import security_device as _sd
from ecl.security_portal.v1 import security_device_interface as _sdi
from ecl import proxy2


class Proxy(proxy2.BaseProxy):
    def security_devices(self):
        """Listing security devices associated with specific tenant.

        :return: List security devices.
        :rtype: :class:`~ecl.security_portal.v1.security_device.SecurityDevice`
        """
        return list(self._list(_sd.SecurityDevice, paginated=False,
                               tenantid=self.session.get_project_id(),
                               usertoken=self.session.get_token()))

    def get_security_device(self, server_id):
        """Show security device details associated with specific tenant.

        :param string server_id: Server ID registered in Openstack(UUID).
        :return: One security device.
        :rtype: :class:`~ecl.security_portal.v1.security_device.SecurityDevice`
        """
        sd = _sd.SecurityDevice()
        return sd.get(self.session, server_id)

    def security_device_interfaces(self, server_id):
        """Listing security device Interfaces associated with specific tenant.

        :param string server_id: Server ID registered in Openstack(UUID).
        :return: List security device interfaces.
        :rtype: :class:`~ecl.security_portal.v1.security_device_interface.SecurityDeviceInterface`
        """
        return list(self._list(_sdi.SecurityDeviceInterface, paginated=False,
                               server_id=server_id,
                               tenantid=self.session.get_project_id(),
                               usertoken=self.session.get_token()))

    def get_security_device_interface(self, port_id):
        """Show security device Interface associated with specific tenant.

        :param string port_id: Port ID registered in Openstack(UUID).
        :return: One security device interface.
        :rtype: :class:`~ecl.security_portal.v1.security_device_interface.SecurityDeviceInterface`
        """
        sdi = _sdi.SecurityDeviceInterface()
        return sdi.get(self.session, port_id)
