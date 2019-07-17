# -*- coding: utf-8 -*-


from ecl import resource2


class NetworkBaseResource(resource2.Resource):

    @property
    def name_or_id(self):
        try:
            return (self._body.get('name') or
                    '(%s)' % self._body['id'][:13])
        except KeyError:
            pass

    def set_id_as_name_if_empty(self, length=8):
        try:
            if not self._body.get('name'):
                id = self._body['id']
                if length:
                    id = id[:length]
                setattr(self, 'name', '(%s)' % id)
        except KeyError:
            pass

    #: The ID of the project this resource is associated with.
    tenant_id = resource2.Body('tenant_id')
