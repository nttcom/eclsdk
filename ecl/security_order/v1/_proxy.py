# -*- coding: utf-8 -*-

from ecl.security_order.v1 import device as _fgs
from ecl.security_order.v1 import ha_device as _fgha
from ecl.security_order.v1 import waf as _fgwaf
from ecl.security_order.v1 import host_based_security as _hbs
from ecl import proxy2


class Proxy(proxy2.BaseProxy):

    def devices(self, locale=None):
        """List Managed Firwall/UTM devices of single constitution.

        :param string locale: Messages are displayed in Japanese or English
                              depending on this value.
                              ja: Japanese, en: English. Default value is "en".
        :return: Single Firwall/UTM.
        :rtype: :class:`~ecl.security.v1.device.Device`
        """
        fgs = _fgs.Device()
        return fgs.list(self.session, locale=locale)

    def create_device(self, operatingmode, licensekind,
                               azgroup, locale=None):
        """Create a new Managed Firewall/UTM device of single constitution.

        :param string operatingmode: Set "FW" or "UTM" to this value.
        :param string licensekind: Set "02" or "08" as FW/UTM plan.
        :param string azgroup: Availability Zone
        :param string locale: Messages are displayed in Japanese or English
                              depending on this value.
                              ja: Japanese, en: English. Default value is "en".
        :return: Single Firwall/UTM.
        :rtype: :class:`~ecl.security.v1.device.Device`
        """
        body = {}
        body["tenant_id"] = self.session.get_project_id()
        body["gt_host"] = [{
            "operatingmode": operatingmode,
            "licensekind": licensekind,
            "azgroup": azgroup
        }]
        body["sokind"] = "A"
        if locale:
            body["locale"] = locale
        return self._create(_fgs.Device, **body)

    def update_device(self, hostname, operatingmode,
                               licensekind, locale=None):
        """Change menu (Firewall/Managed UTM) and/or plan of single device.

        :param string operatingmode: Set "FW" or "UTM" to this value.
        :param string licensekind: Set "02" or "08" as FW/UTM plan.
        :param string hostname: Set the hostname.
        :param string locale: Messages are displayed in Japanese or English
                              depending on this value.
                              ja: Japanese, en: English. Default value is "en".
        :return: Single Firwall/UTM.
        :rtype: :class:`~ecl.security.v1.device.Device`
        """
        body = {}
        body["tenant_id"] = self.session.get_project_id()
        body["gt_host"] = [{
            "hostname": hostname,
            "operatingmode": operatingmode,
            "licensekind": licensekind
        }]
        body["sokind"] = "M"
        if locale:
            body.update({"locale": locale})
        fgs = _fgs.Device()
        return fgs.update(self.session, **body)

    def delete_device(self, hostname, locale=None):
        """Delete a Managed Firewall/UTM device of single constitution.

        :param string hostname: Set the hostname.
        :param string locale: Messages are displayed in Japanese or English
                              depending on this value.
                              ja: Japanese, en: English. Default value is "en".
        :return: Single Firwall/UTM.
        :rtype: :class:`~ecl.security.v1.device.Device`
        """
        body = {}
        body["tenant_id"] = self.session.get_project_id()
        body["gt_host"] = [{
            "hostname": hostname
        }]
        body["sokind"] = "D"
        if locale:
            body["locale"] = locale
        fgs = _fgs.Device()
        return fgs.delete(self.session, body, locale=locale)

    def ha_devices(self, locale=None):
        """List Managed Firwall/UTM devices of single constitution.

        :param string locale: Messages are displayed in Japanese or English
                              depending on this value.
                              ja: Japanese, en: English. Default value is "en".
        :return: HA Firwall/UTM.
        :rtype: :class:`~ecl.security.v1.ha_device.HADevice`
        """
        fgha = _fgha.HADevice()
        return fgha.list(self.session, locale=locale)

    def create_ha_device(self, operatingmode, licensekind,
                           azgroup1, azgroup2,
                           halink1networkid, halink1subnetid,
                           halink1ipaddress1, halink1ipaddress2,
                           halink2networkid, halink2subnetid,
                           halink2ipaddress1, halink2ipaddress2,
                           locale=None):
        """Create a new Managed Firewall/UTM device of single constitution.

        :param string operatingmode: Set "UTM_HA" or "FW_HA" to this value.
        :param string licensekind: Set "02" or "08" as FW/UTM plan.
        :param string azgroup1: Availability Zone
        :param string azgroup2: Availability Zone
        :param string halink1networkid: Set Network ID to be used for HA line.
        :param string halink1subnetid: Set Subnet ID to be used for HA line.
        :param string halink1ipaddress1: Set value of IPv4.
        :param string halink1ipaddress2: Set value of IPv4.
        :param string halink2networkid: Set Network ID to be used for HA line.
        :param string halink2subnetid: Set Subnet ID to be used for HA line.
        :param string halink2ipaddress1: Set value of IPv4.
        :param string halink2ipaddress2: Set value of IPv4.
        :param string locale: Messages are displayed in Japanese or English
                              depending on this value.
                              ja: Japanese, en: English. Default value is "en".
        :return: HA Firwall/UTM.
        :rtype: :class:`~ecl.security.v1.ha_device.HADevice`
        """
        body = {}
        body["tenant_id"] = self.session.get_project_id()
        body["gt_host"] = [{
            "operatingmode": operatingmode,
            "licensekind": licensekind,
            "azgroup": azgroup1,
            "halink1networkid": halink1networkid,
            "halink1subnetid": halink1subnetid,
            "halink1ipaddress": halink1ipaddress1,
            "halink2networkid": halink2networkid,
            "halink2subnetid": halink2subnetid,
            "halink2ipaddress": halink2ipaddress1
        },{
            "operatingmode": operatingmode,
            "licensekind": licensekind,
            "azgroup": azgroup2,
            "halink1networkid": halink1networkid,
            "halink1subnetid": halink1subnetid,
            "halink1ipaddress": halink1ipaddress2,
            "halink2networkid": halink2networkid,
            "halink2subnetid": halink2subnetid,
            "halink2ipaddress": halink2ipaddress2
        }]
        body["sokind"] = "AH"
        if locale:
            body["locale"] = locale
        return self._create(_fgha.HADevice, **body)

    def update_ha_device(self, hostname1, hostname2, operatingmode,
                           licensekind, locale=None):
        """Change menu (Firewall/Managed UTM) and/or plan of single device.

        :param string hostname1: Set the hostname.
        :param string hostname2: Set the hostname.
        :param string operatingmode: Set "UTM_HA" or "FW_HA" to this value.
        :param string licensekind: Set "02" or "08" as FW/UTM plan.
        :param string locale: Messages are displayed in Japanese or English
                              depending on this value.
                              ja: Japanese, en: English. Default value is "en".
        :return: HA Firwall/UTM.
        :rtype: :class:`~ecl.security.v1.ha_device.HADevice`
        """
        body = {}
        body["tenant_id"] = self.session.get_project_id()
        body["gt_host"] = [{
            "hostname": hostname1,
            "operatingmode": operatingmode,
            "licensekind": licensekind
        },{
            "hostname": hostname2,
            "operatingmode": operatingmode,
            "licensekind": licensekind
        }]
        body["sokind"] = "MH"
        if locale:
            body.update({"locale": locale})
        fgha = _fgha.HADevice()
        return fgha.update(self.session, **body)

    def delete_ha_device(self, hostname1, hostname2, locale=None):
        """Delete a Managed Firewall/UTM device of single constitution.

        :param string hostname1: Set the hostname.
        :param string hostname2: Set the hostname.
        :param string locale: Messages are displayed in Japanese or English
                              depending on this value.
                              ja: Japanese, en: English. Default value is "en".
        :return: HA Firwall/UTM.
        :rtype: :class:`~ecl.security.v1.ha_device.HADevice`
        """
        body = {}
        body["tenant_id"] = self.session.get_project_id()
        body["gt_host"] = [{
            "hostname": hostname1
        }, {
            "hostname": hostname2
        }]
        body["sokind"] = "DH"
        if locale:
            body["locale"] = locale
        fgha = _fgha.HADevice()
        return fgha.delete(self.session, body, locale=locale)

    def get_device_order_status(self, soid, locale=None):
        """Check progress status of Managed Firewall/UTM device Service Order.

        :param string soid: This value is returned value of when you execute
                            Create Server, Update Server or Delete Server API.
        :param string locale: Messages are displayed in Japanese or English
                              depending on this value.
                              ja: Japanese, en: English. Default value is "en".
        :return: Single Firwall/UTM.
        :rtype: :class:`~ecl.security.v1.device.Device`
        """
        fgs = _fgs.Device()
        return fgs.get_order_status(self.session, soid, locale=locale)

    def wafs(self, locale=None):
        """List active waf devices you ordered.

        :param string locale: Messages are displayed in Japanese or English
                              depending on this value.
                              ja: Japanese, en: English. Default value is "en".
        :return: WAF.
        :rtype: :class:`~ecl.security.v1.waf.WAF`
        """
        fgwaf = _fgwaf.WAF()
        return fgwaf.list(self.session, locale=locale)

    def create_waf(self, licensekind, azgroup, locale=None):
        """Create a new WAF device.

        :param string licensekind: Set "02", "04" or "08" as WAF plan.
        :param string azgroup: Availability Zone
        :param string locale: Messages are displayed in Japanese or English
                              depending on this value.
                              ja: Japanese, en: English. Default value is "en".
        :return: WAF.
        :rtype: :class:`~ecl.security.v1.waf.WAF`
        """
        body = {}
        body["tenant_id"] = self.session.get_project_id()
        body["gt_host"] = [{
            "operatingmode": "WAF",
            "licensekind": licensekind,
            "azgroup": azgroup
        }]
        body["sokind"] = "A"
        if locale:
            body["locale"] = locale
        return self._create(_fgwaf.WAF, **body)

    def get_waf_order_status(self, soid, locale=None):
        """Check progress status of Managed WAF device Service Order.

        :param string soid: This value is returned value of when you execute
                            Create Server, Update Server or Delete Server API.
        :param string locale: Messages are displayed in Japanese or English
                              depending on this value.
                              ja: Japanese, en: English. Default value is "en".
        :return: WAF.
        :rtype: :class:`~ecl.security.v1.waf.WAF`
        """
        fgwaf = _fgwaf.WAF()
        return fgwaf.get_order_status(self.session, soid, locale=locale)

    def update_waf(self, hostname, licensekind, locale=None):
        """Change plan of device.

        :param string licensekind: Set "02", "04" or "08" as WAF plan.
        :param string hostname: Set the hostname.
        :param string locale: Messages are displayed in Japanese or English
                              depending on this value.
                              ja: Japanese, en: English. Default value is "en".
        :return: WAF.
        :rtype: :class:`~ecl.security.v1.waf.WAF`
        """
        body = {}
        body["tenant_id"] = self.session.get_project_id()
        body["gt_host"] = [{
            "hostname": hostname,
            "licensekind": licensekind
        }]
        body["sokind"] = "M"
        if locale:
            body.update({"locale": locale})
        fgwaf = _fgwaf.WAF()
        return fgwaf.update(self.session, **body)

    def delete_waf(self, hostname, locale=None):
        """Delete a WAF device.

        :param string hostname: Set the hostname.
        :param string locale: Messages are displayed in Japanese or English
                              depending on this value.
                              ja: Japanese, en: English. Default value is "en".
        :return: WAF.
        :rtype: :class:`~ecl.security.v1.waf.WAF`
        """
        body = {}
        body["tenant_id"] = self.session.get_project_id()
        body["gt_host"] = [{
            "hostname": hostname
        }]
        body["sokind"] = "D"
        if locale:
            body["locale"] = locale
        fgwaf = _fgwaf.WAF()
        return fgwaf.delete(self.session, body, locale=locale)

    def get_hbs_order_status(self, soid, locale=None):
        """Check progress status of Host-based Security Service Order.

        :param string soid: This value is returned value of when you execute API
                            of Order Host-based Security, Change menu or
                            quantity, or Cancel the order.
        :param string locale: Messages are displayed in Japanese or English
                              depending on this value.
                              ja: Japanese, en: English. Default value is "en".
        :return: Host Based Security.
        :rtype: :class:`~ecl.security.v1.host_based_security.HostBasedSecurity`
        """
        hbs = _hbs.HostBasedSecurity()
        return hbs.get_order_status(self.session, soid, locale=locale)

    def get_hbs_order_info(self, locale=None):
        """Get Order Information that tied to tenant id.

        :param string locale: Messages are displayed in Japanese or English
                              depending on this value.
                              ja: Japanese, en: English. Default value is "en".
        :return: Host Based Security.
        :rtype: :class:`~ecl.security.v1.host_based_security.HostBasedSecurity`
        """
        hbs = _hbs.HostBasedSecurity()
        return hbs.get_order_info(self.session, locale=locale)

    def order_hbs(self, service_order_service, max_agent_value,
                                  mailaddress, dsm_lang, time_zone,
                                  locale=None):
        """Make a new application for Host-based Security.

        :param string service_order_service: Requested menu.
            Set "Managed Anti-Virus", "Managed Virtual Patch"
            or "Managed Host-based Security Package" to this field.
        :param string max_agent_value: Set maximum quantity of Agenet usage.
        :param string mailaddress: Contactable mail address.
        :param string dsm_lang: This value is used for language of Deep
                                Security Manager. ja: Japanese, en: English.
        :param string time_zone: Set "Asia/Tokyo" for JST or "Etc/GMT" for UTC.
        :param string locale: Messages are displayed in Japanese or English
                              depending on this value.
                              ja: Japanese, en: English. Default value is "en".
        :return: Host Based Security
        :rtype: :class:`~ecl.security.v1.host_based_security.HostBasedSecurity`
        """
        body = {}
        body["tenant_id"] = self.session.get_project_id()
        body["service_order_service"] = service_order_service
        body["max_agent_value"] = max_agent_value
        body["mailaddress"] = mailaddress
        body["dsm_lang"] = dsm_lang
        body["time_zone"] = time_zone
        body["sokind"] = "N"
        if locale:
            body["locale"] = locale
        return self._create(_hbs.HostBasedSecurity, **body)

    def change_hbs_menu(self, service_order_service, mailaddress, locale=None):
        """Change menu of Host-based Security.

        :param string service_order_service: Requested menu.
            Set "Managed Anti-Virus", "Managed Virtual Patch"
            or "Managed Host-based Security Package" to this field.
        :param string mailaddress: Contactable mail address.
        :param string locale: Messages are displayed in Japanese or English
                              depending on this value.
                              ja: Japanese, en: English. Default value is "en".
        :return: Host Based Security.
        :rtype: :class:`~ecl.security.v1.host_based_security.HostBasedSecurity`
        """
        body = {}
        body["tenant_id"] = self.session.get_project_id()
        body["service_order_service"] = service_order_service
        body["mailaddress"] = mailaddress
        body["sokind"] = "M1"
        if locale:
            body.update({"locale": locale})
        hbs = _hbs.HostBasedSecurity()
        return hbs.update(self.session, **body)

    def change_hbs_quantity(self, max_agent_value, mailaddress, locale=None):
        """Change maximum quantity of Agent usage.

        :param string max_agent_value: Set maximum quantity of Agenet usage.
        :param string mailaddress: Contactable mail address.
        :param string locale: Messages are displayed in Japanese or English
                              depending on this value.
                              ja: Japanese, en: English. Default value is "en".
        :return: Host Based Security.
        :rtype: :class:`~ecl.security.v1.host_based_security.HostBasedSecurity`
        """
        body = {}
        body["tenant_id"] = self.session.get_project_id()
        body["max_agent_value"] = max_agent_value
        body["mailaddress"] = mailaddress
        body["sokind"] = "M2"
        if locale:
            body.update({"locale": locale})
        hbs = _hbs.HostBasedSecurity()
        return hbs.update(self.session, **body)

    def cancel_hbs(self, mailaddress, locale=None):
        """Cancel the order of Host-based Security.

        :param string mailaddress: Contactable mail address.
        :param string locale: Messages are displayed in Japanese or English
                              depending on this value.
                              ja: Japanese, en: English. Default value is "en".
        :return: Host Based Security.
        :rtype: :class:`~ecl.security.v1.host_based_security.HostBasedSecurity`
        """
        body = {}
        body["tenant_id"] = self.session.get_project_id()
        body["mailaddress"] = mailaddress
        body["sokind"] = "C"
        if locale:
            body["locale"] = locale
        hbs = _hbs.HostBasedSecurity()
        return hbs.delete(self.session, body, locale=locale)
