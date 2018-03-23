# -*- coding: utf-8 -*-

from ecl import resource2


class ProviderConnectivityBaseResource(resource2.Resource):

    @property
    def name_or_id(self):
        try:
            return (self._body.get('name') or
                    '(%s)' % self._body['id'][:13])
        except KeyError:
            pass

    @property
    def name_other_or_id(self):
        try:
            return (self._body.get('name_other') or
                    '(%s)' % self._body['id'][:13])
        except KeyError:
            pass
