#!/usr/bin/env python3
"""A github org client
"""
from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized
from unittest.mock import MagicMock
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
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
