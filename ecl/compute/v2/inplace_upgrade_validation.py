# -*- coding: utf-8 -*-

from ecl.compute import compute_service
from ecl import exceptions
from ecl import resource2


class InplaceUpgradeValidation(resource2.Resource):
    resource_key = 'inplace_upgrade_validation'
    base_path = '/servers/%(server_id)s/inplace_upgrades/validation'
    service = compute_service.ComputeService()

    # capabilities
    allow_create = False
    allow_get = True
    allow_delete = False
    allow_list = False
    allow_update = False

    server_id = resource2.URI("server_id")
    instance_id = resource2.Body("instance_id")
    validation = resource2.Body("validation")
    upgradable_targets = resource2.Body("upgradable_targets")

    def get(self, session, requires_id=False):
        if not self.allow_get:
            raise exceptions.MethodNotSupported(self, "get")

        request = self._prepare_request(requires_id=False)
        response = session.get(request.uri, endpoint_filter=self.service)

        self._translate_get_response(response)
        return self

    def _translate_get_response(self, response, has_body=True):
        if has_body:
            body = response.json()
            body = self._filter_component(body, self._body_mapping())
            self._body.attributes.update(body)
            self._body.clean()

        headers = self._filter_component(response.headers,
                                          self._header_mapping())
        self._header.attributes.update(headers)
        self._header.clean()
