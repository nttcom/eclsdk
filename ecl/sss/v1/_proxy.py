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

from ecl.sss.v1 import user as _user
from ecl.sss.v1 import tenant as _tenant
from ecl.sss.v1 import role as _role
from ecl.sss.v1 import api_key as _api_key
from ecl.sss.v1 import channel as _channel
from ecl.sss.v1 import contract as _contract
from ecl.sss.v1 import iam_group as _iam_group
from ecl.sss.v1 import iam_role as _iam_role
from ecl import proxy2


class Proxy(proxy2.BaseProxy):
    def users(self):
        """
        List users in the designated contract.

        :return: A generator of user instances.
        :rtype: :class:`~ecl.sss.v1.user.User`
        """
        return list(self._list(_user.User, paginated=False))

    def find_user(self, user_id, ignore_missing=False):
        """
        Find a user. Get user information such as login id, email, apikey, etc.

        :param user_id: ID of a user
        :param ignore_missing: When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :return: One :class:`~ecl.sss.v1.user.User` or None
        """
        return self._find(_user.User, user_id,
                           ignore_missing=ignore_missing)

    def get_user(self, user):
        """
        Get user information such as login id, email, apikey, etc.

        :param user: ID of a user or a :class:`~ecl.sss.v1.user.User` instance.
        :return: One :class:`~ecl.sss.v1.user.User` or
                     :class:`~ecl.exceptions.ResourceNotFound`when no
                     resource can be found.
        """
        return self._get(_user.User, user)

    def create_user(self, login_id, mail_address, notify_password,
                    password=None):
        """
        Create user in the designated contract. Only supser user (contract
        owner user) allowed.

        :param login_id: Login id of new user.
        :param mail_address: Mail address of new user.
        :param notify_password: If this flag is set 'true',
            notification email will be sent to new users email
        :param password: Initial password of new user.
            If this parameter is not designated, random initial password is
            generated and applied to new user.
        :return: The results of user creation
        :rtype: :class:`~ecl.sss.v1.user.User`
        """
        body = {}
        body["login_id"] = login_id
        body["mail_address"] = mail_address
        body["notify_password"] = notify_password
        if password:
            body["password"] = password
        return self._create(_user.User, **body)

    def update_user(self, user_id, login_id=None, mail_address=None,
                    new_password=None):
        """
        Update user's informain.

        :param user_id: Specified user_id.
        :param login_id: Login id of new user.
        :param mail_address: Mail address of new user.
        :param new_password: New password of the user.
        :return: ``None``
        """
        body = {}
        if login_id:
            body["login_id"] = login_id
        if mail_address:
            body["mail_address"] = mail_address
        if new_password:
            body["new_password"] = new_password
        user = _user.User()
        return user.update(self.session, user_id, **body)

    def delete_user(self, user, ignore_missing=False):
        """
        Delete user. Only supser user (contract owner user) allowed. Contract
        owner user itself cannot be deleted

        :param user: Delete target user's user id.
        :param ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the user does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent server
        :return: ``None``
        """
        self._delete(_user.User, user, ignore_missing=ignore_missing)

    def tenants(self, **query):
        """
        List tenants in the designated contract.

        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.

        :return: A generator of tenant instances.
        :rtype: :class:`~ecl.sss.v1.tenant.Tenant`
        """
        return list(self._list(_tenant.Tenant, paginated=False, **query))

    def find_tenant(self, tenant_id, ignore_missing=False):
        """
        Find a tenant. Get tenant information such as tenant name, etc.

        :param tenant_id: ID of a tenant
        :param ignore_missing: When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :return: One :class:`~ecl.sss.v1.tenant.Tenant` or None
        """
        return self._find(_tenant.Tenant, tenant_id,
                           ignore_missing=ignore_missing)

    def create_tenant(self, **attrs):
        """
        Create new tenant in the designated contract. Only supser user
        (contract owner user) allowed.

        :param attrs: Keyword arguments which will be used to create
                      a :class:`~ecl.sss.v1.tenant.Tenant`,
                      comprised of the properties on the Tenant class.
        :return: The results of tenant creation
        :rtype: :class:`~ecl.sss.v1.tenant.Tenant`
        """
        return self._create(_tenant.Tenant, **attrs)

    def delete_tenant(self, tenant, ignore_missing = True):
        """
        Delete tenant. Only supser user (contract owner user) allowed.

        :param tenant: Delete target tenant's tenant id.
        :param ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the user does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent server
        :return: ``None``
        """
        self._delete(_tenant.Tenant, tenant, ignore_missing=ignore_missing)

    def create_role(self, user_id, tenant_id):
        """
        Create role between a user and a tenant. With role, users can access
        to the tenants.

        :param user_id: User which have new role.
        :param tenant_id: Tenant which the user have role.
        :return: :class:`~ecl.sss.v1.role.Role`
        """
        body = {}
        body["user_id"] = user_id
        body["tenant_id"] = tenant_id
        return self._create(_role.Role, **body)

    def delete_role(self, tenant_id, user_id):
        """
        Delete role between user and tenant. Contract owner user always have
        role to all tenants in the contract. Only supser user
        (contract owner user) allowed.

        :param tenant_id: Delete target tenant's tenant id.
        :param user_id: User's id of the role
        :return: ``None``
        """
        role = _role.Role()
        return role.delete(session=self.session,
                                 tenant_id=tenant_id, user_id=user_id)

    def update_api_key(self, user_id):
        """
        Update API key pair of target user.

        :param user_id: Change target user's user id.
        :return: The attributes to update on the api_key represented by
                ``Api_key``.
        """
        key = _api_key.Api_key()
        return key.update(session=self.session, user_id=user_id)

    def channels(self, get_contracts, **query):
        """
        Getting lists of information about the own channel and end user channel
        that own contract belongs. Only partner user allowed.

        :param get_contracts: The flag of whether getting contracts
                              (true or false(default)).
        :return: A generator of channels instances.
        :rtype: :class:`~ecl.sss.v1.channel.Channel`
        """
        return list(self._list(_channel.Channel, paginated=False,
                               get_contracts=get_contracts, **query))

    def create_contract(self, login_id, mail_address, channel_id, password=None,
                        external_reference_id=None, notify_password=None):
        """
        Create contract in designated channel. Only partner user allowed.

        :param login_id: Login ID of new user.
        :param mail_address: E-mail address of the user.
        :param channel_id: The channel means the group to manage contracts.
            The partner user will be given 2 channels. One is the channel that
            contains own contract. The other is the channel that contains all
            end user contracts which the partner user has. By executing the List
            Channel API(For partner user only),
            the user can get your (and enduser's) channel ID.
        :param password: Password of the user. If the API user set this item as
            blank, the system set initial random password automatically.
        :param external_reference_id: By using this item, the partner API user
            can associate optional string to the constract(e.g. The end user
            management ID in the partner user's system). Note that this ID will
            be NOT used to control the contract in ECL2.0 internal system.
            If the item is set as blank, ECL 2.0 system set the end user's
            contract ID automatically(e.g. econXXXXXXXX).
        :param notify_password: Setting true or false(default is false).
            This item designate whether the system should send to the login_ID
            and Password with e-mail.
        :return: :class:`~ecl.sss.v1.contract.Contract`
        """
        body = {}
        body["login_id"] = login_id
        body["mail_address"] = mail_address
        body["channel_id"] = channel_id
        if password:
            body["password"] = password
        if external_reference_id:
            body["external_reference_id"] = external_reference_id
        if notify_password:
            body["notify_password"] = notify_password
        return self._create(_contract.Contract, **body)

    def contracts(self, channel_id, include_deleted="false"):
        """
        List Contracts in the designated channel. Only partner user allowed.

        :param channel_id: Target channel_id under own contract.
        :param include_deleted: Setting true or false(default is false)
        (true : Include deleted contract/ false: Not include deleted contract.
        :return: A generator of contracts instances.
        :rtype: :class:`~ecl.sss.v1.contract.Contract`
        """
        contract = _contract.Contract()
        return list(contract.list(session=self.session, channel_id=channel_id,
                          include_deleted=include_deleted))

    def delete_contract(self, contract_id, ignore_missing=False):
        """
        Delete contract in designated channel. Only partner user allowed.

        :param contract_id: Contract ID of Delete target
        :param ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the user does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent server
        :return: ``None``
        """
        return self._delete(_contract.Contract, contract_id,
                            ignore_missing=ignore_missing)

    def get_contract(self, contract_id):
        """
        Get the information of the designated contract.

        :param contract_id: The contract ID getting more information.
        :return: One :class:`~ecl.sss.v1.contract.Contract`
        """
        return self._get(_contract.Contract, contract_id)

    def get_billing_info(self, channel_id, target_month):
        """
        Get billing statement of designated month.

        :param channel_id: Billing statement owner contract.
        :param target_month: Target billing month with YYYY-MM format
        :return: One :class:`~ecl.sss.v1.contract.Contract`
        """
        bill_info = _contract.Contract()
        return bill_info.get_billing_info(
            session=self.session, channel_id=channel_id,
            target_month=target_month
        )

    def get_monthly_billing_of_each_contract(self, contract_id, target_month,
                                             target_contract_id):
        """
        Get montly billing for each contract. Only partner user allowed.

        :param contract_id: Contract ID of this request.
        :param target_month: Target billing month with YYYY-MM format
        :param target_contract_id: Target contract ID
        :return:
        """
        bill_info = _contract.Contract()
        return bill_info.get_monthly_billing_of_each_contract(
            session=self.session,
            contract_id=contract_id, target_month=target_month,
            target_contract_id=target_contract_id
        )

    def iam_groups(self, contract_id):
        """
        List iam groups by contract id.

        :param contract_id: Contract ID ( Default is the Contract ID of
            API executing user ) .
        :return: A list of iam groups.
        :rtype: :class:`~ecl.sss.v1.iam_group.IAMGroup`
        """
        iam_group = _iam_group.IAMGroup()
        return list(iam_group.list(session=self.session,
                                   contract_id=contract_id))

    def create_iam_group(self, iam_group_name, contract_id=None,
                         description=None):
        """
        Create iam group.

        :param iam_group_name: New IAM Group name.
            Alphanumeric characters and @, -, ., _ can be used.
        :param contract_id: Contract ID ( Default is the Contract ID of API
            executing user ) .
        :param description: Description of the IAM Group.
        :return: :class:`~ecl.sss.v1.iam_group.IAMGroup`
        """
        body = {}
        body["iam_group_name"] = iam_group_name
        if contract_id:
            body["contract_id"] = contract_id
        if description:
            body["description"] = description
        return self._create(_iam_group.IAMGroup, **body)

    def delete_iam_group(self, iam_group_id, ignore_missing=False):
        """
        Delete iam group.

        :param iam_group_id: Group ID that you want to delete.
        :param ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the user does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent server
        :return: ``None``
        """
        return self._delete(_iam_group.IAMGroup, iam_group_id,
                            ignore_missing=ignore_missing)

    def assign_iam_role(self, iam_group_id, iam_role_id):
        """
        Assignment of the IAM Role to the IAM Group.

        :param iam_group_id: IAM Group ID that assign to the Role.
        :param iam_role_id: IAM Role ID that assign to the Group.
        :return: :class:`~ecl.sss.v1.iam_group.IAMGroup`
        """
        iam_group = _iam_group.IAMGroup()
        return iam_group.assign_iam_role(session=self.session,
                                         iam_group_id=iam_group_id,
                                         iam_role_id=iam_role_id)

    def delete_assign_iam_role(self, iam_group_id, iam_role_id):
        """
        Delete Assignment of the IAM Role to the IAM Group.

        :param iam_group_id: IAM Group ID.
        :param iam_role_id: IAM Role ID.
        :return: ``None``
        """
        iam_group = _iam_group.IAMGroup()
        return iam_group.delete_assign_iam_role(session=self.session,
                                                iam_group_id=iam_group_id,
                                                iam_role_id=iam_role_id)

    def users_designated_iam_group(self, iam_group_id):
        """
        List User list in the designated IAM Group ID.

        :param iam_group_id: IAM Group ID that you want to show user list.
        :return: :class:`~ecl.sss.v1.iam_group.IAMGroup`
        """
        iam_group = _iam_group.IAMGroup()
        return iam_group.list_users(session=self.session,
                                    iam_group_id=iam_group_id)

    def assign_user(self, iam_group_id, user_id):
        """
        Assignment of the IAM User to the IAM Group.

        :param iam_group_id: IAM Group ID that assign to the User.
        :param user_id: User ID that assign to the Group.
        :return: :class:`~ecl.sss.v1.iam_group.IAMGroup`
        """
        iam_group = _iam_group.IAMGroup()
        return iam_group.assign_user(session=self.session,
                                     iam_group_id=iam_group_id,
                                     user_id=user_id)

    def delete_assign_user(self, iam_group_id, user_id):
        """
        Delete Assignment of the User to the IAM Group.

        :param iam_group_id: IAM Group ID.
        :param user_id: User ID.
        :return: ``None``
        """
        iam_group = _iam_group.IAMGroup()
        return iam_group.delete_assign_user(session=self.session,
                                            iam_group_id=iam_group_id,
                                            user_id=user_id)

    def iam_roles(self, contract_id):
        """
        List IAM Role list in the designated contract.

        :param contract_id: Contract ID ( Default is the Contract ID of API
            executing user ) .
        :return: A list of iam groups.
        :rtype: :class:`~ecl.sss.v1.iam_role.IAMRole`
        """
        iam_role = _iam_role.IAMRole()
        return list(iam_role.list(session=self.session,
                                  contract_id=contract_id))

    def get_iam_role(self, iam_role_id):
        """
        Show a IAM Role's information. You can check a IAM Role's
            name, ID and resources by executing this API.

        :param iam_role_id: IAM Role ID that you want to check information.
        :return: :class:`~ecl.sss.v1.iam_role.IAMRole`
        """
        return self._get(_iam_role.IAMRole, iam_role_id)

    def create_iam_role(self, iam_role_name, resources, contract_id=None,
                        description=None):
        """
        Create IAM Role in the designated contract. Only supser user
        (contract owner user) can use this API.

        :param iam_role_name: New IAM Role name.
            Alphanumeric characters and @, -, ., _ can be used.
        :param resources: Whitelist rules of API execution.
            ( resources item is mandatory, but a user can define any rule by
            using follow parameters. )
        :param contract_id: Contract ID ( Default is the Contract ID of API
            executing user ).
        :param description: Description of the IAM Role.
        :return: :class:`~ecl.sss.v1.iam_group.IAMGroup`
        """
        body = {}
        body["iam_role_name"] = iam_role_name
        body["resources"] = resources
        if contract_id:
            body["contract_id"] = contract_id
        if description:
            body["description"] = description
        return self._create(_iam_role.IAMRole, **body)

    def delete_iam_role(self, iam_role_id, ignore_missing=False):
        """
        Delete designated IAM Role. Only supser user (contract owner user)
        can use this API.

        :param iam_role_id: IAM Role ID that you want to delete.
        :return: ``None``
        """
        return self._delete(_iam_role.IAMRole, iam_role_id,
                            ignore_missing=ignore_missing)
