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

from ecl.image import image_service
from ecl import resource2

class Tag(resource2.Resource):
    service = image_service.ImageService()
    base_path = '/' + service.version + '/images/%(image_id)s/tags/%(tag)s'

    def add_tag(self, session, image_id, tag):
        """Adds a specified tag to a specified image."""
        uri = self.base_path % {"image_id":image_id, "tag":tag}
        session.put(uri, endpoint_filter=self.service)

    def delete_tag(self, session, image_id, tag):
        """Delete a specified tag from a specified image"""
        uri = self.base_path % {"image_id": image_id, "tag": tag}
        session.delete(uri, endpoint_filter=self.service)
