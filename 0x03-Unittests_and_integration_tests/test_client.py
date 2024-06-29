#!/usr/bin/env python3

"""
This module contains unit tests for the GithubOrgClient
class in the client module.

Author: [Fabrice Eklou]
Date: [June 29, 2024]
"""

import unittest
from unittest.mock import Mock, MagicMock, patch
from parameterized import parameterized, param
from client import GithubOrgClient
from utils import get_json
from typing import List, Dict


class TestGithubOrgClient(unittest.TestCase):
    """
    Test class for the GithubOrgClient class.

    This class contains test cases for the org method of the
    GithubOrgClient class.
    """

    @parameterized.expand([
        param(org_name='google'),
        param(org_name='abc')
    ])
    @patch('client.get_json')
    def test_org(self, mock_get_json, org_name: str) -> None:
        """
        Test case for the org method of the GithubOrgClient class.

        Args:
            mock_get_json: Mock object for the get_json function.
            org_name: Name of the organization.

        Returns:
            None

        Raises:
            AssertionError: If the org attribute of the GithubOrgClient
                instance is not equal to the expected payload.
            AssertionError: If the get_json function is not called with
                the expected URL.
        """
        payload = {'repos_urls': 'https://api.github.com/orgs/{}/repos'
                   .format(org_name)}

        mock_get_json.return_value = payload
        github_client = GithubOrgClient(org_name)

        self.assertEqual(github_client.org, payload)
        mock_get_json.assert_called_once_with(
            'https://api.github.com/orgs/{}'.format(org_name))


if __name__ == '__main__':
    unittest.main()
