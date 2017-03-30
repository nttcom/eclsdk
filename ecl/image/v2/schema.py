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

class Scheme(resource2.Resource):
    service = image_service.ImageService()
    base_path = '/' + service.version + '/schemas'

    # Properties
    #: Image's additionalProperties.
    additionalProperties = resource2.Body('additionalProperties')
    #: Image's links.
    links = resource2.Body('links')
    #: Image's name.
    name = resource2.Body('name')
    #: Properties for image.
    #: Properties list:
    #: architecture: Operating system architecture as specified in URL.
    #: status: The image status.
    #: container_format: The container format of image.
    #: min_ram: The minimum amount of RAM in MB that is required to boot the image..
    #: updated_at: The date and time when the resource was updated.The date and time stamp format is ISO 8601.
    #: owner: The ID of the owner, or tenant, of the image.
    #: min_disk: The minimum disk size in GB that is required to boot the image.
    #: tags: A list of Image tag.
    #: visibility: The image visibility.
    #: id: The unique ID for the image.
    #: size: The size of the image data, in bytes.
    #: virtual_size: The virtual size of the image.
    #: name: The name of the image.
    #: checksum: Hash of the image data used. The Image service uses this value for verification.
    #: created_at: The date and time when the resource was created.The date and time stamp format is ISO 8601.
    #: disk_format: The disk format of the image.
    #: properties: Properties, if any, that are associated with the image.
    #: protected: Indicates whether the image can be deleted.
    #: location: URL to access the image file kept in external store.
    #: self: URL for the virtual machine image.
    #: schema: URL for schema of the virtual machine image/member.
    #: direct_url: URL to access the image file kept in external store.
    #: instance_uuid: ID of instance used to create this image.
    #: kernel_id: ID of image stored in Glance that should be used as the kernel when booting an AMI-style image.
    #: os_distro: Common name of operating system distribution as specified in URL.
    #: os_version: Operating system version as specified by the distributor.
    #: ramdisk_id: ID of image stored in Glance that should be used as the ramdisk when booting an AMI-style image.
    #: member_id: Image member ID. For example, the tenant ID of the user with whom the image is being shared.
    properties = resource2.Body('properties')
    #: Metadata's definition.
    definitions = resource2.Body('definitions')

    def get_image_schema(self, session):
        """Gets a JSON schema document that represents an image
        entity."""

        uri = self.base_path + '/image'
        resp = session.get(
            uri,
            headers={"Accept": "application/json"},
            endpoint_filter=self.service
        )
        self._translate_response(resp, has_body=True)
        return self

    def get_images_schema(self, session):
        """Gets a JSON schema document that represents an images
        entity."""

        uri = self.base_path + '/images'
        resp = session.get(
            uri,
            headers={"Accept": "application/json"},
            endpoint_filter=self.service
        )
        self._translate_response(resp, has_body=True)
        return self

    def get_image_member_schema(self, session):
        """Gets a JSON schema document that represents an image member
        entity."""

        uri = self.base_path + '/member'
        resp = session.get(
            uri,
            headers={"Accept": "application/json"},
            endpoint_filter=self.service
        )
        self._translate_response(resp, has_body=True)
        return self

    def get_metadata_namespace_schema(self, session):
        """Gets a JSON schema document that represents a metadata
        definition namespace entity."""

        uri = self.base_path + '/metadefs/namespace'
        resp = session.get(
            uri,
            headers={"Accept": "application/json"},
            endpoint_filter=self.service
        )
        self._translate_response(resp, has_body=True)
        return self

    def get_metadata_object_schema(self, session):
        """Gets a JSON schema document that represents a metadata
        definition object entity."""

        uri = self.base_path + '/metadefs/object'
        resp = session.get(
            uri,
            headers={"Accept": "application/json"},
            endpoint_filter=self.service
        )
        self._translate_response(resp, has_body=True)
        return self

    def get_metadata_property_schema(self, session):
        """Gets a JSON schema document that represents a metadata
        definition property entity."""

        uri = self.base_path + '/metadefs/property'
        resp = session.get(
            uri,
            headers={"Accept": "application/json"},
            endpoint_filter=self.service
        )
        self._translate_response(resp, has_body=True)
        return self

    def get_metadata_resource_type_schema(self, session):
        """Gets a JSON schema document that represents a metadata definition namespace resource type association entity."""

        uri = self.base_path + '/metadefs/resource_type'
        resp = session.get(
            uri,
            headers={"Accept": "application/json"},
            endpoint_filter=self.service
        )
        self._translate_response(resp, has_body=True)
        return self