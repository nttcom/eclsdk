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

from ecl.dns import dns_service
from ecl import resource2
from ecl import exceptions


class Zone(resource2.Resource):
    resource_key = None
    resources_key = "zones"
    base_path = '/v2/zones'
    service = dns_service.DnsService()

    # Capabilities
    allow_create = True
    allow_delete = True
    allow_update = True
    allow_list = True
    allow_get = True
    patch_update = True

    # Properties
    #: ID for the resource
    id = resource2.Body('id')
    #: ID for the pool hosting this zone. This parameter is not currently supported. It always returns an empty string.
    pool_id = resource2.Body('pool_id')
    #: ID for the project(tenant) that owns the resource.
    project_id = resource2.Body('project_id')
    #: DNS Name for the zone
    name = resource2.Body('name')
    #: e-mail for the zone. Used in SOA records for the zone. This parameter is not currently supported.
    #: It always returns an empty string.
    email = resource2.Body('email')
    #: TTL (Time to Live) for the zone. This parameter is not currently supported. it always return zero.
    ttl = resource2.Body('ttl')
    #: current serial number for the zone. This parameter is not currently supported. it always return zero.
    serial = resource2.Body('serial')
    #: status of the resource.
    status = resource2.Body('status')
    #: Description for this zone.
    description = resource2.Body('description')
    #: For secondary zones. The servers to slave from to get DNS information. This parameter is not currently supported.
    #: It always returns an empty string.
    masters = resource2.Body('masters')
    #: Type of zone. PRIMARY is controlled by ECL2.0 DNS, SECONDARY zones are slaved from another DNS Server.
    #: Defaults to PRIMARY. This parameter is not currently supported. It always returns an empty string.
    type = resource2.Body('type')
    #: For secondary zones. The last time an update was retrieved from the master servers.
    #: This parameter is not currently supported. it always return null.
    transferred_at = resource2.Body('transferred_at')
    #: Version of the resource. This parameter is not currently supported. it always return 1.
    version = resource2.Body('version')
    #: Date / Time when resource was created.
    created_at = resource2.Body('created_at')
    #: Date / Time when resource last updated.
    updated_at = resource2.Body('updated_at')
    #: Links to the resource, and other related resources. When a response has been broken into pages,
    #: we will include a next link that should be followed to retrive all results.
    links = resource2.Body('links')


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

        data = cls.list(session, **params)

        result = cls._get_one_match(name_or_id, data)
        if result is not None:
            return result

        if ignore_missing:
            return None
        raise exceptions.ResourceNotFound(
            "No %s found for %s" % (cls.__name__, name_or_id))
