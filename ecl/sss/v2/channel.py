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

from ecl.sss import  sss_service
from ecl import resource2

class Channel(resource2.Resource):
    resource_key = None
    resources_key = "channels"
    base_path = "/channels?get_contracts=%(get_contracts)s"
    service = sss_service.SssService()

    #Capabilities
    allow_list = True

    #_query_mapping = resource2.QueryParameters("get_contracts")

    #Properties
    #: Channel ID.
    channel_id = resource2.Body("channel_id", alternate_id=True)
    #: Channel name.
    channel_name = resource2.Body("channel_name")
    #: This item setting will relate to language setting of E-mail that will
    #: send by ECL2.0. Please note that NOT related to user's display language
    #: setting(That setting is rely on the user browser's language setting.)
    language = resource2.Body("language")
    #: Whether this channel_id is the partner management channel(true), or
    #: not(false).
    management_channel = resource2.Body("management_channel")
    #: The parent channel ID means partner's channel ID that belongs the end
    #: user.
    parent_channel_id = resource2.Body("parent_channel_id")
    #: List of contracts has two parameters:
    #: contract_id: Contract ID.
    #: status: The status of the contract(enable or deleted).
    contracts = resource2.Body("contracts")

    def __init__(self, synchronized=False, **attrs):
        super(Channel, self).__init__(synchronized=synchronized, **attrs)
        if "get_contracts" in attrs:
            attrs.pop("get_contracts")
