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

import testtools

from ecl.sss.v2 import service_menu

CATEGORIES_EXAMPLE = [
    {
        "category_name": "menu.category.test1",
        "sub_categories": [
            {
                "sub_category_name": "menu.subcategory.test1",
                "service_menus": [
                    {
                        "menu_name": "sss.menu.test1",
                        "areas": [
                            {"region_name": "lab3ec"},
                            {"region_name": "lab4ec"},
                            {"region_name": "lab5ec"}
                        ]
                    }
                ]
            }
        ]
    }
]

USER_SERVICE_MENU_EXAMPLE = {
    'user_id': 'user1234567890',
    'categories': CATEGORIES_EXAMPLE
}


class TestServiceMenu(testtools.TestCase):

    def test_service_menu(self):
        sot = service_menu.ServiceMenu()
        self.assertEqual(None, sot.resources_key, message='resouces_key')
        self.assertEqual(None, sot.resource_key, message='resource_key')
        self.assertEqual('', sot.base_path, message='base_path')
        self.assertEqual('sssv2', sot.service.service_type,
                         message='service_type')

        self.assertFalse(sot.allow_create, msg='allow_create')
        self.assertFalse(sot.allow_get, msg='allow_get')
        self.assertFalse(sot.allow_update, msg='allow_update')
        self.assertFalse(sot.allow_delete, msg='allow_delete')
        self.assertFalse(sot.allow_list, msg='allow_list')
        self.assertFalse(sot.allow_head, msg='allow_head')
        self.assertFalse(sot.patch_update, msg='patch_update')
        self.assertFalse(sot.put_create, msg='put_create')

    def test_make_user_service_menu(self):
        sot = service_menu.ServiceMenu(**USER_SERVICE_MENU_EXAMPLE)
        self.assertEqual(USER_SERVICE_MENU_EXAMPLE['user_id'], sot.user_id)
        self.assertEqual(CATEGORIES_EXAMPLE, sot.categories)
