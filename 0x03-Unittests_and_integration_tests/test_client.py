#!/usr/bin/env python3
"""A github org client
"""
from unittest import TestCase
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from typing import Mapping, Dict
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """TestGithubOrgClient class
    """

    @parameterized.expand([
        ("google", {"response": "google"}),
        ("abc", {"response": "abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, response: Mapping,
                 mock_get_json) -> None:
        """Tests GithubOrgClient.org method returns correct value
        """
        mock_get_json.return_value = response
        gh = GithubOrgClient(org_name)
        self.assertEqual(gh.org, response)
        self.assertEqual(gh.org, response)

    @parameterized.expand([
        ("google"),
    ])
    @patch.object(GithubOrgClient, 'org', return_value={"repos_url": "google"})
    def test_public_repos_url(self, org_name: str, repos_url: Mapping) -> None:
        """Tests GithubOrgClient._public_repos_url method returns correct value
        """
        gh = GithubOrgClient(org_name)
        self.assertEqual(gh._public_repos_url, repos_url["repos_url"])

    @parameterized.expand([
        ('google', 'my_license', ['repo', 'old_repo']),
    ])
    @patch('client.get_json')
    @patch.object(GithubOrgClient, '_public_repos_url')
    def test_public_repos(self, org_name: str,
                          license: str,
                          expected: Mapping,
                          mock_public_repos_url,
                          mock_get_json) -> None:
        """Tests GithubOrgClient.public_repos method returns correct value
        """
        url = 'https://api.github.com/users/google/repos'
        payload = [
            {"name": "repo", "license": {"key": "my_license"}},
            {"name": "pub_repo", "license": {"key": "pub_license"}},
            {"name": "old_repo", "license": {"key": "my_license"}}
            ]

        mock_public_repos_url.return_value = url
        mock_get_json.return_value = payload

        gh = GithubOrgClient(org_name)
        self.assertEqual(gh.public_repos(license), expected)
        mock_get_json.assert_called_once()
        mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: Dict[str, Dict], license: str,
                         expected: bool) -> None:
        """Tests GithubOrgClient.has_license method returns correct output"""
        gh = GithubOrgClient("google")
        self.assertEqual(gh.has_license(repo, license), expected)
