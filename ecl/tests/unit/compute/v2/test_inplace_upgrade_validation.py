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

from ecl.compute.v2 import inplace_upgrade_validation

SERVER_ID = 'ea5a4499-c71d-4af9-b58a-30a7bcf0a898'
VALIDATION_BODY = {
    'overall_result': 'success',
    'validations': [
        {
            'validation_id': '12345',
            'result': 'success',
            'reason': '',
        },
    ],
}

EXAMPLE = {
    'server_id': SERVER_ID,
    'instance_id': 'ea5a4499-c71d-4af9-b58a-30a7bcf0a898',
    'validation': VALIDATION_BODY,
    'upgradable_targets': ['Windows2026'],
}

RESPONSE_BODY = {
    'instance_id': 'ea5a4499-c71d-4af9-b58a-30a7bcf0a898',
    'validation': VALIDATION_BODY,
    'upgradable_targets': ['Windows2026'],
}


class TestInplaceUpgradeValidation(testtools.TestCase):

    def test_basic(self):
        sot = inplace_upgrade_validation.InplaceUpgradeValidation()
        self.assertEqual('inplace_upgrade_validation', sot.resource_key)
        self.assertEqual('/servers/%(server_id)s/inplace_upgrades/validation',
                         sot.base_path)
        self.assertEqual('compute', sot.service.service_type)
        self.assertFalse(sot.allow_create)
        self.assertTrue(sot.allow_get)
        self.assertFalse(sot.allow_delete)
        self.assertFalse(sot.allow_list)
        self.assertFalse(sot.allow_update)

    def test_make_it(self):
        sot = inplace_upgrade_validation.InplaceUpgradeValidation(**EXAMPLE)
        self.assertEqual(EXAMPLE['server_id'], sot.server_id)
        self.assertEqual(EXAMPLE['instance_id'], sot.instance_id)
        self.assertEqual(EXAMPLE['validation'], sot.validation)
        self.assertEqual(EXAMPLE['upgradable_targets'], sot.upgradable_targets)

    def test_get(self):
        sess = mock.Mock()
        resp = mock.Mock()
        resp.headers = {}
        resp.json.return_value = RESPONSE_BODY
        sess.get.return_value = resp

        sot = inplace_upgrade_validation.InplaceUpgradeValidation(
            server_id=SERVER_ID).get(sess)

        sess.get.assert_called_once_with(
            '/servers/%s/inplace_upgrades/validation' % SERVER_ID,
            endpoint_filter=sot.service)

        self.assertEqual(RESPONSE_BODY['instance_id'], sot.instance_id)
        self.assertEqual(RESPONSE_BODY['validation'], sot.validation)
        self.assertEqual(RESPONSE_BODY['upgradable_targets'],
                         sot.upgradable_targets)
