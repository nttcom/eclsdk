# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from ecl import proxy2
from ecl.dns.v2 import zone as _zone
from ecl.dns.v2 import name_server
from ecl.dns.v2 import recordset as _recordset


class Proxy(proxy2.BaseProxy):

    def zones(self):
        """
        List the zones.
        :return: A list of zone object
        """
        return list(self._list(_zone.Zone))

    def get_zone(self, zone):
        """
        Show a Zone.
        :param: zone: The value can be the ID of a zone or a
                       :class:`~ecl.dns.v2.zone.Zone` instance.
        :return: One :class:`~ecl.dns.v2.zone.Zone` or
                     :class:`~ecl.exceptions.ResourceNotFound`when no
                     resource can be found.
        """
        return self._get(_zone.Zone, zone)

    def find_zone(self, name_or_id, ignore_missing=False):
        """
        Find a zone by its name or ID
        :param name_or_id: The name or ID of a zone
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :return: One :class:`~ecl.dns.v2.zone.Zone` or
                     :class:`~ecl.exceptions.ResourceNotFound`when no
                     resource can be found.
        """
        return self._find(_zone.Zone, name_or_id, ignore_missing=ignore_missing)

    def create_zone(self, name=None, ttl=None, type=None,
                    description=None, email=None, masters=None):
        """
        Create a zone.
        :param name: DNS Name for the zone. Required.
        :param ttl: TTL (Time to Live) for the zone. This parameter is not currently supported.
        :param type: Type of zone. PRIMARY is controlled by ECL2.0 DNS, SECONDARY zones are slaved from another DNS Server. Defaults to PRIMARY. This parameter is not currently supported.
        :param description: Description for this zone
        :param email: e-mail for the zone. Used in SOA records for the zone. This parameter is not currently supported.
        :param masters: For secondary zones. The servers to slave from to get DNS information. This parameter is not currently supported.
        :return: :class:`~ecl.dns.v2.zone.Zone`
        """
        attr = {"name": name}
        if ttl is not None:
            attr["ttl"] = ttl
        if type is not None:
            attr["type"] = type
        if description is not None:
            attr["description"] = description
        if email is not None:
            attr["email"] = email
        if masters is not None:
            attr["masters"] = masters
        return self._create(_zone.Zone, **attr)

    def update_zone(self, zone, ttl=None,
                    description=None, email=None, masters=None):
        """
        Update the attribute(s) for an existing zone.
        :param zone: ID for the zone or zone instance to update.
        :param ttl: TTL (Time to Live) for the zone. This parameter is not currently supported.
        :param description: Description for this zone
        :param email: e-mail for the zone. Used in SOA records for the zone. This parameter is not currently supported.
        :param masters: For secondary zones. The servers to slave from to get DNS information. This parameter is not currently supported.
        :return: :class:`~ecl.dns.v2.zone.Zone`
        """
        attr = {}
        if ttl is not None:
            attr["ttl"] = ttl
        if description is not None:
            attr["description"] = description
        if email is not None:
            attr["email"] = email
        if masters is not None:
            attr["masters"] = masters

        if not isinstance(zone, _zone.Zone):
            zone = self._get_resource(_zone.Zone, zone)
            zone._body.clean()

        return self._update(_zone.Zone, zone, **attr)

    def delete_zone(self, zone_id, ignore_missing=False):
        """
        Delete a zone.
        :param zone_id: ID for the zone
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the server does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent zone
        :return: None
        """
        return self._delete(_zone.Zone, zone_id, ignore_missing=False)

    def get_name_server(self, zone_id):
        """
        Show the nameservers for a zone.
        :param zone_id: ID for the zone
        :return: :class:`~ecl.dns.v2.name_server.NameServer`
        """
        return list(self._list(name_server.NameServer, zone_id=zone_id))

    def recordsets(self, zone_id, limit=None, marker=None):
        """
        This lists all recordsets in a zone.
        :param zone_id: ID for the zone
        :param limit: Requests a page size of items(1-500). Returns a number of items up to a limit value. Use the limit parameter to make an initial limited request and use the ID of the last-seen item from the response as the marker parameter value in a subsequent limited request.
        :param marker: The ID of the last-seen item. Use the limit parameter to make an initial limited request and use the ID of the last-seen item from the response as the marker parameter value in a subsequent limited request.
        :return: One list of :class:`~ecl.dns.v2.recordsets.Recordsets`
        """
        attrs = {}
        attrs["zone_id"] = zone_id
        if limit is not None:
            attrs["limit"] = limit
        if marker is not None:
            attrs["marker"] = marker

        return list(self._list(_recordset.RecordSet, **attrs))

    def get_recordset(self, zone_id, recordset_id):
        """
        Show a single recordset.
        :param zone_id: ID for the zone the recordset belonging to
        :param recordset_id: ID for the recordset
        :return: One :class:`~ecl.dns.v2.recordsets.Recordsets` or
                     :class:`~ecl.exceptions.ResourceNotFound`when no
                     resource can be found.
        """
        # TODO: If zone instance is used...
        return self._get(_recordset.RecordSet, recordset_id, zone_id=zone_id)

    def find_recordset(self, zone_id, name_or_id, ignore_missing=False):
        """
        Find a recordset by its name or ID.
        :param name_or_id: Name or ID for this recordset
        :return: One :class:`~ecl.dns.v2.recordsets.Recordsets` or
                     :class:`~ecl.exceptions.ResourceNotFound`when no
                     resource can be found.
        """
        return self._find(_recordset.RecordSet, name_or_id, zone_id=zone_id, ignore_missing=ignore_missing)

    def create_recordset(self, zone_id, name=None, description=None,
                         type=None, ttl=None, records=None):
        """
        Create a recordset in a zone.
        :param zone_id: ID for the zone.
        :param name: DNS Name for the recordset.
        :param description: Description for this recordset.
        :param type: RRTYPE of the recordset. Valid Values: A | AAAA | MX | CNAME | SRV | SPF | TXT | PTR | NS
        :param ttl: TTL (Time to Live) for the recordset.
        :param recodrs: A list of data for this recordset.
                        Each item will be a separate record in ECL2.0 DNS.
                        These items should conform to the DNS spec for the record type
                        - e.g. A records must be IPv4 addresses, CNAME records must be a hostname.
        :return: :class:`~ecl.dns.v2.recordsets.Recordsets`
        """
        attr = {"name": name}
        if ttl is not None:
            attr["ttl"] = ttl
        if type is not None:
            attr["type"] = type
        if description is not None:
            attr["description"] = description
        if records is not None:
            attr["records"] = records

        return self._create(_recordset.RecordSet, zone_id=zone_id, **attr)

    def update_recordset(self, zone_id, recordset, ttl=None, description=None,
                         name=None, records=None):
        """
        Update a recordset.
        :param recordset: ID for the recordset.
        :param zone_id: ID for the zone.
        :param ttl: TTL (Time to Live) for the recordset.
        :param description: Description for this recordset.
        :param name: DNS Name for the recordset.
        :param record: A list of data for this recordset.
                        Each item will be a separate record in ECL2.0 DNS.
                        These items should conform to the DNS spec for the record type
                        - e.g. A records must be IPv4 addresses, CNAME records must be a hostname.
        :return: :class:`~ecl.dns.v2.recordsets.Recordsets`
        """
        attr = {}
        if ttl is not None:
            attr["ttl"] = ttl
        if description is not None:
            attr["description"] = description
        if records is not None:
            attr["records"] = records
        if name is not None:
            attr["name"] = name

        if not isinstance(recordset, _recordset.RecordSet):
            recordset = self._get_resource(_recordset.RecordSet, recordset)
            recordset._body.clean()

        return self._update(_recordset.RecordSet,
                            recordset, zone_id=zone_id, **attr)

    def delete_recordset(self, zone_id, recordset):
        """
        Delete a recordset.
        :param zone_id: ID for the recordset.
        :param recordset: ID for the zone.
        :return: None
        """
        return self._delete(_recordset.RecordSet, recordset, zone_id=zone_id)

    def delete_multiple_recordsets(self, zone_id, recordset_ids):
        """
        Delete multiple Recordsets.
        :param recordset_ids: A list of IDs for the recordsets.
        :param zone_id: ID for the zone
        :return: None
        """
        return _recordset.RecordSet.multi_delete(
                self.session, zone_id=zone_id,
                recordset_ids=recordset_ids
        )
