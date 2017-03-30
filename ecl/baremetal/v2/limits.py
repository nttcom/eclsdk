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

from ecl.baremetal import baremetal_service
from ecl import resource2


class AbsoluteLimits(resource2.Resource):

    maxPersonality = resource2.Body("maxPersonality")
    personality = resource2.Body("maxPersonality")

    maxPersonalitySize = resource2.Body("maxPersonalitySize")
    personality_size = resource2.Body("maxPersonalitySize")

    maxServerMeta = resource2.Body("maxServerMeta")
    server_meta = resource2.Body("maxServerMeta")

    maxTotalInstances = resource2.Body("maxTotalInstances", alternate_id=True)
    instances = resource2.Body("maxTotalInstances")

    totalInstancesUsed = resource2.Body("totalInstancesUsed")
    instances_used = resource2.Body("totalInstancesUsed")

    maxTotalKeypairs = resource2.Body("maxTotalKeypairs")
    keypairs = resource2.Body("maxTotalKeypairs")


class RateLimit(resource2.Resource):

    limits = resource2.Body("limit", type=list)
    regex = resource2.Body("regex")
    uri = resource2.Body("uri", alternate_id=True)


class Limits(resource2.Resource):
    base_path = "/limits"
    resource_key = "limits"
    service = baremetal_service.BaremetalService()

    allow_get = True

    absolute = resource2.Body("absolute", type=AbsoluteLimits)
    rate = resource2.Body("rate", type=list)

    def get(self, session, requires_id=False):
        """Get the Limits resource.

        :param session: The session to use for making this request.
        :type session: :class:`~ecl.session.Session`

        :returns: A Baremetal Limits instance
        :rtype: :class:`~ecl.baremetal.v2.limits.Limits`
        """
        request = self._prepare_request(requires_id=False, prepend_key=False)

        response = session.get(request.uri, endpoint_filter=self.service)

        body = response.json()
        body = body[self.resource_key]

        absolute_body = self._filter_component(
            body["absolute"], AbsoluteLimits._body_mapping())
        self.absolute = AbsoluteLimits.existing(**absolute_body)

        rates_body = body["rate"]

        rates = []
        for rate_body in rates_body:
            rate_body = self._filter_component(rate_body,
                                               RateLimit._body_mapping())
            rates.append(RateLimit(**rate_body))

        self.rate = rates

        return self
