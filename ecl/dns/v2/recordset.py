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

from ecl.dns import dns_service
from ecl import resource2
from ecl import exceptions


class RecordSet(resource2.Resource):
    resource_key = None
    resources_key = "recordsets"
    base_path = '/v2/zones/%(zone_id)s/recordsets'
    service = dns_service.DnsService()

    # Capabilities
    allow_create = True
    allow_delete = True
    allow_update = True
    allow_list = True
    allow_get = True

    _query_mapping = resource2.QueryParameters("limit", "marker")

    # Properties
    #: ID for the resource
    id = resource2.Body('id')
    #: DNS Name for the recordset.
    name = resource2.Body('name')
    #: Description for this recordset.
    description = resource2.Body('description')
    #: ID for the zone that contains this recordset.
    zone_id = resource2.URI('zone_id')
    #: Date / Time when resource was created.
    created_at = resource2.Body('created_at')
    #: Date / Time when resource last updated.
    updated_at = resource2.Body('updated_at')
    #: Version of the resource. This parameter is not currently supported. it always return 1.
    version = resource2.Body('version')
    #: They RRTYPE of the recordset.
    type = resource2.Body('type')
    #: status of the resource.
    status = resource2.Body('status')
    #: TTL (Time to Live) for the recordset. This parameter is not currently supported. it always return zero.
    ttl = resource2.Body('ttl')
    #: Links to the resource, and other related resources. When a response has been broken into pages,
    #: we will include a next link that should be followed to retrive all results.
    links = resource2.Body('links')
    #: Links to the resource, and other related resources. When a response has been broken into pages,
    #: we will include a next link that should be followed to retrive all results.
    records = resource2.Body('records')


    def _translate_recordsets(self, response, has_body=True):
        """
        In order to handle the response.
        Response example:
        {"recordsets":
        [
            {"id":"fcb86eb9-8f8d-4cfd-8309-9052236d75df",
                "zone_id":"d4f0ea0e-edb6-4bbb-aefd-2944457be234",
                "records":["203.0.143.22"],
                "ttl":3600,"name":"ns3.base.co.jp.",
                "description":null,"type":"A","version":1,
                "created_at":"","updated_at":null,
                "links":{"self":"https://dns-lab3ec-ecl.lab.api.ntt.com/v2/zones/d4f0ea0e-edb6-4bbb-aefd-2944457be234/recordsets/fcb86eb9-8f8d-4cfd-8309-9052236d75df"}},
            {"id":"b0590460-11b3-413d-ad95-5cd3f4b01c27",
                "zone_id":"d4f0ea0e-edb6-4bbb-aefd-2944457be234",
                "records":["203.0.143.23"],"ttl":3600,
                "name":"ns3.base.co.jp.",
                "description":null,"type":"A",
                "version":1,"created_at":"",
                "updated_at":null,
                "links":{"self":"https://dns-lab3ec-ecl.lab.api.ntt.com/v2/zones/d4f0ea0e-edb6-4bbb-aefd-2944457be234/recordsets/b0590460-11b3-413d-ad95-5cd3f4b01c27"}}
        ],
        "links":{"self":"https://dns-lab3ec-ecl.lab.api.ntt.com/v2/zones/d4f0ea0e-edb6-4bbb-aefd-2944457be234/recordsets"},
        "metadata":{"total_count":2}}
        """

        if has_body:
            body = response.json()
            body = body[self.resources_key]


            for data in body:
                value = self.existing(**data)
                yield value

    def create(self, session, prepend_key=True):
        """
        Recordset allow creating several records once.
        Thus return a list.
        """
        if not self.allow_create:
            raise exceptions.MethodNotSupported(self, "create")

        if self.put_create:
            request = self._prepare_request(requires_id=True,
                                            prepend_key=prepend_key)
            response = session.put(request.uri, endpoint_filter=self.service,
                                   json=request.body, headers=request.headers)
        else:
            request = self._prepare_request(requires_id=False,
                                            prepend_key=prepend_key)
            response = session.post(request.uri, endpoint_filter=self.service,
                                    json=request.body, headers=request.headers)

        return list(self._translate_recordsets(response, has_body=True))

    @classmethod
    def multi_delete(cls, session, zone_id, recordset_ids):
        """
        Delete multiple Recordsets
        """
        uri = cls.base_path % {"zone_id": zone_id}
        body = {"id": recordset_ids}
        session.delete(uri, endpoint_filter=cls.service, json=body)

    @classmethod
    def find(cls, session, name_or_id, zone_id, ignore_missing=False, **params):
        """Find a resource by its name or id.

        :param session: The session to use for making this request.
        :type session: :class:`~ecl.session.Session`
        :param name_or_id: This resource's identifier, if needed by
                           the request. The default is ``None``.
        :param zone_id: ID for the zone
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :param dict params: Any additional parameters to be passed into
                            underlying methods, such as to
                            :meth:`~ecl.resource2.Resource.existing`
                            in order to pass on URI parameters.

        :return: The :class:`Resource` object matching the given name or id
                 or None if nothing matches.
        :raises: :class:`ecl.exceptions.DuplicateResource` if more
                 than one resource is found for this request.
        :raises: :class:`ecl.exceptions.ResourceNotFound` if nothing
                 is found and ignore_missing is ``False``.
        """
        # Try to short-circuit by looking directly for a matching ID.

        data = list(cls.list(session, zone_id=zone_id, **params))

        result = cls._get_one_match(name_or_id, data)
        if result is not None:
            return result

        if ignore_missing:
            return None
        raise exceptions.ResourceNotFound(
            "No %s found for %s" % (cls.__name__, name_or_id))
