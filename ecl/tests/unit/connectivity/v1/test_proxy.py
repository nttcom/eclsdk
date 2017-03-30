# -*- coding: utf-8 -*-


from ecl.connectivity.v1 import _proxy
from ecl.connectivity.v1 import mcic
from ecl.tests.unit import test_proxy_base2


class TestConnectivityProxy(test_proxy_base2.TestProxyBase):
    def setUp(self):
        super(TestConnectivityProxy, self).setUp()
        self.proxy = _proxy.Proxy(self.session)

    def test_mcics(self):
        self.verify_list(self.proxy.mcics, mcic.MCIC,
                         paginated=False,
                         method_kwargs={"query": 1},
                         expected_kwargs={"query": 1})
