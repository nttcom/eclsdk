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

from ecl.dedicated_hypervisor.v1 import license as _license
from ecl.dedicated_hypervisor.v1 import license_type as _license_type
from ecl.dedicated_hypervisor.v1 import server as _server
from ecl.dedicated_hypervisor.v1 import usage as _usage
from ecl.dedicated_hypervisor.v1 import vcf as _vcf
from ecl.dedicated_hypervisor.v1 import vcenter as _vcenter
from ecl.dedicated_hypervisor.v1 import vsphere_contract as _vsphere_contract
from ecl import proxy2


class Proxy(proxy2.BaseProxy):

    def servers(self, details=True, **query):
        """
        List your Dedicated Hypervisor servers information.

        :param query: Query parameters to select results
        :return: list of the servers
        :rtype: list of :class:`~ecl.dedicated_hypervisor.v1.server.Server`
        """
        server = _server.ServerDetail if details else _server.Server
        return list(self._list(server, **query))

    def get_server(self, server_id):
        """
        Shows your Dedicated Hypervisor server information.

        :param string server_id: ID for the server.
        :return: One :class:`~ecl.dedicated_hypervisor.v1.server.Sever`
            instance.
        :rtype: :class:`~ecl.dedicated_hypervisor.v1.server.Server`
        """
        return self._get(_server.Server, server_id)

    def create_server(self, name, networks, image, flavor,
                      admin_pass=None, description=None, availability_zone=None,
                      metadata=None):
        """
        Create additional Dedicated Hypervisor server.

        :param string name: Name of your Dedicated Hypervisor/Baremetal server
            as a string.
        :param string description: Description of your Dedicated Hypervisor
            server as a string.
        :param array networks: If it is specified greater than two,
            default gateway is first network.
        :param string flavor: The flavor reference for the desired flavor
            for your Dedicated Hypervisor server.
            Specify as an UUID or full URL.
            Parameters of id or links -> href in api_list_flavors page
            can be used as flavorRef parameter.
        :param string admin_pass: Password for the administrator.
        :param string image: The image reference for the desired image
            for your Dedicated Hypervisor server.
            Specify as an UUID or full URL.
        :param string availability_zone: The availability zone name
            in which to launch the server.
            If omit this parameter, target availability_zone is random.
        :param dict metadata: Metadata key and value pairs.
            The maximum size of the metadata key and value is 255 bytes each.
        :return: The results of server createion.
        :rtype: :class:`~ecl.dedicated_hypervisor.v1.server.Server`
        """
        body = {}
        body["name"] = name
        body["networks"] = networks
        body["imageRef"] = image
        body["flavorRef"] = flavor
        if admin_pass:
            body["adminPass"] = admin_pass
        if description:
            body["description"] = description
        if availability_zone:
            body["availability_zone"] = availability_zone
        if metadata:
            body["metadata"] = metadata
        return self._create(_server.Server, **body)

    def update_server(self, server_id, name):
        """
        Updates the editable attributes of the specified baremetal server.

        :param string server_id: ID for the server.
        :param string name: Name of your Dedicated Hypervisor/Baremetal server
            as a string.
        :return: The results of server update.
        :rtype: :class:`~ecl.dedicated_hypervisor.v1.server.Server`
        """
        body = {"name": name}
        return self._update(_server.Server, server_id, **body)

    def delete_server(self, server_id, ignore_missing=False):
        """
        Deletes a specified Dedicated Hypervisor server.
        You can delete server when specified server status is
        ACTIVE or ERROR status.

        :param string server_id: ID for the server.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the server does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent server
        :returns: ``None``
        """
        return self._delete(_server.Server, server_id,
                            ignore_missing=ignore_missing)

    def license_types(self):
        """
        Lists your Guest Image license on Dedicated Hypervisor servers
        information.

        :return: list of the license types.
        :rtype: list of
            :class:`~ecl.dedicated_hypervisor.v1.license_type.LicenseType`
        """
        return list(self._list(_license_type.LicenseType, paginated=False))

    def find_license_type(self, name_or_id, ignore_missing=False):
        """Find a single license type

        :param name_or_id: The name or ID of a license type.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.dedicated_hypervisor.v1.license_type.LicenseType` or None
        """
        return self._find(_license_type.LicenseType, name_or_id,
                          ignore_missing=ignore_missing)

    def licenses(self, license_type=None):
        """
        Lists your Guest Image license key information.

        :return: list of the licenses.
        :rtype: list of
            :class:`~ecl.dedicated_hypervisor.v1.license.License`
        """
        return list(self._list(_license.License, license_type=license_type,
                               paginated=False))

    def create_license(self, license_type):
        """
        Create additional Guest Image license key.
        You can create additional license key only for the licenses which
        `has_license_key` property is True.

        :param string license_type: Name of your Guest Image license type
            as a string.
        :return: The results of license createion.
        :rtype: :class:`~ecl.dedicated_hypervisor.v1.license.License`
        """

        lic = _license.License()
        return lic.create(self.session, license_type)

    def delete_license(self, license_id, ignore_missing=False):
        """
        Delete a specified Guest Image license key.

        :param string license_id: ID for the license
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the server does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent server
        :returns: ``None``
        """
        return self._delete(_license.License, license_id,
                            ignore_missing=ignore_missing)

    def usages(self):
        """
        Lists your Guest Image usage information.

        :return: list of the usages
        :rtype: list of :class:`~ecl.dedicated_hypervisor.v1.usage.Usage`
        """
        return list(self._list(_usage.Usage))

    def get_usage_histories(self, history_id, From=None, to=None):
        """
        Shows your Guest Image usage history information.

        :param string history_id: ID for the history.
        :param dateTime From: date to list usage from. `YYYY-MM-DD hh:mm:ss` .
        :param dateTime to: date to list usage to. month of the parameter
            must be the same as `from` . `YYYY-MM-DD hh:mm:ss` .
        :return: :class:`~ecl.dedicated_hypervisor.v1.usage.Usage`
        """
        query = {}
        if From:
            query["from"] = From
        if to:
            query["to"] = to
        usage = _usage.Usage()
        return usage.get_usage_histories(session=self.session,
                                         history_id=history_id, **query)

    def add_license(self, server_id, license_types, vm_id=None, vm_name=None):
        """Add license to VM on hyper visor

        :param string server_id: ID of server that have VM to add license
        :param array license_types: Array of license type's Name
        :param string vm_id: VM ID, Specify either vm_id or vm_name
        :param string vm_name: VM Name, Specify either vm_id or vm_name
        :returns: dict of job_id
        """
        server = _server.ServerAction()
        return server.add_license(self.session, server_id, license_types,
                                  vm_id=vm_id, vm_name=vm_name)

    def get_add_license_job(self, server_id, job_id):
        """Get add license job status

        :param string server_id: Server ID
        :param string job_id: Job ID
        :returns: Job object
        """
        server = _server.ServerAction()
        return server.get_add_license_job(self.session, server_id, job_id)


    def sddcs(self, **query):
        return list(self._list(_vcf.Sddc, **query))


    def delete_sddc(self, sddc_id, ignore_missing=False):
        return self._delete(_vcf.Sddc, sddc_id, ignore_missing=ignore_missing)

    def get_cfgw_connection(self, server_id):
        """
        Shows the connection status between your Dedicated Hypervisor and
        common function gateway network.

        :param string server_id: ID for the server.
        :return: One :class:`~ecl.dedicated_hypervisor.v1.server.CFGWConnection`
        instance.
        """
        cfgw = _server.CFGWConnection()
        return cfgw.get_cfgw_connection(self.session, server_id)

    def update_cfgw_connection(self, server_id):
        """
        Updates the connection status between your Dedicated Hypervisor and
        common function gateway network.

        :param string server_id: ID for the server.
        :return: One :class:`~ecl.dedicated_hypervisor.v1.server.CFGWConnection`
        instance.
        """
        cfgw = _server.CFGWConnection()
        return cfgw.update_cfgw_connection(self.session, server_id)

    def show_vcenter(self):
        """
        Shows the registered vCenter server information.

        :return: A list of the vCenter servers
        :rtype: list of :class:`~ecl.dedicated_hypervisor.v1.vcenter.VCenter`
        instance.
        """
        return list(self._list(_vcenter.VCenter))

    def register_vcenter(self, link_local_address, password, license_id):
        """
        Register the vCenter Server.

        :param link_local_address: The IP address that you can assign to your vCenter.
        :param password: The password of vCenter server. Available character is
                1-20 character of alphabet[a-zA-Z], number[0-9] and Symbols[
                .-_/*+,!#$%&()~|].
        :param string license_id: ID for license of vCenter server.

        :return: One :class:`~ecl.dedicated_hypervisor.v1.vcenter.VCenter`
        instance.
        """
        vcenter = _vcenter.VCenter()
        return vcenter.register(self.session, link_local_address, password, license_id)

    def update_vcenter(self, vcenter_id, link_local_address=None, password=None, license_id=None):
        """
        Updates the registered vCenter server information.

        :param link_local_address: The IP address that you can assign to your vCenter.
        :param string vcenter_id: ID for the vcenter server.
        :param password: The password of vCenter server. Available character is
                1-20 character of alphabet[a-zA-Z], number[0-9] and Symbols[
                .-_/*+,!#$%&()~|].
        :param string license_id: ID for license of vCenter server.
        :return: One :class:`~ecl.dedicated_hypervisor.v1.vcenter.VCenter`
        instance.
        """
        vcenter = _vcenter.VCenter()
        return vcenter.update(self.session, vcenter_id, link_local_address, password, license_id)

    def delete_vcenter(self, vcenter_id, ignore_missing=False):
        """
        Deletes the registered vCenter server.

        :param string vcenter_id: ID for the vcenter server.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the server does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent server
        :returns: ``None``
        """
        return self._delete(_vcenter.VCenter, vcenter_id ,
                            ignore_missing=ignore_missing)

    def available_addresses_vcenter(self):
        """
        List the link local addresses that you can assign to your vCenter.

        :return: A list of the link local addresses
        :rtype: list of :class:`~ecl.dedicated_hypervisor.v1.vcenter.VCenter`
        instance.
        """
        return list(self._list(_vcenter.LinkLocalAddresses))

    def vsphere_contracts(self):
        """
        List vSphere Contracts.

        :returns:
            vsphere_contracts: A list of the vSphere Contracts
            all_server_cores: The total cores of your vSphere ESXi server.
            vsphere_contracts_histories: A list of the vSphere contracts histories.
        :rtype:
            vsphere_contracts: list of :class:`~ecl.dedicated_hypervisor.v1._vsphere_contract.VSphereContract` instance.
            all_server_cores: integer
            vsphere_contracts_histories: dict
        """
        vsphere_contract = _vsphere_contract.VSphereContract()
        return vsphere_contract.list(self.session)

    def manage_vsphere_contract(self, contract_year, cores):
        """
        Manage vSphere Contracts.

        :param integer contract_year: The number of years of the contract. You can specify 1 or 3.
        :param integer cores: The number of cores to be added to your contract.
        :return: vSphere Contract.
        :rtype: :class:`~ecl.dedicated_hypervisor.v1._vsphere_contract.VSphereContract`
        """
        vsphere_contract = _vsphere_contract.VSphereContract()
        return vsphere_contract.manage(self.session, contract_year, cores)

    def renewal_vsphere_contract(self, contract_year, contract_renewal=None):
        """
        Enable/Disable Contract Renewal.

        :param integer contract_year: The number of years of the contract. You can specify 1 or 3.
        :param bool contract_renewal: The flag that you renew your contract or not.
        :return: vSphere Contract.
        :rtype: :class:`~ecl.dedicated_hypervisor.v1._vsphere_contract.VSphereContract`
        """
        vsphere_contract = _vsphere_contract.VSphereContract()
        return vsphere_contract.renewal(self.session, contract_year, contract_renewal)
