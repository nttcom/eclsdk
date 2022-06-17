from . import base

from ecl import resource2
from ecl.mvna import mvna_service


class TLSPolicy(resource2.Resource):
    resource_key = "tls_policy"
    resources_key = "tls_policies"
    service = mvna_service.MVNAService("v1.0")
    base_path = '/' + service.version + '/tls_policies'

    _query_mapping = base.MVNAQueryParameters(
        "id", "name", "description", "default",
    )

    # Capabilities
    allow_list = True
    allow_get = True
    allow_create = False
    allow_update = False
    allow_delete = False
    patch_update = False

    # Properties
    #: It identifies connection resource uniquely
    id = resource2.Body('id')
    #: Name of tls policy
    name = resource2.Body('name')
    #: Description of tls policy
    description = resource2.Body('description')
    #: Default of tls policy
    default = resource2.Body('default')
    #: TLS protocols of tls policy
    tls_protocols = resource2.Body('tls_protocols')
    #: TLS Ciphers of tls policy
    tls_ciphers = resource2.Body('tls_ciphers')
