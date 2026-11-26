# -*- coding: utf-8 -*-

from ecl.compute import compute_service
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
    upgradable_target = resource2.Body("upgradable_target")

    def get(self, session, requires_id=False):
        return super(InplaceUpgradeValidation, self).get(session, False)

    def _translate_response(self, response, has_body=True):
        if has_body:
            body = response.json()
            validation = body.get('validation', {})
            flattened = {
                'instance_id': body.get('instance_id'),
                'overall_result': validation.get('overall_result'),
                'validations': validation.get('validations'),
                'upgradable_target': body.get('upgradable_targets'),
            }
            flattened = self._filter_component(flattened, self._body_mapping())
            self._body.attributes.update(flattened)
            self._body.clean()

        headers = self._filter_component(response.headers,
                                          self._header_mapping())
        self._header.attributes.update(headers)
        self._header.clean()
