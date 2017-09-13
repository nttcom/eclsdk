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

from ecl.sss import sss_service
from ecl import resource2
from ecl import exceptions
from ecl import utils

class User(resource2.Resource):
    resource_key = None
    resources_key = 'users'
    base_path = '/users'
    service = sss_service.SssService()

    # Capabilities
    allow_create = True
    allow_get = True
    allow_delete = True
    allow_list = True
    allow_update = True
    put_create = False

    # Properties
    #: login id of the user. When this contract is tied with icp, this
    #: parameter is fixed {email}_{user_id}.
    login_id = resource2.Body('login_id')
    #: Mail address of the user.
    mail_address = resource2.Body('mail_address')
    #: User id. format is ecid[0-9]{10}.
    user_id = resource2.Body('user_id', alternate_id=True)
    #: If this user is the Super user in this contract, 1. If not, 0.
    contract_owner = resource2.Body('contract_owner')
    #: Contract ID which this user belongs. contract id format is econ[0-9]{10}.
    contract_id = resource2.Body('contract_id')
    #: This user's API key for keystone authentication.
    keystone_name = resource2.Body('keystone_name')
    #: Keystone address this user can use to get token for SSS API request.
    keystone_endpoint = resource2.Body('keystone_endpoint')
    #: This user's API secret for keystone authentication.
    keystone_password = resource2.Body('keystone_password')
    #: SSS endpoint recommended for this user
    sss_endpoint = resource2.Body('sss_endpoint')
    #: Password of the user
    password = resource2.Body('password')
    #: If this flag is set 'true', notification eamil will be sent to new
    #: user's email.
    notify_password = resource2.Body('notify_password')
    #: New password of the user
    new_password = resource2.Body('new_password')
    #: User list.
    users = resource2.Body('users')
    #: If this user's contract is tied with NTT Communications business portal,
    #: 'icp' is shown.
    login_integration = resource2.Body('login_integration')
    #: External system oriented contract id. If this user's contract is NTT
    #: Communications, customer number with 15 numbers will be shown.
    external_reference_id = resource2.Body('external_reference_id')

    def update(self, session, user_id, **attrs):
        """Update user's information"""

        uri = utils.urljoin(self.base_path, user_id)
        resp = session.put(
            uri, endpoint_filter=self.service,
            json=attrs
        )
        self._translate_response(resp, has_body=False)
        return self

    @classmethod
    def find(cls, session, name_or_id, ignore_missing=False, **params):
        """Find a resource by its name or id.

        :param session: The session to use for making this request.
        :type session: :class:`~ecl.session.Session`
        :param name_or_id: This resource's identifier, if needed by
                           the request. The default is ``None``.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :param dict params: Any additional parameters to be passed into
                            underlying methods, such as to
                            :meth:`~ecl.resource2.Resource.existing`
                            in order to pass on URI parameters.

        :return: The :class:`Resource` object matching the given name or id
                 or None if nothing matches.
        :raises: :class:`ecl.exceptions.DuplicateResource` if more
                 than one resource is found for this request.
        :raises: :class:`ecl.exceptions.ResourceNotFound` if nothing
                 is found and ignore_missing is ``False``.
        """
        # Try to short-circuit by looking directly for a matching ID.

        data = cls.list(session, **params)

        result = cls._get_one_match(name_or_id, data)
        if result is not None:
            return result

        if ignore_missing:
            return None
        raise exceptions.ResourceNotFound(
            "No %s found for %s" % (cls.__name__, name_or_id))
