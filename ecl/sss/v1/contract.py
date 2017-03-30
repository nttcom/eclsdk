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

from ecl.sss import  sss_service
from ecl import resource2


class Contract(resource2.Resource):
    resource_key = None
    resources_key = None
    base_path = '/contracts'
    service = sss_service.SssService()

    # Capabilities
    allow_create = True
    allow_get = True
    allow_delete = True
    allow_list = True
    put_create = False

    # Properties
    #: Contract ID.
    contract_id = resource2.Body('contract_id', alternate_id=True)
    #: Login ID of user.
    login_id = resource2.Body('login_id')
    #: E-mail address of the user.
    mail_address = resource2.Body('mail_addresss')
    #: Password of the user. If user set this item as blank, the system
    #: set initial random password automatically.
    password = resource2.Body('password')
    #: By using this item, the partner API user can associate optional
    #: string to the constract(e.g. The end user management ID in the
    #: partner user's system). Note that this ID will be NOT used to
    #: control the contract in ECL2.0 internal system. If the item is
    #: set as blank, ECL 2.0 system set the end user's contract ID
    #: automatically
    external_reference_id = resource2.Body('external_reference_id')
    #: Setting true or false(default is false). This item designate
    #: whether the system should send to the login_ID and Password with
    #: e-mail.
    notify_password = resource2.Body('notify_password')
    #: User id. format is ecid[0-9]{10}.
    user_id = resource2.Body('user_id')
    #: This user's API key for keystone authentication.
    keystone_name = resource2.Body('keystone_name')
    #: This user's API secret for keystone authentication.
    keystone_password = resource2.Body('keystone_password')
    #: Keystone address this user can use to get token for SSS API
    #: request.
    keystone_endpoint = resource2.Body('keystone_endpoint')
    #: SSS endpoint recommended for user.
    sss_endpoint = resource2.Body('sss_endpoint')
    #: status
    status = resource2.Body('status')
    #: customer_name
    customer_name = resource2.Body('customer_name')
    #: This ID is equal to external_reference_id.
    customer_number = resource2.Body('customer_number')
    #: Channel name.
    channel_name = resource2.Body('channel_name')
    #: Channel ID of this contract.
    channel_id = resource2.Body('channel_id')
    #: Whether this channel_id is the partner management channel(true),
    #: or not(false).
    management_channel = resource2.Body('management_channel')
    #: The owner user ID in the Contract
    contract_owner_user_id = resource2.Body('contract_owner_user_id')
    #: Start time of the contract
    start_time = resource2.Body('start_time')
    #: End time of the contract
    end_time = resource2.Body('end_time')
    #: Internal use(Login type)
    login_integration = resource2.Body('login_integration')
    #: Access point to use APIs in the decided region
    sss_endpoint = resource2.Body('sss_endpoint')
    #: keystone_endpoint
    keystone_endpoint = resource2.Body('keystone_endpoint')
    #: Internal use
    company_code = resource2.Body('company_code')
    #: Internal use
    glass_customer_id = resource2.Body('glass_customer_id')
    #: Internal use
    glass_user_id = resource2.Body('glass_user_id')
    #: The status of the acquired charge information (estimated:
    #: undetermined / fixed: Committed)
    charge_status = resource2.Body('charge_status')
    #: Period of the acquired charge information(Start time)
    cycle_start_time = resource2.Body('cycle_start_time')
    #: Period of the acquired charge information(End time)
    cycle_end_time = resource2.Body('cycle_end_time')
    #: The detail of billing information
    charge_data = resource2.Body('charge_data')
    #: The designated contract ID by request's target_contract_id.
    owner_contract_id = resource2.Body('owner_contract_id')

    def list(self, session, channel_id, include_deleted):
        """List contracts by channel id"""

        url = self.base_path + '?channel_id=%s&include_deleted=%s' % (
            channel_id, include_deleted
        )
        resp = session.get(
            url, endpoint_filter=self.service
        )
        self._translate_response(resp, has_body=True)
        return self

    def get_billing_info(self, session, channel_id, target_month):
        """Get billing information by channel id and target month"""

        url = self.base_path + '/%s/billing/%s' % (
            channel_id, target_month)
        resp = session.get(
            url, endpoint_filter=self.service
        )
        self._translate_response(resp, has_body=True)
        return self

    def get_monthly_billing_of_each_contract(
            self, session, contract_id, target_month, target_contract_id
    ):
        """Get montly billing for each contract."""

        url = self.base_path + "/%s/billing/%s/target_contract/%s" % (
            contract_id, target_month, target_contract_id
        )
        resp = session.get(url, endpoint_filter=self.service)
        self._translate_response(resp, has_body=True)
        return self
