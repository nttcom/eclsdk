# -*- coding: utf-8 -*-

from ecl.security_order import security_order_service
from ecl import resource2
from ecl import exceptions
from ecl import utils

class HostBased(resource2.Resource):
    resource_key = None
    resources_key = None
    base_path = '/API/SoEntryHBS'
    service = security_order_service.SecurityOrderService()

    # Capabilities
    allow_create = True
    allow_get = True
    allow_delete = True
    allow_list = True
    allow_update = True

    def get_order_status(self, session, soid, locale=None):
        tenant_id = session.get_project_id()
        uri = '/API/ScreenEventHBSOrderProgressRate?tenant_id=%s&soid=%s' \
              % (tenant_id, soid)
        if locale is not None:
            uri += '&locale=%s' % locale
        headers = {'Content-Type': 'application/json'}
        resp = session.get(uri, endpoint_filter=self.service, headers=headers)
        self._translate_response(resp, has_body=True)
        return self

    def get_order_info(self, session, locale=None):
        tenant_id = session.get_project_id()
        uri = '/API/ScreenEventHBSOrderInfoGet?tenant_id=%s' % tenant_id
        if locale is not None:
            uri += '&locale=%s' % locale
        headers = {'Content-Type': 'application/json'}
        resp = session.get(uri, endpoint_filter=self.service, headers=headers)
        self._translate_response(resp, has_body=True)
        return self

    def update(self, session, **body):
        uri = self.base_path
        resp = session.post(uri, endpoint_filter=self.service, json=body)
        self._translate_response(resp, has_body=True)
        return self

    def delete(self, session, body, locale=None):
        uri = self.base_path
        resp = session.post(uri, endpoint_filter=self.service, json=body)
        self._translate_response(resp, has_body=True)
        return self
