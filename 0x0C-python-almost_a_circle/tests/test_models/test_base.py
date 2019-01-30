#!/usr/bin/python3
"""
Test for `Base` class
"""
import unittest
import pep8
from inspect import getdoc, getmembers, isfunction
from models import base
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """
    Tests for `Base` class
    """
    @classmethod
    def setUp(cls):
        """ Create a few objects """
        cls.b0 = Base()
        cls.b1 = Base(12)
        cls.b2 = Base()

    def tearDown(self):
        """ Reset object count after each test. """
        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_pep8(self):
        """
        Test pep8 conformance.
        https://pep8.readthedocs.io/en/release-1.7.x/advanced.html
        """
        file_msgs = [('models/base.py',
                      'Found code style errors in base.py.'),
                     ('tests/test_models/test_base.py',
                      'Found code style errors in test_base.py.')]
        for f, e in file_msgs:
            self.assertEqual(pep8.Checker(f).check_all(), 0, e)

    def test_docstring(self):
        """
        Test for docstrings at module, class, and function level
        """
        self.assertTrue(len(getdoc(base)) > 0)
        self.assertTrue(len(getdoc(Base)) > 0)
        for _, fn in getmembers(Base, isfunction):
            self.assertTrue(len(getdoc(fn)) > 0)

    def test_none_id(self):
        self.assertEqual(self.b0.id, 1)

    def test_valid_id(self):
        self.assertEqual(self.b1.id, 12)
        self.assertEqual(self.b2.id, 2)

    def test_none_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_empty_to_json_string(self):
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_bad_to_json_string(self):
        with self.assertRaises(TypeError):
            Base.to_json_string(9000)

    def test_valid_to_json_string(self):
        self.assertEqual(Base.to_json_string([{'a': 1}]), '[{"a": 1}]')

    def test_none_from_json_string(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_empty_from_json_string(self):
        self.assertEqual([], Base.from_json_string(""))

    # def test_bad_from_json_string(self):

    def test_valid_from_json_string(self):
        self.assertEqual([{'a': 1}], Base.from_json_string('[{"a": 1}]'))


if __name__ == '__main__':
    pass
