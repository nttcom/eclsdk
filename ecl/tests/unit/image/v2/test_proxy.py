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

import mock

from ecl import exceptions
from ecl.image.v2 import _proxy
from ecl.image.v2 import image
from ecl.image.v2 import member
from ecl.tests.unit import test_proxy_base2


class TestImageProxy(test_proxy_base2.TestProxyBase):
    def setUp(self):
        super(TestImageProxy, self).setUp()
        self.proxy = _proxy.Proxy(self.session)

    def test_image_create_no_args(self):
        # container_format and disk_format are required args
        self.assertRaises(exceptions.InvalidRequest, self.proxy.upload_image)

    def test_image_create(self):
        # NOTE: This doesn't use any of the base class verify methods
        # because it ends up making two separate calls to complete the
        # operation.
        created_image = mock.Mock(spec=image.Image(id="id"))

        self.proxy._create = mock.Mock()
        self.proxy._create.return_value = created_image

        rv = self.proxy.upload_image(data="data", container_format="x",
                                     disk_format="y", name="z")

        self.proxy._create.assert_called_with(image.Image,
                                              container_format="x",
                                              disk_format="y",
                                              name="z")
        created_image.upload.assert_called_with(self.session)
        self.assertEqual(rv, created_image)

    def test_image_delete(self):
        self.verify_delete(self.proxy.delete_image, image.Image, False)

    def test_image_delete_ignore(self):
        self.verify_delete(self.proxy.delete_image, image.Image, True)

    def test_image_update(self):
        self.verify_update(self.proxy.update_image, image.Image)

    def test_image_get(self):
        self.verify_get(self.proxy.get_image, image.Image)

    def test_images(self):
        self.verify_list(list(self.proxy.images), image.Image, paginated=True)

    def test_add_tag(self):
        self._verify("ecl.image.v2.image.Image.add_tag",
                     self.proxy.add_tag,
                     method_args=["image", "tag"],
                     expected_args=["tag"])

    def test_remove_tag(self):
        self._verify("ecl.image.v2.image.Image.remove_tag",
                     self.proxy.remove_tag,
                     method_args=["image", "tag"],
                     expected_args=["tag"])

    def test_member_update(self):
        self._verify2("ecl.proxy2.BaseProxy._update",
                      self.proxy.update_member,
                      method_args=['member_id', 'image_id', 'status'],
                      expected_args=[member.Member],
                      expected_kwargs={'member_id': 'member_id',
                                       'image_id': 'image_id'})

    def test_member_get(self):
        self._verify2("ecl.proxy2.BaseProxy._get",
                      self.proxy.get_member,
                      method_args=['image_id','member'],
                      expected_args=[member.Member, 'member'],
                      expected_kwargs={"image_id":"image_id"})

    def test_members(self):
        self.verify_list(self.proxy.members, member.Member, paginated=False,
                         method_args=('image_1',),
                         expected_kwargs={'image_id': 'image_1'})
