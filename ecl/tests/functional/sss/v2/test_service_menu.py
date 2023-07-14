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

import os
import unittest

import six

import ecl
from ecl.tests.functional import base


class TestServiceMenu(base.BaseFunctionalTest):
    """Test ServiceMenu resources

    To run this test, you will need.
    - Prior Smart Data Platform login
    - Administrator account
    """
    @classmethod
    def setUpClass(cls):
        # keystone admin endpoint URL
        admin_keystone_url = os.getenv('ADMIN_KEYSTONE_URL')
        # adminstrator account
        admin_username = os.getenv('ADMIN_USER_NAME')
        admin_password = os.getenv('ADMIN_PASSWORD')
        # user information
        cls.user_ecid = os.getenv('USER_ECID')

        cls.conn = ecl.connection.Connection(auth_url=admin_keystone_url,
                                             username=admin_username,
                                             password=admin_password,
                                             user_domain_id='default',
                                             timeout=100)

    @unittest.skip("Skip as it requires administrator authorization.")
    def test_get_user_service_menu(self):
        service_menu = self.conn.sss.get_user_service_menu(self.user_ecid)
        self.assertIsInstance(service_menu.user_id, six.string_types)
        self.assertIsInstance(service_menu.categories, list)

    @unittest.skip("Skip as it requires administrator authorization.")
    def test_categories_in_service_menu(self):
        service_menu = self.conn.sss.get_user_service_menu(self.user_ecid)
        for category in service_menu.categories:
            self._check_category(category)
            sub_categories = category.get('sub_categories')

            for sub_category in sub_categories:
                self._check_sub_category(sub_category)
                service_menus = sub_category.get('service_menus')

                for service_menu in service_menus:
                    self._check_service_menu(service_menu)

    def _check_category(self, category):
        self.assertIsInstance(category, dict)
        self.assertIsInstance(category.get('category_name'),
                              six.string_types)
        self.assertIsInstance(category.get('sub_categories'), list)

    def _check_sub_category(self, sub_category):
        self.assertIsInstance(sub_category, dict)
        self.assertIsInstance(sub_category.get('sub_category_name'),
                              six.string_types)
        self.assertIsInstance(sub_category.get('service_menus'), list)

    def _check_service_menu(self, service_menu):
        self.assertIsInstance(service_menu, dict)
        self.assertIsInstance(service_menu.get('menu_name'), six.string_types)
        areas = service_menu.get('areas')
        self.assertIsInstance(areas, list)
        for area in areas:
            self.assertIsInstance(area, dict)
            self.assertIn('area_name', area)
            self.assertIn('region_name', area)
