# -*- coding: utf-8 -*-

from ecl.compute import compute_service
from ecl import resource2
from ecl import utils

class Volume(resource2.Resource):
    resource_key = 'volume'
    resources_key = 'volumes'
    base_path = '/volumes'
    service = compute_service.ComputeService()

    # capabilities
    allow_create = True
    allow_get = True
    allow_delete = True
    allow_list = True
    allow_update = True

    id = resource2.Body("id")
    name = resource2.Body("displayName")
    description = resource2.Body("displayDescription")
    size = resource2.Body("size")
    volume_type = resource2.Body("volumeType")
    metadata = resource2.Body("metadata", dict)
    availability_zone = resource2.Body("availabilityZone")
    snapshot_id = resource2.Body("snapshotId")
    attachments = resource2.Body("attachments", list)
    created_at = resource2.Body("createdAt")
    status = resource2.Body('status')
    bootable = resource2.Body('bootable')

    def retype(self, session, volume_type, is_dry_run=False):
        """ Volume type change and dry run configuration process. """
        body = {
            'os-retype': {
                'new_type': volume_type,
                'migration_policy': 'on-demand'
            }
        }
        if is_dry_run:
            body['os-retype']['dryRun'] = True
        self._action(session, body)

    def _action(self, session, body):
        """Preform server actions given the message body."""
        # NOTE: This is using Server.base_path instead of self.base_path
        # as both Server and ServerDetail instances can be acted on, but
        # the URL used is sans any additional /detail/ part.
        url = utils.urljoin(Volume.base_path, self.id, 'action')
        headers = {'Accept': ''}
        return session.post(
            url, endpoint_filter=self.service, json=body, headers=headers)


class VolumeDetail(Volume):
    base_path = '/os-volumes/detail'

    allow_create = False
    allow_get = False
    allow_delete = False
