#!/usr/bin/python3
"""
Test for `Base` class
"""
import unittest
import pep8
import inspect
from models import base
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """
    Tests for `Base` class
    """
    @classmethod
    def setUp(cls):
        """ Need class funcs to test for docstrings """
        cls.funcs = inspect.getmembers(Base, inspect.isfunction)

    def test_pep8(self):
        """
        Test pep8 conformance.
        https://pep8.readthedocs.io/en/release-1.7.x/advanced.html
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result1 = pep8style.check_files(['models/base.py'])
        result2 = pep8style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(result1.total_errors, 0,
                         "Found code style errors in base.py.")
        self.assertEqual(result2.total_errors, 0,
                         "Found code style errors in test_base.py.")

    def test_docstring(self):
        """
        Test for docstrings at module, class, and function level
        """
        self.assertTrue(len(base.__doc__) > 0)
        self.assertTrue(len(Base.__doc__) > 0)
        for func in self.funcs:
            self.assertTrue(len(func[1].__doc__) > 0)

    def test_none_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_valid_id(self):
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)

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
