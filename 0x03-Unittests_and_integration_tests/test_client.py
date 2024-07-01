#!/usr/bin/env python3

"""
This module contains unit tests for the GithubOrgClient
class in the client module.

Author: [Fabrice Eklou]
Date: [June 30, 2024]
"""

import unittest
from unittest.mock import Mock, MagicMock, patch, PropertyMock
from parameterized import parameterized, param, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
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
            {"name": "NestJS", "license": {"key": "MIT"}},
            {"name": "ReactJS", "license": {"key": "apache-2.0"}},
            {"name": "PostgreSQL", "license": {"key": "BSD"}},
        ]
        mock_get_json.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_pru:
            mock_pru.return_value = 'http://xclr.io'

            github_client = GithubOrgClient('xclr')
            repos = github_client.public_repos()

            self.assertEqual(repos, ["NestJS", "ReactJS", "PostgreSQL"])
            mock_get_json.assert_called_once_with('http://xclr.io')
            mock_pru.assert_called_once()

    @parameterized.expand([
        param(repo={"license": {"key": "my_license"}},
              license_key="my_license",
              expected=True),
        param(repo={"license": {"key": "other_license"}},
              license_key="my_license",
              expected=False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test the `has_license` method of the GithubOrgClient class.

        Args:
            repo (str): The name of the repository to check
                for the license.
            license_key (str): The license key to check for.
            expected (bool): The expected result of the
                `has_license` method.

        Returns:
            None

        Raises:
            AssertionError: If the actual result of the `has_license`
                method does not match the expected result.
        """
        has_license = GithubOrgClient.has_license(repo, license_key)
        if expected:
            self.assertTrue(has_license)
        else:
            self.assertFalse(has_license)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    A test case class for integration testing the GithubOrgClient class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test class before running any test cases.

        This method is called once before any test cases in the
        test class are executed.
        It is used to perform any necessary setup steps that are
        common to all test cases.

        Args:
            cls: The class object representing the test class.

        Returns:
            None
        """
        cls.get_patcher = patch(
            'requests.get', side_effect=cls.mocked_requests_get)
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """
        This method is called after all the test methods
        in the test case have been run.
        It is used to perform any necessary clean-up actions,
        such as stopping patchers or closing resources.
        """
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
