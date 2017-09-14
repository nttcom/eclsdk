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

from ecl.baremetal import baremetal_service
from ecl import exceptions
from ecl import resource2


class Flavor(resource2.Resource):
    resource_key = 'flavor'
    resources_key = 'flavors'
    base_path = '/flavors'
    service = baremetal_service.BaremetalService()

    # Capabilities
    allow_get = True
    allow_list = True

    # Properties
    #: The ID for the flavor, which is a unique integer value.
    id = resource2.Body('id')
    #: List of flavor resource links.
    links = resource2.Body('links')
    #: The amount of RAM, in MBs, for this flavor.
    ram = resource2.Body('ram', type=int)
    #: Name for the flavor.
    name = resource2.Body('name')
    #: The amount of disk space, in GBs.
    disk = resource2.Body('disk', type=int)
    #: The CPUs, in whole integer amount, for the flavor.
    #: In order to maintain compatibility with Nova API,
    #: we put the size of the physical cpu to vcpu.
    vcpus = resource2.Body('vcpus', type=int)

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


class FlavorDetail(Flavor):
    base_path = '/flavors/detail'

    allow_get = False
