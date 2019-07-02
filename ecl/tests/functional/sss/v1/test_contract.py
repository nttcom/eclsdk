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

import six
from ecl.tests.functional import base


class TestContract(base.BaseFunctionalTest):
    def test_contracts(self):
        contracts = list(self.conn.sss.contracts("channel_id-xxxxx"))
        for i in contracts:
            print(i.id + " " + i.login_id)
        self.assertGreater(len(contracts), 0)

    @classmethod
    def test_01_create_contract(cls):
        contract = cls.conn.sss.create_contract(
            login_id="test001",
            mail_address="test@ntt.com",
            password="dsrtf34ht",
            external_reference_id="GXXXXXXXX",
            channel_id="chxxxxxxx",
            notify_password="true",
        )
        cls.new_contract_id = contract.id
        assert isinstance(contract.login_id, six.string_types)
        assert isinstance(contract.mail_address, six.string_types)
        assert isinstance(contract.id, six.string_types)
        assert isinstance(contract.user_id, six.string_types)
        assert isinstance(contract.keystone_name, six.string_types)
        assert isinstance(contract.keystone_password, six.string_types)
        assert isinstance(contract.keystone_endpoint, six.string_types)
        assert isinstance(contract.sss_endpoint, six.string_types)
        assert isinstance(contract.password, six.string_types)

    def test_02_delete_contract(self):
        self.conn.sss.delete_contract(self.new_contract_id)
        self.conn.sss.delete_contract("contract_xxxxx")

    def test_03_get_contract(self):
        contract = self.conn.sss.get_contract("econ1000015949")
        assert isinstance(contract.id, six.string_types)
        assert isinstance(contract.status, six.string_types)
        assert isinstance(contract.customer_number, six.string_types)
        assert isinstance(contract.channel_name, six.string_types)
        assert isinstance(contract.channel_id, six.string_types)
        assert isinstance(contract.management_channel, bool)
        assert isinstance(contract.contract_owner_user_id,
                          six.string_types)
        assert isinstance(contract.start_time, six.string_types)
        assert isinstance(contract.end_time, six.string_types)
        assert isinstance(contract.login_integration, six.string_types)
        assert isinstance(contract.sss_endpoint, six.string_types)
        assert isinstance(contract.sss_endpoint, six.string_types)
        assert isinstance(contract.company_code, six.string_types)
        assert isinstance(contract.glass_customer_id, six.string_types)
        assert isinstance(contract.glass_user_id, six.string_types)

    def test_04_get_billing_info(self):
        bill = self.conn.sss.get_billing_info("econ1000015949", "2016-02")
        assert isinstance(bill.id, six.string_types)
        assert isinstance(bill.customer_number, six.string_types)
        assert isinstance(bill.charge_status, six.string_types)
        assert isinstance(bill.cycle_start_time, six.string_types)
        assert isinstance(bill.cycle_end_time, six.string_types)
        assert isinstance(bill.charge_data, dict)

    def test_05_get_monthly_billing_of_each_contract(self):
        bill = self.conn.sss.get_monthly_billing_of_each_contract(
            "econ1000015949", "2016-02", "econ1000015949"
        )

        assert isinstance(bill.id, six.string_types)
        assert isinstance(bill.owner_contract_id, six.string_types)
        assert isinstance(bill.customer_number, six.string_types)
        assert isinstance(bill.charge_status, six.string_types)
        assert isinstance(bill.cycle_start_time, six.string_types)
        assert isinstance(bill.cycle_end_time, six.string_types)
        assert isinstance(bill.charge_data, dict)
