# -*- coding: utf-8 -*-
import unittest


class UtilityTestCase(unittest.TestCase):

    def test_object_dict(self):
        from apiutils.utils import ObjectDict
        obj = ObjectDict()
        self.assertTrue(obj.xxx is None)
        obj.xxx = 1
        self.assertEqual(1, obj.xxx)
