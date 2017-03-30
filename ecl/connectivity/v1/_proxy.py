# -*- coding: utf-8 -*-


from ecl.connectivity.v1.cic import CIC, EIC
from ecl.connectivity.v1.mcic import MCIC, MEIC
from ecl.connectivity.v1.operation import Operation
from ecl.connectivity.v1.server_segment import ServerSegment

from ecl import proxy2


class Proxy(proxy2.BaseProxy):

    def mcics(self, **query):
        """Return a list of MCICs

        :param kwargs query: Query parameter to get mCICs.
            * string tenant_id: ID of a tenant to retrieve mCICs.

        :returns: A list of MCICs objects
        """
        mcic_list = self._list(MCIC, paginated=False, **query)
        return [mcic for mcic in mcic_list if mcic.service_type == "NGC-colo"]

    def meics(self, **query):
        """Return a list of MEICs

        :param kwargs query: Query parameter to get mEICs.
            * string tenant_id: ID of a tenant to retrieve mEICs.

        :returns: A list of MEICs objects
        """
        meic_list = self._list(MEIC, paginated=False, **query)
        return [meic for meic in meic_list if meic.service_type == "NGC-EC"]

    def get_mcic(self, mcic):
        """Get a single mcic

        :param mcic: The value can be the ID of a mcic or a
                       :class:`~ecl.connectivity.v2.mcic.MCIC` instance.

        :returns: One :class:`~ecl.connectivity.v2.mcic.MCIC`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(MCIC, mcic)

    def get_meic(self, meic):
        """Get a single meic

        :param meic: The value can be the ID of a meic or a
                       :class:`~ecl.connectivity.v2.mcic.MEIC` instance.

        :returns: One :class:`~ecl.connectivity.v2.mcic.MEIC`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(MEIC, meic)

    def cics(self, mcic_id, **query):
        """Return a list of CICs

        :param string mcic_id: ID of a mcic that cics belong to

        :returns: A list of CICs objects
        """
        return self._list(CIC, paginated=False, mcic_id=mcic_id, **query)

    def eics(self, meic_id, **query):
        """Return a list of EICs

        :param string meic_id: ID of a meic that eics belong to

        :returns: A list of EICs objects
        """
        return self._list(EIC, paginated=False, mcic_id=meic_id, **query)

    def get_cic(self, mcic_id, cic):
        """Get a single cic

        :param string mcic_id: ID of a mcic
        :param cic: The value can be the ID of a cic or a
                       :class:`~ecl.connectivity.v2.cic.CIC` instance.

        :returns: One :class:`~ecl.connectivity.v2.cic.CIC`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        cic = self._get_resource(CIC, cic, mcic_id=mcic_id)
        return self._get(CIC, cic)

    def get_eic(self, meic_id, eic):
        """Get a single eic

        :param string meic_id: ID of a meic
        :param eic: The value can be the ID of a eic or a
                       :class:`~ecl.connectivity.v2.cic.EIC` instance.

        :returns: One :class:`~ecl.connectivity.v2.cic.EIC`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        eic = self._get_resource(EIC, eic, mcic_id=meic_id)
        return self._get(CIC, eic)

    def create_cic(self, mcic_id, cic_name, network_id, colo_vlan):
        """Create a single cic

        :param string mcic_id: The value is the ID of a mcic
        :param string cic_name: The value is the name of a cic
        :param string network_id: The value is the ID of network of a cic
        :param int colo_vlan: The value indicates the colocation vlan of a cic

        :returns: One :class:`~ecl.connectivity.v2.cic.CIC`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        body = {
            "cic_name": cic_name,
            "network_id": network_id,
            "colo_vlan": colo_vlan,
            "mcic_id": mcic_id
        }
        return self._create(CIC, **body)

    def create_eic(self, meic_id, eic_name, network_id, server_segment_nbr):
        """Create a single eic

        :param string meic_id: The value is the ID of a meic
        :param string eic_name: The value is the name of  eic


        :returns: One :class:`~ecl.connectivity.v2.cic.EIC`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        body = {
            "cic_name": eic_name,
            "network_id": network_id,
            "server_segment_nbr": server_segment_nbr,
            "mcic_id": meic_id
        }
        return self._create(EIC, **body)

    def delete_cic(self, mcic_id, cic):
        """Delete a single cic

        :param string mcic_id: The value is the ID of a mcic
        :param cic: The value can be the ID of a cic or a
                       :class:`~ecl.connectivity.v2.cic.CIC` instance.

        :returns: One :class:`~ecl.connectivity.v2.cic.CIC`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._delete(CIC, cic, mcic_id=mcic_id)

    def delete_eic(self, meic_id, eic):
        """Delete a single eic

        :param string meic_id: The value is the ID of a meic
        :param eic: The value can be the ID of a eic or a
                       :class:`~ecl.connectivity.v2.cic.EIC` instance.

        :returns: One :class:`~ecl.connectivity.v2.cic.EIC`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._delete(EIC, eic, mcic_id=meic_id)

    def update_cic(self, mcic_id, cic, cic_name):
        """Update a single cic

        :param string mcic_id: The value is the ID of a mcic
        :param cic: The value can be the ID of a cic or a
                       :class:`~ecl.connectivity.v2.cic.CIC` instance.
        :param cic_name: The name of CIC to update

        :returns: One :class:`~ecl.connectivity.v2.cic.CIC`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        body = {"cic_name": cic_name}
        res = self._get_resource(CIC, cic, **body)
        return res.update(self.session, mcic_id, cic, **body)

    def update_eic(self, meic_id, eic, eic_name):
        """Update a single eic

        :param string meic_id: The value is the ID of a meic
        :param eic: The value can be the ID of a eic or a
                       :class:`~ecl.connectivity.v2.cic.EIC` instance.
        :param eic_name: The name of EIC to update

        :returns: One :class:`~ecl.connectivity.v2.cic.EIC`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        body = {"cic_name": eic_name}
        res = self._get_resource(CIC, eic, **body)
        return res.update(self.session, meic_id, eic, **body)

    def operations(self, **query):
        """Return a list of MCICs

        :param kwargs query: Query parameter to get operations.
            * string mcic_id: ID of a mcic
            * string cic_id: ID of a cic

        :returns: A list of Operation objects
        """
        return list(self._list(Operation, paginated=False, **query))

    def get_operation(self, operation):
        """Get a single operation

        :param operation: The value can be the ID of a operation or a
                       :class:`~ecl.connectivity.v2.operation.Operation` instance.

        :returns: One :class:`~ecl.connectivity.v2.operation.Operation`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(Operation, operation)

    def server_segments(self, service_id):
        """Return a list of Server Segments.
        :param string service_id: Enterprise Cloud service ID
        :returns: A list of ServerSegment objects
        """
        return list(self._list(ServerSegment, service_id=service_id))
