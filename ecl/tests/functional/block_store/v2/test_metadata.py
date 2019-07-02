# -*- coding: utf-8 -*-

from ecl.tests.functional import base


class TestMetadata(base.BaseFunctionalTest):

    @classmethod
    def setUpClass(cls):
        super(TestMetadata, cls).setUpClass()
        cls.test_name = "test-volume-sdk"
        volumes = cls.conn.block_store.volumes()
        cls.one_volume = None
        for vol in volumes:
            if vol.name == cls.test_name:
                cls.one_volume = vol
                break

    def _test_create(self):
        metadata = self.conn.block_store.create_metadata(self.one_volume.id,
                                                         key1="value1",
                                                         key2="value2")
        self.assertEqual(metadata.key1, "value1")
        self.assertEqual(metadata.key2, "value2")

    def test_update(self):
        metadata = self.conn.block_store.update_metadata(self.one_volume.id,
                                                         key1="value111",
                                                         key2="value222")
        self.assertEqual(metadata.key1, "value111")
        self.assertEqual(metadata.key2, "value222")
