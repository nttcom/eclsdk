from ecl import resource2


class MVNABaseResource(resource2.Resource):

    def get_resource(self, session, resource_id, changes=None):
        if changes is not None and type(changes) is bool:
            uri = self.base_path + '/%s?changes=%s' % \
                  (resource_id, str(changes).lower())
        else:
            uri = self.base_path + '/%s' % resource_id
        resp = session.get(uri, endpoint_filter=self.service)
        self._translate_response(resp, has_body=True)
        return self

    def create_staged_configuration(self, session, resource_id, **body):
        uri = self.base_path + '/%s/staged' % resource_id
        resp = session.post(uri, endpoint_filter=self.service,
                            json={self.resource_key: body})
        self._translate_response(resp, has_body=True)
        return self

    def get_staged_configuration(self, session, resource_id, changes=None):
        if changes is not None and type(changes) is bool:
            uri = self.base_path + '/%s/staged?changes=%s' % \
                  (resource_id, str(changes).lower())
        else:
            uri = self.base_path + '/%s/staged' % resource_id
        resp = session.get(uri, endpoint_filter=self.service)
        self._translate_response(resp, has_body=True)
        return self

    def update_staged_configuration(self, session, resource_id, **body):
        uri = self.base_path + '/%s/staged' % resource_id
        resp = session.patch(uri, endpoint_filter=self.service,
                             json={self.resource_key: body})
        self._translate_response(resp, has_body=True)
        return self

    def cancel_staged_configuration(self, session, resource_id):
        uri = self.base_path + '/%s/staged' % resource_id
        session.delete(uri, endpoint_filter=self.service)
