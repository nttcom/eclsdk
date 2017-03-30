# -*- coding: utf-8 -*-

import six

from ecl.tests.functional import base


class TestVolume(base.BaseFunctionalTest):

    @classmethod
    def setUpClass(cls):
        super(TestVolume, cls).setUpClass()
        vols = cls.conn.compute.volumes()
        cls.one_volume = None
        if vols and len(vols):
            cls.one_volume = vols[0]

    def _test_volumes(self):
        vols = self.conn.compute.volumes()
        for vol in vols:
            self.assertIsInstance(vol.id, six.string_types)

    def _test_get_volumes(self):
        if self.one_volume is None:
            return
        vol = self.conn.compute.get_volume(self.one_volume.id)
        self.assertEqual(vol.id, self.one_volume.id)

    def _test_create(self):
        test_name = "test-volume-sdk"
        vol = self.conn.compute.create_volume(15, name=test_name)
        self.assertEqual(vol.name, test_name)

    def test_delete(self):
        test_name = "test-volume-sdk"
        vols = self.conn.compute.volumes()
        find_vol = None
        for vol in vols:
            if vol.name == test_name:
                find_vol = vol
                break
        if find_vol:
            ret = self.conn.compute.delete_volume(find_vol.id)
            self.assertIsNone(ret)
