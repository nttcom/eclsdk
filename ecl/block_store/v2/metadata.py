# -*- coding: utf-8 -*-

from ecl.block_store import block_store_service
from ecl import resource


class Metadata(resource.Resource):
    resource_key = "metadata"
    resources_key = "metadata"
    base_path = "/volumes/%(volume_id)s/metadata"
    service = block_store_service.BlockStoreService()

    # capabilities
    allow_list = True
    allow_create = True
    allow_update = True


    def update(self, session, volume_id, **metadata):
        uri = self.base_path % {"volume_id": volume_id}
        body = {"metadata": metadata}
        resp = session.post(
            uri,
            endpoint_filter=self.service,
            json=body,
            headers={"Accept": ""}
        )

        meta = resp.json().get('metadata')
        for key in meta.keys():
            self.__setattr__(key, meta[key])

        return self

    def create(self, session, volume_id, **metadata):
        uri = self.base_path % {"volume_id": volume_id}
        body = {"metadata": metadata}
        resp = session.put(
            uri,
            endpoint_filter=self.service,
            json=body,
            headers={"Accept": ""}
        )

        meta = resp.json().get('metadata')
        for key in meta.keys():
            self.__setattr__(key, meta[key])

        return self
