# -*- coding: utf-8 -*-

from ecl.tests.functional import base


class TestVPNService(base.BaseFunctionalTest):

    def test_list_vpns(self):
        vpn_services = self.conn.network.vpn_services()
        if not vpn_services or len(vpn_services) <= 0:
            return
        vpn_service = vpn_services[0]

        vpn_gateways = self.conn.network.vpn_gateways(vpn_service_id=vpn_service.id)
        if not vpn_gateways or len(vpn_gateways) <= 0:
            return
        vpn_gw = vpn_gateways[0]
        self.assertEqual(vpn_gw.vpn_service_id, vpn_service.id)

        vpn_ifs = self.conn.network.vpn_interfaces(vpn_gw_id=vpn_gw.id)
        if not vpn_ifs or len(vpn_ifs) <= 0:
            return
        print("vpn_ifs:", len(vpn_ifs), "example id:")
        vpn_if = vpn_ifs[0]
        self.assertEqual(vpn_if.vpn_gw_id, vpn_gw.id)

    def test_list_gw_interfaces(self):
        vpn_gw_ifs = self.conn.network.gateway_interfaces(service_type="vpn")
        inet_gw_ifs = self.conn.network.gateway_interfaces(service_type="internet")
        idc_gw_ifs = self.conn.network.gateway_interfaces(service_type="interdc")
        self.assertGreaterEqual(vpn_gw_ifs, 0)
        self.assertGreaterEqual(inet_gw_ifs, 0)
        self.assertGreaterEqual(idc_gw_ifs, 0)
