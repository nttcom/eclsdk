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

import mock
import testtools

from ecl.baremetal.v2 import limits

ABSOLUTE_LIMITS = {
    "maxPersonality": 5,
    "maxPersonalitySize": 10240,
    "maxServerMeta": 128,
    "maxTotalInstances": 10,
    "maxTotalKeypairs": 100,
    "totalInstancesUsed": 5,
}

RATE_LIMIT = {
    "limit": [
        {
            "next-available": "2012-11-27T17:22:18Z",
            "remaining": 120,
            "unit": "MINUTE",
            "value": 120,
            "verb": "POST"
        },
    ],
    "regex": ".*",
    "uri": "*"
}

LIMITS_BODY = {
    "limits": {
        "absolute": ABSOLUTE_LIMITS,
        "rate": [RATE_LIMIT]
    }
}


class TestAbsoluteLimits(testtools.TestCase):

    def test_basic(self):
        sot = limits.AbsoluteLimits()
        self.assertIsNone(sot.resource_key)
        self.assertIsNone(sot.resources_key)
        self.assertEqual("", sot.base_path)
        self.assertIsNone(sot.service)
        self.assertFalse(sot.allow_create)
        self.assertFalse(sot.allow_get)
        self.assertFalse(sot.allow_update)
        self.assertFalse(sot.allow_delete)
        self.assertFalse(sot.allow_list)

    def test_make_it(self):
        sot = limits.AbsoluteLimits(**ABSOLUTE_LIMITS)
        self.assertEqual(ABSOLUTE_LIMITS["maxPersonality"], sot.personality)
        self.assertEqual(ABSOLUTE_LIMITS["maxPersonalitySize"],
                         sot.personality_size)
        self.assertEqual(ABSOLUTE_LIMITS["maxServerMeta"], sot.server_meta)
        self.assertEqual(ABSOLUTE_LIMITS["maxTotalInstances"],
                         sot.instances)
        self.assertEqual(ABSOLUTE_LIMITS["maxTotalKeypairs"],
                         sot.keypairs)
        self.assertEqual(ABSOLUTE_LIMITS["totalInstancesUsed"],
                         sot.instances_used)


class TestRateLimit(testtools.TestCase):

    def test_basic(self):
        sot = limits.RateLimit()
        self.assertIsNone(sot.resource_key)
        self.assertIsNone(sot.resources_key)
        self.assertEqual("", sot.base_path)
        self.assertIsNone(sot.service)
        self.assertFalse(sot.allow_create)
        self.assertFalse(sot.allow_get)
        self.assertFalse(sot.allow_update)
        self.assertFalse(sot.allow_delete)
        self.assertFalse(sot.allow_list)

    def test_make_it(self):
        sot = limits.RateLimit(**RATE_LIMIT)
        self.assertEqual(RATE_LIMIT["regex"], sot.regex)
        self.assertEqual(RATE_LIMIT["uri"], sot.uri)
        self.assertEqual(RATE_LIMIT["limit"], sot.limits)


class TestLimits(testtools.TestCase):

    def test_basic(self):
        sot = limits.Limits()
        self.assertEqual("limits", sot.resource_key)
        self.assertEqual("/limits", sot.base_path)
        self.assertEqual("baremetal-server", sot.service.service_type)
        self.assertTrue(sot.allow_get)
        self.assertFalse(sot.allow_create)
        self.assertFalse(sot.allow_update)
        self.assertFalse(sot.allow_delete)
        self.assertFalse(sot.allow_list)

    def test_get(self):
        sess = mock.Mock()
        resp = mock.Mock()
        sess.get.return_value = resp
        resp.json.return_value = LIMITS_BODY

        sot = limits.Limits().get(sess)

        self.assertEqual(ABSOLUTE_LIMITS["maxPersonality"],
                         sot.absolute.personality)
        self.assertEqual(ABSOLUTE_LIMITS["maxPersonalitySize"],
                         sot.absolute.personality_size)
        self.assertEqual(ABSOLUTE_LIMITS["maxServerMeta"],
                         sot.absolute.server_meta)
        self.assertEqual(ABSOLUTE_LIMITS["maxTotalInstances"],
                         sot.absolute.instances)
        self.assertEqual(ABSOLUTE_LIMITS["maxTotalKeypairs"],
                         sot.absolute.keypairs)
        self.assertEqual(ABSOLUTE_LIMITS["totalInstancesUsed"],
                         sot.absolute.instances_used)

        self.assertEqual(RATE_LIMIT["uri"], sot.rate[0].uri)
        self.assertEqual(RATE_LIMIT["regex"], sot.rate[0].regex)
        self.assertEqual(RATE_LIMIT["limit"], sot.rate[0].limits)
