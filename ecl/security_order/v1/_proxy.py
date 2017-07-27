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

from ecl.security_order.v1 import single_firewall as _fgs
from ecl import proxy2


class Proxy(proxy2.BaseProxy):

    def single_firewalls(self, locale=None):
        """List Managed Firwall/UTM devices of single constitution.

        :param string locale: Messages are displayed in Japanese or English
                              depending on this value.
                              ja: Japanese, en: English. Default value is "en".
        :return: Single Firwall/UTM.
        :rtype: :class:`~ecl.security.v1.single_firewall.SingleFirewall`
        """
        fgs = _fgs.SingleFirewall()
        return fgs.list(self.session, locale=locale)

    def create_single_firewall(self, operatingmode, licensekind,
                               azgroup, locale=None):
        """Create a new Managed Firewall/UTM device of single constitution.

        :param string operating_mode: Set "FW" or "UTM" to this value.
        :param string licensekind: Set "02" or "08" as FW/UTM plan.
        :param string azgroup: Availability Zone
        :param string locale: Messages are displayed in Japanese or English
                              depending on this value.
                              ja: Japanese, en: English. Default value is "en".
        :return: Single Firwall/UTM.
        :rtype: :class:`~ecl.security.v1.single_firewall.SingleFirewall`
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
        return self._create(_fgs.SingleFirewall, **body)

    def update_single_firewall(self, hostname, operatingmode,
                               licensekind, locale=None):
        """Change menu (Firewall/Managed UTM) and/or plan of single device.

        :param string operating_mode: Set "FW" or "UTM" to this value.
        :param string licensekind: Set "02" or "08" as FW/UTM plan.
        :param string hostname: Set the hostname.
        :param string locale: Messages are displayed in Japanese or English
                              depending on this value.
                              ja: Japanese, en: English. Default value is "en".
        :return: Single Firwall/UTM.
        :rtype: :class:`~ecl.security.v1.single_firewall.SingleFirewall`
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
        fgs = _fgs.SingleFirewall()
        return fgs.update(self.session, **body)

    def get_order_status(self, soid, locale=None):
        """Check progress status of Managed Firewall/UTM device Service Order.

        :param string soid: This value is returned value of when you execute
                            Create Server, Update Server or Delete Server API.
        :param string locale: Messages are displayed in Japanese or English
                              depending on this value.
                              ja: Japanese, en: English. Default value is "en".
        :return: Single Firwall/UTM.
        :rtype: :class:`~ecl.security.v1.single_firewall.SingleFirewall`
        """
        fgs = _fgs.SingleFirewall()
        return fgs.get_order_status(self.session, soid, locale=locale)

    def delete_single_firewall(self, hostname, locale=None):
        """Delete a Managed Firewall/UTM device of single constitution.

        :param string hostname: Set the hostname.
        :param string locale: Messages are displayed in Japanese or English
                              depending on this value.
                              ja: Japanese, en: English. Default value is "en".
        """
        body = {}
        body["tenant_id"] = self.session.get_project_id()
        body["gt_host"] = [{
            "hostname": hostname
        }]
        body["sokind"] = "D"
        if locale:
            body["locale"] = locale
        fgs = _fgs.SingleFirewall()
        return fgs.delete(self.session, body, locale=locale)
