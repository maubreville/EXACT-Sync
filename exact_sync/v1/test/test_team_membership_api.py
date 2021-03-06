# coding: utf-8

"""
    EXACT - API

    API to interact with the EXACT Server  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

from exact_sync.v1.api_client import ApiClient as client
from exact_sync.v1.api.team_membership_api import TeamMembershipApi  # noqa: E501
from exact_sync.v1.rest import ApiException


class TestTeamMembershipApi(unittest.TestCase):
    """TeamMembershipApi unit test stubs"""

    def setUp(self):
        self.api = TeamMembershipApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_team_membership(self):
        """Test case for create_team_membership

        """
        assert False

    def test_destroy_team_membership(self):
        """Test case for destroy_team_membership

        """
        assert False

    def test_list_team_memberships(self):
        """Test case for list_team_memberships

        """
        team_memberships = self.api.list_team_memberships()        
        pass

    def test_partial_update_team_membership(self):
        """Test case for partial_update_team_membership

        """
        assert False

    def test_retrieve_team_membership(self):
        """Test case for retrieve_team_membership

        """
        team_memberships = self.api.list_team_memberships()  
        team_membership = team_memberships.results[0]
        self.api.retrieve_team_membership(id=team_membership.id)

        pass

    def test_update_team_membership(self):
        """Test case for update_team_membership

        """
        assert False


if __name__ == '__main__':
    unittest.main()
