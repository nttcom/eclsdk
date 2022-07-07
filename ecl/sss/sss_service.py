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

from ecl import service_filter


class SssService(service_filter.ServiceFilter):
    """The SSS service."""

    valid_versions = [service_filter.ValidVersion('v2')]

    def __init__(self, **kwargs):
        """Create a SSS service."""
        super(SssService, self).__init__(service_type='sssv2',
                                         **kwargs)


class SssAdminService(SssService):
    """The SSS service. (Admin Endpoint)"""

    def __init__(self, **kwargs):
        kwargs['interface'] = service_filter.ServiceFilter.ADMIN
        super(SssAdminService, self).__init__(**kwargs)

