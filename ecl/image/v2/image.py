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


from ecl import exceptions
from ecl.image import image_service
from ecl import resource2
from ecl import utils
import json


class Image(resource2.Resource):
    resources_key = 'images'
    service = image_service.ImageService()
    base_path = '/' + service.version + '/images'


    # capabilities
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True
    patch_update = True

    _query_mapping = resource2.QueryParameters(
        "limit", "marker",
        "name", "visibility",
        "member_status", "owner",
        "status", "size_min",
        "size_max", "sort_key",
        "sort_dir", "tag"
    )

    # NOTE: Do not add "self" support here. If you've used Python before,
    # you know that self, while not being a reserved word, has special
    # meaning. You can't call a class initializer with the self name
    # as the first argument and then additionally in kwargs, as we
    # do when we're constructing instances from the JSON body.
    # Resource.list explicitly pops off any "self" keys from bodies so
    # that we don't end up getting the following:
    # TypeError: __init__() got multiple values for argument 'self'

    # The image data (bytes or a file-like object)
    data = None

    # Properties
    #: Descriptive name for the image
    name = resource2.Body('name')
    #: Status of the image
    image_status = resource2.Body('status')
    #: String related to the image
    tags = resource2.Body('tags')
    #: The container format refers to whether the VM image is in a file
    #: format that also contains metadata about the actual VM.
    #: Container formats include OVF and Amazon AMI. In addition,
    #: a VM image might not have a container format - instead,
    #: the image is just a blob of unstructured data.
    container_format = resource2.Body('container_format')
    #: Date and time of image registration
    created_at = resource2.Body('created_at')
    #: Valid values are: aki, ari, ami, raw, iso, vhd, vdi, qcow2, or vmdk.
    #: The disk format of a VM image is the format of the underlying
    #: disk image. Virtual appliance vendors have different formats
    #: for laying out the information contained in a VM disk image.
    disk_format = resource2.Body('disk_format')
    #: Include location_url and location_metadata.
    #: location_url: URL to access the image file kept in external store
    #: (it is shown when 'show_multiple_locations' option is enabled)
    locations = resource2.Body('locations')
    #: The URL to access the image file kept in external store. It appears
    #: when you set the show_image_direct_url option to true in the
    #: Image service's configuration file.
    direct_url = resource2.Body('direct_url')
    #: Date and time of the last image modification.
    updated_at = resource2.Body('updated_at')
    #: The image visibility.
    visibility = resource2.Body('visibility')
    #: Amount of disk space (in GB) required to boot image.
    min_disk = resource2.Body('min_disk')
    #: If true, image will not be deletable.
    protected = resource2.Body('protected')
    #: An identifier for the image.
    id = resource2.Body('id')
    #: URL for the virtual machine image file.
    file = resource2.Body('file')
    #: md5 hash of image contents
    checksum = resource2.Body('checksum')
    #: Owner of the image.
    owner = resource2.Body('owner')
    #: Size of image file in bytes.
    size = resource2.Body('size')
    #: Amount of ram (in MB) required to boot image.
    min_ram = resource2.Body('min_ram')
    #: URL for schema of the virtual machine image.
    image_schema = resource2.Body('image_schema')
    ##: URL for the virtual machine image.
    self = resource2.Body('self')

    #: URL for schema of the virtual machine images.
    images_schema = resource2.Body('images_schema')
    #: URL for the first page of response
    first = resource2.Body('first')

    #: The key of the extra properties.
    extra_key = resource2.Body('extra_key')
    #: The value of the extra properties.
    extra_value = resource2.Body('extra_value')
    #: OS information of this image.
    os_type = resource2.Body('.os.type')
    #: Service information of this image.
    service_type = resource2.Body('.service.type')

    # def _get_image_with_extra_key(self, attr):
    #     image = self.existing(**attr)
    #
    #     for key in attr.keys():
    #         if not hasattr(image, key):
    #             image.__setattr__(key, attr[key])
    #     return image
    #
    # def list(self, session, **query):
    #     """Lists virtual machine (VM) images."""
    #
    #     if query != None:
    #         query_params = self._query_mapping._transpose(query)
    #         uri = self.base_path
    #
    #         params = []
    #         for key in query_params.keys():
    #             item = "%s=%s" % (str(key), str(query_params[key]))
    #             params.append(item)
    #
    #         if len(params) != 0:
    #             uri += '?'
    #             for item in params:
    #                 uri += item + '&'
    #             uri = uri[:-1]
    #
    #     resp = session.get(
    #         uri,
    #         headers={"Accept": "application/json"},
    #         endpoint_filter=self.service
    #     )
    #     resp = resp.json()
    #     images_schema = resp['schema']
    #     first = resp['first']
    #     resp = resp[self.resources_key]
    #
    #     for data in resp:
    #         # Do not allow keys called "self" through. Glance chose
    #         # to name a key "self", so we need to pop it out because
    #         # we can't send it through cls.existing and into the
    #         # Resource initializer. "self" is already the first
    #         # argument and is practically a reserved word.
    #         data.pop("self", None)
    #
    #         image = self._get_image_with_extra_key(data)
    #         image.images_schema = images_schema
    #         image.first = first
    #
    #         yield image

    def get(self, session, image_id):
        """Get a single image's detailed information."""
        url = utils.urljoin(self.base_path, image_id)
        resp = session.get(
            url,
            headers={"Accept": "application/json"},
            endpoint_filter=self.service
        )
        #For extra key/value use.
        self.response = resp.json()
        self._translate_response(resp, has_body=True)
        return self

    def update(self, session, image_id, attrs_list):
        """Updates a specified image."""
        url = utils.urljoin(self.base_path, image_id)
        attrs_list = json.dumps(attrs_list)

        resp = session.patch(url, endpoint_filter=self.service, data=attrs_list, headers={"Content-Type": "application/openstack-images-v2.1-json-patch", "Accept": ""})
        self._translate_response(resp, has_body=True)
        return self

    def upload(self, session, image_id, image_data):
        """Upload data into an existing image"""
        url = utils.urljoin(self.base_path, image_id, 'file')
        resp = session.put(url, endpoint_filter=self.service,
                    data=image_data,
                    headers={"Content-Type": "application/octet-stream",
                             "Accept": "application/json"})
        self._translate_response(resp, has_body=False)
        return self

    def download(self, session, image_id):
        """Download the data contained in an image"""
        # TODO(briancurtin): This method should probably offload the get
        # operation into another thread or something of that nature.
        url = utils.urljoin(self.base_path, image_id, 'file')
        resp = session.get(url, endpoint_filter=self.service)
        return resp.content

    @classmethod
    def find(cls, session, name_or_id, ignore_missing=False, **params):
        """Find a resource by its name or id.

        :param session: The session to use for making this request.
        :type session: :class:`~ecl.session.Session`
        :param name_or_id: This resource's identifier, if needed by
                           the request. The default is ``None``.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :param dict params: Any additional parameters to be passed into
                            underlying methods, such as to
                            :meth:`~ecl.resource2.Resource.existing`
                            in order to pass on URI parameters.

        :return: The :class:`Resource` object matching the given name or id
                 or None if nothing matches.
        :raises: :class:`ecl.exceptions.DuplicateResource` if more
                 than one resource is found for this request.
        :raises: :class:`ecl.exceptions.ResourceNotFound` if nothing
                 is found and ignore_missing is ``False``.
        """
        # Try to short-circuit by looking directly for a matching ID.
        params["limit"] = 10000
        data = cls.list(session, **params)

        result = cls._get_one_match(name_or_id, data)
        if result is not None:
            return result

        if ignore_missing:
            return None
        raise exceptions.ResourceNotFound(
            "No %s found for %s" % (cls.__name__, name_or_id))
