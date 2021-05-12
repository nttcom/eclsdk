from . import base

from ecl import resource2
from ecl.mvna import mvna_service


class Certificate(resource2.Resource):
    resource_key = "certificate"
    resources_key = "certificates"
    service = mvna_service.MVNAService("v1.0")
    base_path = '/' + service.version + '/certificates'

    _query_mapping = base.MVNAQueryParameters(
        "id",
        "name",
        "description",
        "tenant_id",
        "ca_cert_status",
        "ssl_key_status",
        "ssl_cert_status"
    )

    # Capabilities
    allow_list = True
    allow_get = True
    allow_create = True
    allow_update = True
    allow_delete = True
    patch_update = True

    # Properties
    #: It identifies connection resource uniquely
    id = resource2.Body('id')
    #: Name of certificate
    name = resource2.Body('name')
    #: Description of certificate
    description = resource2.Body('description')
    #: Tags of certificate
    tags = resource2.Body('tags')
    #: Tenant ID
    tenant_id = resource2.Body('tenant_id')
    #: SSL Key
    ssl_key = resource2.Body('ssl_key')
    #: SSL Cert
    ssl_cert = resource2.Body('ssl_cert')
    #: Ca Cert
    ca_cert = resource2.Body('ca_cert')

    def upload(self, session, resource_id, **body):
        uri = self.base_path + '/%s/files' % resource_id
        resp = session.post(uri, endpoint_filter=self.service, json=body)
        self._translate_response(resp, has_body=False)
        return self
