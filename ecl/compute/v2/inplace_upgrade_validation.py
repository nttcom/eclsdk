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
    overall_result = resource2.Body("overall_result")
    validations = resource2.Body("validations")
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
            validation = body.get('validation', {})
            flattened = {
                'instance_id': body.get('instance_id'),
                'overall_result': validation.get('overall_result'),
                'validations': validation.get('validations'),
                'upgradable_targets': body.get('upgradable_targets'),
            }
            flattened = self._filter_component(flattened, self._body_mapping())
            self._body.attributes.update(flattened)
            self._body.clean()

        headers = self._filter_component(response.headers,
                                          self._header_mapping())
        self._header.attributes.update(headers)
        self._header.clean()
