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

from ecl import resource2
from ecl.sss import sss_service


class Token(resource2.Resource):
    resources_key = None
    resource_key = 'token'
    base_path = '/tokens/users'
    service = sss_service.SssAdminService()

    # Capabilities
    allow_create = True

    # Properties
    #: The authentication method.
    methods = resource2.Body('methods')
    #: A user object.
    user = resource2.Body('user')
    #: The date and time when the token was issued.
    issued_at = resource2.Body('issued_at')
    #: The date and time when the token expires.
    expires_at = resource2.Body('expires_at')
    #: A list of audit IDs.
    audit_ids = resource2.Body('audit_ids')
    #: A project object including the id, name and domain object representing
    #: the project the token is scoped to.
    project = resource2.Body('project')
    # Whether a project is acting as a domain.
    is_domain = resource2.Body('is_domain')
    #: A list of role objects.
    roles = resource2.Body('roles')
    #: A catalog object.
    catalog = resource2.Body('catalog')
    #: The authentication token. An authentication response returns
    #: the token ID in this header rather than in the response body.
    subject_token = resource2.Header('X-Subject-Token')

    def get_user_token_by_admin(self, session, user_id,
                                tenant_id=None, no_catalog=True):
        """Obtain a user token by SSS on behalf

        :param session: The session to use for making this request.
        :type session: :class:`~ecl.session.Session`
        :param user_id: ID of a user
        :param tenant_id: ID of a tenant
        :param bool no_catalog: Exclude the service catalog from the response.
        :return: :class:`~ecl.sss.v2.token.Token`
        """
        url = '%s/%s' % (self.base_path, user_id)
        if no_catalog:
            url += '?nocatalog=true'
        body = {"tenant_id": tenant_id} if tenant_id else {}

        resp = session.post(url, endpoint_filter=self.service, json=body)
        self._translate_response(resp, has_body=True)
        return self
