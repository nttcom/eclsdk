# -*- coding: utf-8 -*-

from ecl.compute import compute_service
from ecl import resource2


class ServerAction(resource2.Resource):
    resource_key = 'instanceAction'
    resources_key = 'instanceActions'
    base_path = '/servers/%(instance_uuid)s/os-instance-actions'
    service = compute_service.ComputeService()

    # capabilities
    allow_list = True
    allow_get = True

    # Properties
    #: action instance
    action = resource2.Body('action')
    #: The ID for the server.
    instance_uuid = resource2.URI('instance_uuid')
    #: Message of action
    message = resource2.Body('message')
    #: 	project id
    project_id = resource2.Body('project_id')
    #: request id
    request_id = resource2.Body('request_id', alternate_id=True)
    #: start time of an action
    start_time = resource2.Body('start_time')
    #: owner of the instance
    user_id = resource2.Body('user_id')
