#!/usr/bin/env python3

"""
This module contains unit tests for the GithubOrgClient
class in the client module.

Author: [Fabrice Eklou]
Date: [June 30, 2024]
"""

import unittest
from unittest.mock import Mock, MagicMock, patch, PropertyMock
from parameterized import parameterized, param
from client import GithubOrgClient
from utils import get_json
from typing import List, Dict, Union


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

    @parameterized.expand([
        param(org_name='google'),
        param(org_name='abc')
    ])
    def test_public_repos_url(self, org_name: str) -> None:
        """
        Test case to verify the correctness of the _public_repos_url
        property in the GithubOrgClient class.

        Args:
            org_name (str): The name of the organization.

        Returns:
            None
        """

        repos_url = 'https://api.github.com/orgs/{}/repos'.format(
            org_name)
        payload = {'repos_url': repos_url}
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = payload
            github_client = GithubOrgClient(org_name)

            self.assertEqual(github_client._public_repos_url, repos_url)
            mock_org.assert_called_once()

    @parameterized.expand([
        param(license='MIT', name='NestJS'),
        param(license=None, name='xclr')
    ])
    @patch('client.get_json')
    def test_public_repos(
            self, mock_get_json, license: Union[str, None], name: str):
        """
        Test case for the public_repos method of the GithubOrgClient class.

        Args:
            mock_get_json (MagicMock): A mock object for the get_json method.
            license (Union[str, None]): The license key for the repository.
                Can be None.
            name (str): The name of the repository.

        Returns:
            None
        """

        payload = [
            {'name': name,
             'license': {'key': license} if license else None}
        ]
        mock_get_json.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_pru:
            mock_pru.return_value = 'http://xclr.io'

            github_client = GithubOrgClient('xclr')

            self.assertEqual(github_client.public_repos(license), [name])
            mock_get_json.assert_called_once_with('http://xclr.io')
            mock_pru.assert_called_once()


if __name__ == '__main__':
    unittest.main()
