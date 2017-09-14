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

from ecl.network import network_service
from ecl import exceptions
from ecl import resource2

class LoadBalancerPlan(resource2.Resource):
    resource_key = "load_balancer_plan"
    resources_key = "load_balancer_plans"
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + "/load_balancer_plans"

    _query_mapping = resource2.QueryParameters(
        "description", "id", "name",
        "vendor", "version", "enabled",
        "sort_key", "sort_dir",
    )

    # Capabilities
    allow_list = True
    allow_get = True

    # Properties
    #: Description of the Load Balancer Plan.
    description = resource2.Body("description")
    #: Unique ID of the Load Balancer Plan.
    id = resource2.Body("id")
    #: Model of load balancer.
    #: Model.edition of load balancer.
    #: Model.size of load balancer.
    model = resource2.Body("model")
    #: Name of load balancer.
    name = resource2.Body("name")
    #: Vendor of load balancer.
    vendor = resource2.Body("vendor")
    #: Version of load balancer.
    version = resource2.Body("version")
    enabled = resource2.Body("enabled")

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
