# -*- coding: utf-8 -*-

from ecl.compute import compute_service
from ecl import resource2

class ValidateInplaceUpgrade(resource2.Resource):
    resource_key = 'inplace_upgrade_validation'
    resources_key = 'inplace_upgrade_validations'
    base_path = '/servers/%(server_id)s/inplace_upgrades/validate'
    service = compute_service.ComputeService()

    # capabilities
    allow_create = False
    allow_get = True
    allow_delete = False
    allow_list = False
    allow_update = False

    instance_id = resource2.URI("server_id")
    overall_result = resource2.Body("overall_result")
    validations = resource2.Body("validations")
    upgradable_target = resource2.Body("upgradable_target")

    def get(self, session, requires_id=False):
        return super(ValidateInplaceUpgrade, self).get(session, False)
