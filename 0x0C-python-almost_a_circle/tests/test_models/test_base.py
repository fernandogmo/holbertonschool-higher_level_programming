#!/usr/bin/python3
"""
Test for `Base` class
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """
    """
    def setup(self):
        pass

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


if __name__ == '__main__':
    pass
