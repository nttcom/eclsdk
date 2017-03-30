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

class ImageCopy(resource2.Resource):
    service = image_service.ImageService()
    base_path ='/' + service.version + '/extension/image_replicator/jobs'

    # Capabilities
    allow_create = True

    # Properties
    #: An identifier job's id for the image copying.
    job_id = resource2.Body('job_id')
    #: source image_id
    source_image_id = resource2.Body('source_image_id')
    #: source region_id
    source_region_id = resource2.Body('source_region_id')
    #: source tenant_id
    source_tenant_id = resource2.Body('source_tenant_id')
    #: destination image_id
    destination_image_id = resource2.Body('destination_image_id')
    #: destination region_id
    destination_region_id = resource2.Body('destination_region_id')
    #: destination tenant_id
    destination_tenant_id = resource2.Body('destination_tenant_id')
    #: job status
    status = resource2.Body('status')
    #: progress of the image copying
    copy_progress = resource2.Body('copy_progress')

    def copy_image(self, session, image_id, tenant_id_dst):
        """Copy image to a specified region."""

        uri = self.base_path
        resp = session.post(
            uri,
            headers={"Content-Type": "application/json"},
            endpoint_filter = self.service,
            json={
                "image_id":image_id,
                "tenant_id_dst":tenant_id_dst
            }
        )
        self._translate_response(resp, has_body=True)
        return self

    def cancel_copy_image(self, session, job_id):
        """Cancel a specified image copy job."""

        uri = self.base_path + '/' + str(job_id)
        resp = session.delete(uri, endpoint_filter = self.service)
        self._translate_response(resp, has_body=False)
        return self

    def list_image_copy_jobs(self, session):
        """Lists details for image copy jobs."""

        uri = self.base_path
        resp = session.get(uri, endpoint_filter = self.service)
        resp = resp.json()
        for data in resp:
            value = self.existing(**data)
            yield value

    def get_image_copy_job(self, session, job_id):
        """Get details for a specified image copy job."""

        uri = self.base_path + '/' + str(job_id)
        resp = session.get(uri, endpoint_filter = self.service)
        self._translate_response(resp, has_body=True)
        return self
