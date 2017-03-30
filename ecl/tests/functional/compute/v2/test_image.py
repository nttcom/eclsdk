# -*- coding: utf-8 -*-

from ecl.tests.functional import base


class TestImage(base.BaseFunctionalTest):

    # def test_images(self):
    #     images = list(self.conn.compute.images())
    #     self.assertGreater(len(images), 0)
    #     for image in images:
    #         self.assertIsInstance(image.id, six.string_types)

    # def test_find_image(self):
    #     image = self._get_non_test_image()
    #     self.assertIsNotNone(image)
    #     sot = self.conn.compute.find_image(image.id)
    #     self.assertEqual(image.id, sot.id)
    #     self.assertEqual(image.name, sot.name)
    #
    # def test_get_image(self):
    #     image = self._get_non_test_image()
    #     self.assertIsNotNone(image)
    #     sot = self.conn.compute.get_image(image.id)
    #     self.assertEqual(image.id, sot.id)
    #     self.assertEqual(image.name, sot.name)
    #     self.assertIsNotNone(image.links)
    #     self.assertIsNotNone(image.min_disk)
    #     self.assertIsNotNone(image.min_ram)
    #     self.assertIsNotNone(image.metadata)
    #     self.assertIsNotNone(image.progress)
    #     self.assertIsNotNone(image.status)

    def test_image_metadata(self):
        image = "e4b9a8fa-6634-4590-bf9a-8cfc3549f2c1"

        # delete pre-existing metadata
        # self.conn.compute.delete_image_metadata(image, image.metadata.keys())
        image = self.conn.compute.get_image_metadata(image)
        self.assertFalse(image.metadata)

        # # get metadata
        # image = self.conn.compute.get_image_metadata(image)
        # self.assertFalse(image.metadata)
        #
        # # set no metadata
        # self.conn.compute.set_image_metadata(image)
        # image = self.conn.compute.get_image_metadata(image)
        # self.assertFalse(image.metadata)
        #
        # # set empty metadata
        # self.conn.compute.set_image_metadata(image, k0='')
        # image = self.conn.compute.get_image_metadata(image)
        # self.assertFalse(image.metadata)
        #
        # # set metadata
        # self.conn.compute.set_image_metadata(image, k1='v1')
        # image = self.conn.compute.get_image_metadata(image)
        # self.assertTrue(image.metadata)
        # self.assertEqual(1, len(image.metadata))
        # self.assertIn('k1', image.metadata)
        # self.assertEqual('v1', image.metadata['k1'])
        #
        # # set more metadata
        # self.conn.compute.set_image_metadata(image, k2='v2')
        # image = self.conn.compute.get_image_metadata(image)
        # self.assertTrue(image.metadata)
        # self.assertEqual(2, len(image.metadata))
        # self.assertIn('k1', image.metadata)
        # self.assertEqual('v1', image.metadata['k1'])
        # self.assertIn('k2', image.metadata)
        # self.assertEqual('v2', image.metadata['k2'])
        #
        # # update metadata
        # self.conn.compute.set_image_metadata(image, k1='v1.1')
        # image = self.conn.compute.get_image_metadata(image)
        # self.assertTrue(image.metadata)
        # self.assertEqual(2, len(image.metadata))
        # self.assertIn('k1', image.metadata)
        # self.assertEqual('v1.1', image.metadata['k1'])
        # self.assertIn('k2', image.metadata)
        # self.assertEqual('v2', image.metadata['k2'])
        #
        # # delete metadata
        # self.conn.compute.delete_image_metadata(image, image.metadata.keys())
        # image = self.conn.compute.get_image_metadata(image)
        # self.assertFalse(image.metadata)
