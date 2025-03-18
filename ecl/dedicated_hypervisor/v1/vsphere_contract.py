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

from ecl.dedicated_hypervisor import dedicated_hypervisor_service
from ecl import resource2


class VsphereContract(resource2.Resource):
    resources_key = 'vsphere_contracts'
    resource_key = 'vsphere_contract'
    base_path = '/vsphere_contracts'
    service = dedicated_hypervisor_service.DedicatedHypervisorService()

    # Properties
    #: Contract year
    contract_year = resource2.Body('contract_year')
    #: The flag that you renew the contract or not
    contract_renewal = resource2.Body('contract_renewal')
    #: The number of cores used for calculating the discount amount for current month
    cores = resource2.Body('cores')
    #: The month that your contract starts
    start_month = resource2.Body('start_month')
    #: The month that your contract ends
    end_month = resource2.Body('end_month')
    #: The number of additional cores used from next month
    pending_cores = resource2.Body('pending_cores')
    #: The number of cores used for calculating the discount amount for next month
    cores_in_next_month = resource2.Body('cores_in_next_month')

    def list(self, session, **params):
        resp = session.get(
            self.base_path,
            endpoint_filter=self.service
        )
        resp = resp.json()
        datas = resp[self.resources_key]
        all_server_cores = resp['all_server_cores']
        vsphere_contracts_histories = resp['vsphere_contracts_histories']
        vsphere_contracts = []
        for data in datas:
            data.pop("self", None)
            vsphere_contract = self.existing(**data)
            vsphere_contracts.append(vsphere_contract)
        return vsphere_contracts, all_server_cores, vsphere_contracts_histories

    def manage_vsphere_contract(self, session, contract_year, cores):
        params = {}
        params['contract_year'] = contract_year
        params['cores'] = cores
        resp = session.put(
            self.base_path,
            endpoint_filter=self.service,
            json={self.resource_key: params}
        )
        self._translate_response(resp)
        return self

    def renewal_vsphere_contract(self, session, contract_year, contract_renewal=None):
        params = {}
        params['contract_year'] = contract_year
        if contract_renewal:
            params['contract_renewal'] = contract_renewal
        resp = session.post(
            self.base_path,
            endpoint_filter=self.service,
            json={self.resource_key: params}
        )
        self._translate_response(resp)
        return self
