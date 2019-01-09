#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest class for max_integer function"""
    def setUp(self):
        pass

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_ascending(self):
        self.assertEqual(max_integers([1, 2, 3]), 3)

    def test_descending(self):
        self.assertEqual(max_integers([3, 2, 1]), 3)

    def tearDown(self):
        pass
