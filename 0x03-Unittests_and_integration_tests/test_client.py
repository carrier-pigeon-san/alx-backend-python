#!/usr/bin/env python3
"""A github org client
"""
from unittest import TestCase
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from typing import Mapping
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
