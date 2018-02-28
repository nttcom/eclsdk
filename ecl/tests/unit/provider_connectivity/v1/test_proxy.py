# -*- coding: utf-8 -*-


from ecl.provider_connectivity.v1 import _proxy
from ecl.provider_connectivity.v1 import tenant_connection_request as _tc_request
from ecl.provider_connectivity.v1 import tenant_connection as _tc
from ecl.provider_connectivity.v1 import address_assignment as _addr_assignment
from ecl.tests.unit import test_proxy_base2


class TestTenantConnectionProxy(test_proxy_base2.TestProxyBase):
    def setUp(self):
        super(TestTenantConnectionProxy, self).setUp()
        self.proxy = _proxy.Proxy(self.session)

    def test_tenant_connection_requests(self):
        self.verify_list(self.proxy.tenant_connection_requests,
                         _tc_request.TenantConnectionRequest,
                         paginated=False)

    def test_tenant_connection_request_get(self):
        self.verify_get(self.proxy.get_tenant_connection_request,
                        _tc_request.TenantConnectionRequest)

    def test_tenant_connection_request_create(self):
        self.verify_create(self.proxy.create_tenant_connection_request,
                           _tc_request.TenantConnectionRequest,
                           method_kwargs={
                               "keystone_user_id": "test_id",
                               "tenant_id_other": "tenant_id_other",
                               "tenant_id": "tenant_id",
                               "network_id": "network_id"},
                           expected_kwargs={
                               "keystone_user_id": "test_id",
                               "tenant_id_other": "tenant_id_other",
                               "tenant_id": "tenant_id",
                               "network_id": "network_id"})

    def test_tenant_connection_request_delete(self):
        self.verify_delete(self.proxy.delete_tenant_connection_request,
                           _tc_request.TenantConnectionRequest,
                           False)

    def test_tenant_connection_request_find(self):
        self.verify_find(self.proxy.find_tenant_connection_request,
                         _tc_request.TenantConnectionRequest)

    def test_tenant_connections(self):
        self.verify_list(self.proxy.tenant_connections,
                         _tc.TenantConnection,
                         paginated=False)

    def test_tenant_connection_get(self):
        self.verify_get(self.proxy.get_tenant_connection,
                        _tc.TenantConnection)

    def test_tenant_connection_delete(self):
        self.verify_delete(self.proxy.delete_tenant_connection,
                           _tc.TenantConnection, False)

    def test_tenant_connection_create(self):
        self.verify_create(self.proxy.create_tenant_connection,
                           _tc.TenantConnection,
                           method_kwargs={
                               "tenant_connection_request_id": "test_id",
                               "device_type": "device_type",
                               "device_id": "device_id"
                           },
                           expected_kwargs={
                               "tenant_connection_request_id": "test_id",
                               "device_type": "device_type",
                               "device_id": "device_id"
                           })

    def test_tenant_connection_find(self):
        self.verify_find(self.proxy.find_tenant_connection,
                         _tc.TenantConnection)

    def test_address_assignments(self):
        self.verify_list(self.proxy.address_assignments,
                         _addr_assignment.AddressAssignment,
                         method_kwargs={"tenant_connection_request_id": "test_id"},
                         expected_kwargs={"tenant_connection_request_id": "test_id"})
