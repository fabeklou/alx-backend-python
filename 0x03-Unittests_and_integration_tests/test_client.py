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
    A test case class for integration testing of the GithubOrgClient class.

    This class contains test methods to verify the functionality
    of the GithubOrgClient class
    for retrieving public repositories and their licenses
    from a GitHub organization.

    Attributes:
        org_payload (dict): A dictionary representing the
            organization payload.
        repos_payload (dict): A dictionary representing
            the repositories payload.
        expected_repos (list): A list of expected repositories.
        apache2_repos (list): A list of repositories
            with Apache 2.0 license.

    Methods:
        setUpClass(cls): A class method that sets up the necessary
            patching for the tests.
        tearDownClass(cls): A class method that stops the patching
            after the tests.
        test_public_repos(self): A test method to verify
            the public_repos() method.
        test_public_repos_with_license(self): A test method to verify
            the public_repos() method with a specific license.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the necessary patching for the tests.

        This class method is called before any test methods in the class.
        It sets up the patching for the 'requests.get'
        method to return the desired payloads.
        """
        cls.get_patcher = patch('requests.get',
                                **{'return_value.json.side_effect':
                                    [cls.org_payload, cls.repos_payload,
                                     cls.org_payload, cls.repos_payload]})

        cls.mock = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """
        Stop the patching after the tests.

        This class method is called after all test methods
        in the class have been run.
        It stops the patching for the 'requests.get' method.
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test the public_repos() method.

        This test method verifies that the public_repos()
        method of the GithubOrgClient class
        returns the expected repositories and makes the correct API calls.
        """
        github_client = GithubOrgClient("xclr")

        self.assertEqual(github_client.org, self.org_payload)
        self.assertEqual(github_client.repos_payload, self.repos_payload)
        self.assertEqual(github_client.public_repos(), self.expected_repos)
        self.assertEqual(github_client.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """
        Test the public_repos() method with a specific license.

        This test method verifies that the public_repos()
        method of the GithubOrgClient class
        returns the expected repositories with a specific license and makes
        the correct API calls.
        """
        github_client = GithubOrgClient("xclr")

        self.assertEqual(github_client.public_repos(),
                         self.expected_repos)
        self.assertEqual(github_client.public_repos("XLICENSE"), [])
        self.assertEqual(github_client.public_repos("apache-2.0"),
                         self.apache2_repos)
        self.mock.assert_called()


if __name__ == '__main__':
    unittest.main()
