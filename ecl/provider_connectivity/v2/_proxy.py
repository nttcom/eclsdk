# -*- coding: utf-8 -*-

from ecl.provider_connectivity.v2 import aws_connection as _aws_connection
from ecl.provider_connectivity.v2 import gcp_connection as _gcp_connection
from ecl.provider_connectivity.v2 import exchange_point as _exchange_point
from ecl.provider_connectivity.v2 import operation as _operation
from ecl import proxy2


class Proxy(proxy2.BaseProxy):

    def aws_connections(self, **params):
        """List connection resource between ECL2.0 and AWS.

        :param params: The parameters as query string
            to get connections by specified condition.
        :returns: A list of connection objects
        :rtype: list of :class:
                `~ecl.provider_connectivity.v1.aws_connection.AWSConnection`
        """
        return list(self._list(_aws_connection.AWSConnection,
                               paginated=False,
                               **params))

    def get_aws_connection(self, connection_id):
        """Show connection resource between ECL2.0 and AWS.

        :param string connection_id: ID of specified connection.
        :return: :class:`
                ~ecl.provider_connectivity.v1.aws_connection.AWSConnection`
        """
        return self._get(_aws_connection.AWSConnection, connection_id)

    def find_aws_connection(self, name_or_id, ignore_missing=False):
        """Find a single connection

        :param name_or_id: The name or ID of a connection.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:
                `~ecl.network.v2.connection.AWSConnection` or None
        """
        return self._find(_aws_connection.AWSConnection,
                          name_or_id,
                          ignore_missing=ignore_missing)

    def update_aws_connection(self, connection, **params):
        """Update connection between ECL2.0 and AWS.

        :param string connection_id: The ID of a connection.
        :attrs \*\*params: Parameters for connection update.

            * string name: Name of connection.
            * string description: Description of connection.
            * string bandwidth: Bandwidth. If you selected BestEffort
                in the qos_type, can update 100 or 1000 Mbps.
                However, in case of Guarantee, this parameter can not update.
        """
        if not isinstance(connection, _aws_connection.AWSConnection):
            connection = self._get_resource(_aws_connection.AWSConnection,
                                            connection)
            connection._body.clean()
        return self._update(_aws_connection.AWSConnection,
                            connection, **params)

    def delete_aws_connection(self, connection_id, ignore_missing=False):
        """Delete connection between ECL2.0 and AWS.

        :param connection_id: The ID of a connection.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the port does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent port.

        :returns: ``None``
        """
        self._delete(_aws_connection.AWSConnection,
                     connection_id,
                     ignore_missing=ignore_missing)

    def prepare_aws_connection(self, aws_account_id, connected_network_address,
                           bandwidth, qos_type, exchange_point_id,
                           name=None, description=None):
        """Create connection between ECL2.0 and AWS.

        :param string aws_account_id: AWS Account ID of owner.
        :param string connected_network_address: Connected network address
            for AWS connectivity.(/28)
        :param string bandwidth: Bandwidth(Mbps). If you choose BestEffort in
            the qos_type, can select 100 or 1000.
            When you select Guarantee, choose from 50 to 500.
        :param string qos_type: QoS type of network.
            You can choose from "BestEffort" or "Guarantee".
        :param string exchange_point_id: ID of exchange_points.
        :param string name: Name of connection.
        :param string description: Description of connection.
        """
        body = {}
        body["aws_account_id"] = aws_account_id
        body["connected_network_address"] = connected_network_address
        body["bandwidth"] = bandwidth
        body["qos_type"] = qos_type
        body["exchange_point_id"] = exchange_point_id
        if name:
            body["name"] = name
        if description:
            body["description"] = description
        return self._create(_aws_connection.AWSConnection, **body)

    def approve_aws_connection(self, connection_id, action):
        """Approve/Disapprove connection between ECL2.0 and AWS.

        :param connection_id: ID of specified connection.
        :param type: Action type. You can choose "approve" or "disapprove".
        :return: ``None``
        """
        connection = _aws_connection.AWSConnection()
        connection.approve(self.session, connection_id, action)

    def exchange_points(self, **params):
        """List exchange ponts.

        :param params: The parameters as query string
            to get exchange points by specified condition.
        :returns: A list of exchange point objects
        :rtype: list of :class:`~ecl.provider_connectivity.v1.exchange_point.
            ExchangePoint`
        """
        return list(self._list(_exchange_point.ExchangePoint,
                               paginated=False,
                               **params))

    def operations(self, **params):
        """List operations.

        :param params: The parameters as query string
            to get operations by specified condition.
        :returns: A list of operation objects
        :rtype: list of :class:`~ecl.provider_connectivity.v1.operation.
            Operation`
        """
        return list(self._list(_operation.Operation,
                               paginated=False,
                               **params))

    def gcp_connections(self, **params):
        """List connection resource between ECL2.0 and GCP.

        :param params: The parameters as query string
            to get connections by specified condition.
        :returns: A list of connection objects
        :rtype: list of :class:
                `~ecl.provider_connectivity.v1.gcp_connection.GCPConnection`
        """
        return list(self._list(_gcp_connection.GCPConnection,
                               paginated=False,
                               **params))

    def get_gcp_connection(self, connection_id):
        """Show connection resource between ECL2.0 and GCP.

        :param string connection_id: ID of specified connection.
        :return: :class:`
                ~ecl.provider_connectivity.v1.gcp_connection.GCPConnection`
        """
        return self._get(_gcp_connection.GCPConnection, connection_id)

    def find_gcp_connection(self, name_or_id, ignore_missing=False):
        """Find a single connection.

        :param name_or_id: The name or ID of a connection.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:
                `~ecl.network.v2.connection.GCPConnection` or None
        """
        return self._find(_gcp_connection.GCPConnection,
                          name_or_id,
                          ignore_missing=ignore_missing)

    def create_gcp_connection(self, pairing_key_primary, pairing_key_secondary,
                              bandwidth, qos_type, exchange_point_id,
                              name=None, description=None):
        """Create connection between ECL2.0 and GCP.

        :param string pairing_key_primary: Pairing Key
            for Active Cloud Router in GCP.
        :param string pairing_key_secondary: Pairing Key
            for Standby Cloud Router in GCP
        :param string bandwidth: Bandwidth(Mbps). When you select Guarantee,
            choose 50,100,200,300,400,500,1000.
        :param string qos_type: QoS type of network.
            You can choose Guarantee.
        :param string exchange_point_id: ID of exchange_points.
        :param string name: Name of connection.
        :param string description: Description of connection.
        """
        body = {}
        body["pairing_key_primary"] = pairing_key_primary
        body["pairing_key_secondary"] = pairing_key_secondary
        body["bandwidth"] = bandwidth
        body["qos_type"] = qos_type
        body["exchange_point_id"] = exchange_point_id
        if name:
            body["name"] = name
        if description:
            body["description"] = description
        return self._create(_gcp_connection.GCPConnection, **body)

    def update_gcp_connection(self, connection, **params):
        """Update connection between ECL2.0 and GCP.

        :param string connection_id: The ID of a connection.
        :attrs \*\*params: Parameters for connection update.

            * string name: Name of connection.
            * string description: Description of connection.
            * string bandwidth: Bandwidth(Mbps). When you select Guarantee,
                choose 50,100,200,300,400,500,1000.
        """
        if not isinstance(connection, _gcp_connection.GCPConnection):
            connection = self._get_resource(_gcp_connection.GCPConnection,
                                            connection)
            connection._body.clean()
        return self._update(_gcp_connection.GCPConnection,
                            connection, **params)

    def delete_gcp_connection(self, connection_id, ignore_missing=False):
        """Delete connection between ECL2.0 and GCP.

        :param connection_id: The ID of a connection.
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the port does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent port.

        :returns: ``None``
        """
        self._delete(_gcp_connection.GCPConnection,
                     connection_id,
                     ignore_missing=ignore_missing)
