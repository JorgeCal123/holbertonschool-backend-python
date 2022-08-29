#!/usr/bin/env python3
""" Unittest module """

import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """ Class TestAccessNestedMap """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """test access nested map"""
        answer = access_nested_map(map, path)
        self.assertEqual(answer, expected_output)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, wrong_output):
        """ test access nested map exception """
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(wrong_output, e.exception)


class TestGetJson(unittest.TestCase):
    """ test get json """
    # order of args: test_url, test_payload
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test get json """

        response = Mock()
        response.json.return_value = test_payload

        with patch('requests.get', return_value=response):
            real_response = get_json(test_url)
            self.assertEqual(real_response, test_payload)
            response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """ Class test memoize """

    def test_memoize(self):
        """ Tests memoize """

        class TestClass:
            """ Test class """

            def a_method(self):
                """ Method that return 42 """
                return 42

            @memoize
            def a_property(self):
                """ method property """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mocked:
            spec = TestClass()
            spec.a_property
            spec.a_property
            mocked.asset_called_once()
