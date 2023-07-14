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


class ServiceMenu(resource2.Resource):
    service = sss_service.SssAdminService()

    # Properties
    #: User id. format is ecid[0-9]{10}.
    user_id = resource2.Body('user_id')
    #: Category information of service menu
    categories = resource2.Body('categories')

    def get_user_service_menu(self, session, user_id):
        """Get menu of services available to user.

        :param session: The session to use for making this request.
        :param user_id: ID of a user
        :return: :class:`~ecl.sss.v2.service_menu.ServiceMenu`
        """
        url = '/users/%s/service-menus' % user_id
        resp = session.get(url, endpoint_filter=self.service)
        self._translate_response(resp, has_body=True)
        return self
