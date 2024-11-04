#!/usr/bin/env python3
"""Unittests for utils.py"""
from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized
from typing import Mapping, Sequence, Any
from utils import get_json, access_nested_map, memoize
# access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(TestCase):
    """TestAccessNestedMap class"""

    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Mapping,
                               path: Sequence,
                               expected: Any
                               ) -> None:
        """Test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',), KeyError),
        ({'a': 1}, ('a', 'b'), KeyError)
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: Sequence,
                                         expected: Exception
                                         ) -> None:
        """Test access_nested_map function with exception"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """TestGetJson class"""

    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False})
    ])
    @patch('requests.get')
    def test_get_json(self,
                      url: str,
                      payload: Mapping,
                      mock_get
                      ) -> None:
        """Test get_json function"""
        mock_get.return_value.json.return_value = payload
        self.assertEqual(get_json(url), payload)


class TestMemoize(TestCase):
    """TestMemoize class"""

    def test_memoize(self) -> None:
        """Test memoize function"""

        class TestClass:
            
            def a_method(self):
                return 42
            
            @memoize
            def a_property(self):
                return self.a_method()
        
        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            tc = TestClass()
            self.assertEqual(tc.a_property, 42)
            self.assertEqual(tc.a_property, 42)
            mock_method.assert_called_once()
