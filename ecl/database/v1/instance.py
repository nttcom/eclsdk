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

from ecl.database import database_service

from ecl import exceptions
from ecl import resource2
from ecl import utils


class Instance(resource2.Resource):
    resource_key = 'instance'
    resources_key = 'instances'
    base_path = '/instances'
    service = database_service.DatabaseService()

    # capabilities
    allow_create = True
    allow_get = True
    allow_delete = True
    allow_list = True

    allow_update = False

    _query_mapping = resource2.QueryParameters()

    #: ID of the server
    id = resource2.Body('id')

    #: Timestamp of when the instance was created.
    created_at = resource2.Body('created')

    #: The datastore property returned as instence property.
    datastore = resource2.Body('datastore', type=dict)

    #: The flavor property returned from instance.
    flavor = resource2.Body('flavor', type=dict)

    #: The flavor reference, as a ID or full URL,
    #: in case create instane.
    flavor_id = resource2.Body('flavorRef')

    #: An ID representing the host of this instance.
    hostname = resource2.Body('hostname')

    #: A list of dictionaries holding links relevant to this instance.
    links = resource2.Body('links', type=list)

    #: Name of the instance
    name = resource2.Body('name')

    #: Region of the instance
    region = resource2.Body('region')

    #: The state this instance is in.
    status = resource2.Body('status')

    #: Timestamp of when this instance was last updated.
    updated_at = resource2.Body('updated')

    #: The volume property returned from instance.
    volume = resource2.Body('volume', type=dict)

    #: A nic definition object. Required parameter when there are multiple
    #: networks defined for the tenant.
    nics = resource2.Body('nics', type=dict)

    #: Databases list of instance.
    databases = resource2.Body('databases', type=list)

    #: Users list of instance.
    users = resource2.Body('users', type=list)

    #: Backup window of instance.
    backup_window = resource2.Body('backup_window')

    #: Maintenance window of instance.
    maintenance_window = resource2.Body('maintenance_window')

    #: Backup retension period of this instance.
    backup_retention_period = resource2.Body('backup_retention_period',
                                             type=int)

    #: Restore Point
    restore_point = resource2.Body('restorePoint', type=dict)

    #: Restoreable Time
    restorable_time = resource2.Body('restorable_time')

    #: Endpoints
    endpoints = resource2.Body('endpoints', type=list)

    #: Availability Zone
    availability_zone = resource2.Body('availability_zone')

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
