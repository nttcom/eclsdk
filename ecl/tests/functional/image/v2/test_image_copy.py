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

import six
from ecl.tests.functional import base


class TestImageCopy(base.BaseFunctionalTest):
    image_id = "4ddf938a-2cff-46a8-ab7b-efb48c8f79a7"

    @classmethod
    def test_01_copy_image(cls):
        copy = cls.conn.image.copy_image(
            cls.image_id, "72ab9350a47a4173966ad02dc51b32a1")
        print(copy)
        cls.job_id = copy.job_id
        assert isinstance(copy.job_id, six.string_types)

    def test_02_list_image_copy_jobs(self):
        jobs = list(self.conn.image.list_image_copy_jobs())
        for job in jobs:
            self.assertIsInstance(job.source_image_id, six.string_types)
            self.assertIsInstance(job.source_region_id, six.string_types)
            self.assertIsInstance(job.source_tenant_id, six.string_types)
            self.assertIsInstance(job.destination_image_id, six.string_types)
            self.assertIsInstance(job.destination_region_id, six.string_types)
            self.assertIsInstance(job.destination_tenant_id, six.string_types)
            self.assertIsInstance(job.status, six.string_types)
            self.assertIsInstance(job.copy_progress, int)
        print(jobs)

    def test_03_get_image_copy_job(self):
        job = self.conn.image.get_image_copy_job(
            "c02103c2-3b6e-4f5e-9be9-7f6a8d18da26"
        )
        self.assertIsInstance(job.source_image_id, six.string_types)
        self.assertIsInstance(job.source_region_id, six.string_types)
        self.assertIsInstance(job.source_tenant_id, six.string_types)
        self.assertIsInstance(job.destination_image_id, six.string_types)
        self.assertIsInstance(job.destination_region_id, six.string_types)
        self.assertIsInstance(job.destination_tenant_id, six.string_types)
        self.assertIsInstance(job.status, six.string_types)
        self.assertIsInstance(job.copy_progress, int)
        print(job)

    def test_04_cancel_copy_image(self):
        copy = self.conn.image.cancel_copy_image(
            "c02103c2-3b6e-4f5e-9be9-7f6a8d18da26"
        )
        print(copy)
