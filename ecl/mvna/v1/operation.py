# -*- coding: utf-8 -*-

from ecl import resource2
from ecl.mvna import mvna_service

class Operation(resource2.Resource):
    resource_key = "operation"
    resources_key = "operations"
    service = mvna_service.MVNAService("v1.0")
    base_path = '/' + service.version + '/operations'

    _query_mapping = resource2.QueryParameters(
        "id",
        "resource_id",
        "resource_type",
        "request_id",
        "request_type",
        "status",
        "tenant_id",
        "no_deleted",
        "latest"
    )

    # Capabilities
    allow_list = True
    allow_get = True

    # Properties
    #: ID of network appliance's operation
    id = resource2.Body('id')
    #: Target load balancer id of operation.
    resource_id = resource2.Body('resource_id')
    #: resource type of operation.
    resource_type = resource2.Body('resource_type')
    #: Request ID of operation.
    request_id = resource2.Body('request_id')
    #: A string representation of the request type.
    request_types = resource2.Body('request_types')
    #: Request body(JSON String) of operation.
    request_body = resource2.Body('request_body')
    #: Status of operation.
    status = resource2.Body('status')
    #: Reception datetime of operation.
    reception_datetime = resource2.Body('reception_datetime')
    #: Commit datetime of operation.
    commit_datetime = resource2.Body('commit_datetime')
    #: Warning of operation.
    warning = resource2.Body('warning')
    #: Error of operation.
    error = resource2.Body('error')
    #: Tenant ID of operation.
    tenant_id = resource2.Body('tenant_id')

    @classmethod
    def list(cls, session, paginated=False, no_deleted=True, latest=False):
        """This method is a generator which yields operation objects.

        This resource object list generator handles pagination and takes query
        params for response filtering.

        :param session: The session to use for making this request.
        :type session: :class:`~ecl.session.Session`
        :param bool paginated: ``True`` if a GET to this resource returns
            a paginated series of responses, or ``False``
            if a GET returns only one page of data.
            **When paginated is False only one
            page of data will be returned regardless
            of the API's support of pagination.**
        :param bool no_deleted:
            ``True`` You can get operations for only existing resources.
            ``False`` You can get operations for all resources even removed.
        :param bool latest:
            ``True`` You can get only the latest operations for each resource.
            ``False`` You can get all of operations for each resource.
        :return: A generator of :class:`Operation` objects.
        :raises: :exc:`~ecl.exceptions.MethodNotSupported` if
                 :data:`Resource.allow_list` is not set to ``True``.
        """
        more_data = True

        uri = \
            cls.base_path + \
            '?no_deleted=%s&latest=%s' % (str(no_deleted).lower(),
                                          str(latest).lower())

        while more_data:
            resp = session.get(uri, endpoint_filter=cls.service,
                               headers={"Accept": "application/json"})
            resp = resp.json()
            if cls.resources_key:
                resp = resp[cls.resources_key]

            if not resp:
                more_data = False

            # Keep track of how many items we've yielded. If we yielded
            # less than our limit, we don't need to do an extra request
            # to get back an empty data set, which acts as a sentinel.
            yielded = 0
            for data in resp:
                # Do not allow keys called "self" through. Glance chose
                # to name a key "self", so we need to pop it out because
                # we can't send it through cls.existing and into the
                # Resource initializer. "self" is already the first
                # argument and is practically a reserved word.
                data.pop("self", None)

                value = cls.existing(**data)
                yielded += 1
                yield value

            if not paginated:
                return
