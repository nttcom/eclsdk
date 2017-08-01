# -*- coding: utf-8 -*-

from ecl.security_order import security_order_service
from ecl import resource2
from ecl import exceptions
from ecl import utils

class HostBasedSecurity(resource2.Resource):
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

    #: Tenant ID of the owner (UUID).
    tenant_id = resource2.Body('tenant_id')
    #: N: Order New Host-based Security.
    #: M1: Change menu of Host-based Security.
    #: M2: Change quantity of Host-based Security.
    #: C: Cancel Host-based Security.
    sokind = resource2.Body('sokind')
    #: Requested menu. Set "Managed Anti-Virus", "Managed Virtual Patch"
    #: or "Managed Host-based Security Package" to this field.
    service_order_service = resource2.Body('service_order_service')
    #: Set maximum quantity of Agenet usage.
    max_agent_value = resource2.Body('max_agent_value')
    #: Contactable mail address.
    mailaddress = resource2.Body('mailaddress')
    #: This value is used for language of Deep Security Manager.
    #: ja: Japanese, en: English.
    dsm_lang = resource2.Body('dsm_lang')
    #: Set "Asia/Tokyo" for JST or "Etc/GMT" for UTC.
    time_zone = resource2.Body('time_zone')
    #: Messages are displayed in Japanese or English depending on this value.
    #: ja: Japanese, en: English. Default value is "en".
    locale = resource2.Body('locale')
    #: This value indicates normal or abnormal. 1:normal, 2:abnormal.
    code = resource2.Body('code', alternate_id=True)
    #: This message is shown when error has occurred.
    message = resource2.Body('message')
    #: Identification ID of Service Order.
    soid = resource2.Body('soId')
    #: This value indicates normal or abnormal. 1:normal, 2:abnormal.
    status = resource2.Body('status')
    #: Percentage of Service Order Progress Status.
    progress_rate = resource2.Body('progressRate')
    #: Region tenant you specified belongs to.
    region = resource2.Body('region')
    #: Tenant Name.
    tenant_name = resource2.Body('tenant_name')
    #: Description for this tenant.
    tenant_description = resource2.Body('tenant_description')
    #: Contract ID which this tenant belongs to.
    contract_id = resource2.Body('contract_id')
    #: Customer Name.
    customer_name = resource2.Body('customer_name')
    #: Internal Use. (true: Already applied, false: Not applied.)
    tenant_flg = resource2.Body('tenant_flg')

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
