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

from ecl.image.v2 import image as _image
from ecl.image.v2 import image_copy as _copy
from ecl.image.v2 import member as _member
from ecl.image.v2 import license as _license
from ecl.image.v2 import tag as _tag
from ecl.image.v2 import schema as _schema
from ecl import proxy2
from ecl import resource2


class Proxy(proxy2.BaseProxy):

    def create_image(self, **attrs):
        """Creates a virtual machine (VM) image.

        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~ecl.image.v2.image.Image`,
                           comprised of the properties on the Image class.

        :returns: The results of image creation
        :rtype: :class:`~ecl.image.v2.image.Image`
        """
        img = self._create(_image.Image, **attrs)
        return img

    def upload_image(self, image_id, image_data):
        """
        Uploads binary image data.

        :param image_id: An identifier for the image.
        :param image_data: raw binary data that represents the actual virtual disk.
        :return: ``None``
        """
        img = _image.Image()
        return img.upload(self.session, image_id, image_data)

    def download_image(self, image_id):
        """Download an image

        :param image: The value can be either the ID of an image or a
                      :class:`~ecl.image.v2.image.Image` instance.

        :returns: The bytes comprising the given Image.
        """
        img = _image.Image()
        return img.download(self.session, image_id)

    def delete_image(self, image, ignore_missing=False):
        """Delete an image

        :param image: The value can be either the ID of an image or a
                      :class:`~ecl.image.v2.image.Image` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the image does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent image.

        :returns: ``None``
        """
        self._delete(_image.Image, image, ignore_missing=ignore_missing)

    def find_image(self, name_or_id, ignore_missing=False):
        """Find a single image

        :param name_or_id: The name or ID of a image.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.image.v2.image.Image` or None
        """

        return self._find(_image.Image, name_or_id,
                          ignore_missing=ignore_missing)

    def get_image(self, image):
        """Get a single image

        :param image: The value can be the ID of a image or a
                      :class:`~ecl.image.v2.image.Image` instance.

        :returns: One :class:`~ecl.image.v2.image.Image`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        img = _image.Image()
        return img.get(self.session, image)

    def images(self, **query):
        """Return a generator of images

        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.

        :returns: A generator of image objects
        :rtype: :class:`~ecl.image.v2.image.Image`
        """
        if 'limit' not in query.keys():
            query["limit"] = 1000
        return list(self._list(_image.Image, **query))

    def update_image(self, image_id, image_data):
        """
        Update a image.

        :param image_id: ID of a image.
        :param image_data: List of attributes(dict) to update on the image.
        :return: :class:`~ecl.image.v2.image.Image`
        """
        img = _image.Image()
        return img.update(self.session, image_id, image_data)

    def copy_image(self, image_id, tenant_id_dst):
        """
        Copy image to a specified region.

        :param image_id: An identifier for the image.
        :param tenant_id_dst: An identifier for the image tenant for destination region.
        :return: :class:`~ecl.image.v2.image_copy.ImageCopy`
        """
        copy = _copy.ImageCopy()
        return copy.copy_image(self.session, image_id, tenant_id_dst)

    def cancel_copy_image(self, job_id):
        """
        Lists details for image copy jobs.

        :param job_id: JOB_ID that has been paid out in the Copy API.
        :return: ``None``
        """
        copy = _copy.ImageCopy()
        return copy.cancel_copy_image(self.session, job_id)

    def list_image_copy_jobs(self):
        """
        Lists details for image copy jobs.

        :return: A generator of ImageCopy instances.
        :rtype: :class:`~ecl.image.v2.image_copy.ImageCopy`
        """
        copy = _copy.ImageCopy()
        return copy.list_image_copy_jobs(self.session)

    def get_image_copy_job(self, job_id):
        """
        Get details for a specified image copy job.

        :param job_id: JOB_ID that has been paid out in the Copy API.
        :return: :class:`~ecl.image.v2.image_copy.ImageCopy`
        """
        copy = _copy.ImageCopy()
        return copy.get_image_copy_job(self.session, job_id)

    def add_tag(self, image, tag):
        """Add a tag to an image

        :param image: The value can be the ID of a image or a
                      :class:`~ecl.image.v2.image.Image` instance
                      that the member will be created for.
        :param str tag: The tag to be added

        :returns: None
        """
        image = self._get_resource(_image.Image, image)
        image.add_tag(self.session, tag)

    def remove_tag(self, image, tag):
        """Remove a tag to an image

        :param image: The value can be the ID of a image or a
                      :class:`~ecl.image.v2.image.Image` instance
                      that the member will be created for.
        :param str tag: The tag to be removed

        :returns: None
        """
        image = self._get_resource(_image.Image, image)
        image.remove_tag(self.session, tag)

    def create_member(self, image, **attrs):
        """Create a new member from attributes

        :param image: The value can be the ID of a image or a
                      :class:`~ecl.image.v2.image.Image` instance
                      that the member will be created for.
        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~ecl.image.v2.member.Member`,
                           comprised of the properties on the Member class.

        :returns: The results of member creation
        :rtype: :class:`~ecl.image.v2.member.Member`
        """
        image_id = resource2.Resource._get_id(image)
        return self._create(_member.Member, image_id=image_id, **attrs)

    def delete_member(self, image, member, ignore_missing=False):
        """Delete a member

        :param member: The value can be either the ID of a member or a
                       :class:`~ecl.image.v2.member.Member` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the member does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent member.

        :returns: ``None``
        """
        image_id = resource2.Resource._get_id(image)
        member_id = resource2.Resource._get_id(member)
        self._delete(_member.Member, member_id, image_id=image_id,
                     ignore_missing=ignore_missing)

    def get_member(self, image, member):
        """Get a single member on an image

        :param member: The value can be the ID of a member or a
                       :class:`~ecl.image.v2.member.Member` instance.
        :param image: This is the image that the member belongs to.
                      The value can be the ID of a image or a
                      :class:`~ecl.image.v2.image.Image` instance.
        :returns: One :class:`~ecl.image.v2.member.Member`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        member_id = resource2.Resource._get_id(member)
        image_id = resource2.Resource._get_id(image)
        return self._get(_member.Member, member_id, image_id=image_id)

    def members(self, image):
        """Return a generator of members

        :param image: This is the image that the member belongs to,
                      the value can be the ID of a image or a
                      :class:`~ecl.image.v2.image.Image` instance.

        :returns: A generator of member objects
        :rtype: :class:`~ecl.image.v2.member.Member`
        """
        image_id = resource2.Resource._get_id(image)
        return self._list(_member.Member, paginated=False,
                          image_id=image_id)

    def update_member(self, image_id, member_id, status):
        """
        Update the member of an image.

        :param image_id: ID of a member.
        :param member_id: ID of the image that the member belongs to.
        :param status: The status of this image member.
        :returns: The updated member
        :rtype: :class:`~ecl.image.v2.member.Member`
        """
        member = _member.Member()
        return member.update(self.session, image_id, member_id, status)

    def licenses(self):
        """
        List image license switch types.

        :returns: A generator of license objects
        :rtype: :class:`~ecl.image.v2.license.License`
        """
        license = _license.License()
        return license.list(self.session)

    def add_tag(self, image_id, tag_to_add):
        """
        Adds a specified tag to a specified image.

        :param image_id: Image ID stored through the image API.
                        Typically a UUID.
        :param tag: Image tag to add.
        :return: ``None``
        """
        tag = _tag.Tag()
        return tag.add_tag(self.session, image_id, tag_to_add)

    def delete_tag(self, image_id, tag_to_delete):
        """
        Deletes a specified tag from a specified image.

        :param image_id: Image ID stored through the image API.
                        Typically a UUID.
        :param tag_to_delete: Image tag to delete.
        :return: ``None``
        """
        tag = _tag.Tag()
        return tag.delete_tag(self.session, image_id, tag_to_delete)

    def get_image_schema(self):
        """
        Gets a JSON schema document that represents an image entity.

        :return: :class:`~ecl.image.v2.scheme.Scheme`
        """
        schema = _schema.Scheme()
        return schema.get_image_schema(self.session)

    def get_images_schema(self):
        """
        Gets a JSON schema document that represents an images entity.

        :return: :class:`~ecl.image.v2.scheme.Scheme`
        """
        schema = _schema.Scheme()
        return schema.get_images_schema(self.session)

    def get_image_member_schema(self):
        """
        Gets a JSON schema document that represents an image member
        entity.

        :return: :class:`~ecl.image.v2.scheme.Scheme`
        """
        schema = _schema.Scheme()
        return schema.get_image_member_schema(self.session)

    def get_metadata_namespace_schema(self):
        """
        Gets a JSON schema document that represents a metadata
        definition namespace entity.

        :return: :class:`~ecl.image.v2.scheme.Scheme`
        """
        schema = _schema.Scheme()
        return schema.get_metadata_namespace_schema(self.session)

    def get_metadata_object_schema(self):
        """
        Gets a JSON schema document that represents a metadata
        definition object entity.

        :return: :class:`~ecl.image.v2.scheme.Scheme`
        """
        schema = _schema.Scheme()
        return schema.get_metadata_object_schema(self.session)

    def get_metadata_property_schema(self):
        """
        Gets a JSON schema document that represents a metadata
        definition property entity.

        :return: :class:`~ecl.image.v2.scheme.Scheme`
        """
        schema = _schema.Scheme()
        return schema.get_metadata_property_schema(self.session)

    def get_metadata_resource_type_schema(self):
        """
        Gets a JSON schema document that represents a metadata
        definition namespace resource type association entity.

        :return: :class:`~ecl.image.v2.scheme.Scheme`
        """
        schema = _schema.Scheme()
        return schema.get_metadata_resource_type_schema(self.session)
