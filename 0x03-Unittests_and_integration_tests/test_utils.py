#!/usr/bin/env python3

"""
This module contains unit tests for the utility functions
in the 'utils' module.

The utility functions being tested are:
- access_nested_map: A function that retrieves a value
    from a nested map given a path.
- get_json: A function that retrieves JSON data from a given URL.
- memoize: A decorator that caches the return
    value of a method or property.

The unit tests are implemented using the 'unittest'
module and the 'parameterized' library.

Author: [Fabrice Eklou]
Date: [June 28, 2024]
"""


import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, param
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any, Dict, Callable


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case class for the access_nested_map function.
    """

    @parameterized.expand([
        param(nested_map={"a": 1}, path=("a",), expected=1),
        param(nested_map={"a": {"b": 2}}, path=("a",), expected={"b": 2}),
        param(nested_map={"a": {"b": 2}}, path=("a", "b"), expected=2)
    ])
    def test_access_nested_map(self,
                               nested_map: Mapping, path: Sequence,
                               expected: Any) -> None:
        """
        Test the access_nested_map function with different inputs.

        Args:
            nested_map (Mapping): The nested map to access.
            path (Sequence): The path to the desired value.
            expected (Any): The expected value.

        Returns:
            None
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        param(nested_map={}, path=("a",), key="a"),
        param(nested_map={"a": 1}, path=("a", "b"), key="b")
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping, path: Sequence,
                                         key: str) -> None:
        """
        Test the access_nested_map function for raising KeyError.

        Args:
            nested_map (Mapping): The nested map to access.
            path (Sequence): The path to the desired value.
            key (str): The key that should raise KeyError.

        Returns:
            None
        """
        with self.assertRaises(KeyError, msg=f"KeyError: ('{key}')") as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(cm.msg, f"KeyError: ('{key}')")


class TestGetJson(unittest.TestCase):
    """
    Test case for the get_json function.
    """

    @parameterized.expand([
        param(url="http://example.com", payload={"payload": True}),
        param(url="http://holberton.io", payload={"payload": False})
    ])
    def test_get_json(self, url: str, payload: Dict) -> None:
        """
        Test the get_json function with different URLs and payloads.

        Args:
            url (str): The URL to send the request to.
            payload (dict): The expected JSON response payload.

        Returns:
            None
        """
        with patch('requests.get') as mock_get:
            # Create a mock response object with the desired properties
            mock_res = Mock()
            mock_res.json.return_value = payload
            mock_get.return_value = mock_res

            json_response = get_json(url)

            mock_get.assert_called_once_with(url)
            self.assertEqual(json_response, payload)


class TestMemoize(unittest.TestCase):
    """
    Test case for the memoize decorator.

    The TestMemoize class contains test cases for
    the memoize decorator.
    """

    def test_memoize(self) -> None:
        """
        Test the memoize decorator.

        This test case verifies the functionality of the memoize decorator.
        It creates an instance of the TestClass and
        calls its `a_method` method.
        Then it patches the `a_method` method with a mock object
        and calls the `a_property` property twice.
        Finally, it asserts that the results of both calls are equal
        to the return value of `a_method`.
        """

        class TestClass:
            """
            This is a test class used for testing purposes.
            """

            def a_method(self) -> int:
                """
                This method returns the value 42.
                """
                return 42

            @memoize
            def a_property(self) -> int:
                """
                This property returns the value of the a_method() method.
                """
                return self.a_method()

        test_class_object = TestClass()
        return_value = test_class_object.a_method()

        with patch.object(test_class_object, 'a_method',
                          return_value=return_value) as mock_prop:
            result1 = test_class_object.a_property
            result2 = test_class_object.a_property

            self.assertEqual(result1, return_value)
            self.assertEqual(result2, return_value)

            mock_prop.assert_called_once()


if __name__ == '__main__':
    unittest.main()
