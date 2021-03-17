# -*- coding: utf-8 -*-
"""
Created on Thu Mar 05 13:44:00 2021
The primary goal of this file is to demonstrate a simple unittest implementation

@author: dagrawa2
"""

from Githubapi567HW04a import getGithubRepoURL, getGithubRepoCommitsURL, getGithubResponse, getGithubRepos, getGithubRepoCommits, getGitHubReposAndCommitsForAUser
import unittest
import json
import time
from unittest import mock
from unittest.mock import Mock, patch

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestGithubapi567HW04a(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def test_GetGithubRepoURL_GettingFormedCorrectlyUsingGithubID(self): 
        self.assertEqual(getGithubRepoURL('richkempinski'),'https://api.github.com/users/richkempinski/repos')

    def test_GetGithubRepoURL_ThrowingExceptionWhenGithubIDNotProvided(self): 
        self.assertRaises(Exception,'GithubID not provided' ,getGithubRepoURL, None)

    def test_GetGithubRepoCommitsURL_GettingFormedCorrectlyUsingGithubIDAndRepo(self): 
        self.assertEqual(getGithubRepoCommitsURL('richkempinski','hellogitworld'),'https://api.github.com/repos/richkempinski/hellogitworld/commits')

    def test_GetGithubRepoCommitsURL_ThrowingExceptionWhenGithubIDNotProvided(self): 
        self.assertRaises(Exception,'Either githubID or githubRepo not provided' ,getGithubRepoCommitsURL, None, 'hellogitworld')

    def test_GetGithubRepoCommitsURL_ThrowingExceptionWhenGithubRepoNotProvided(self): 
        self.assertRaises(Exception,'Either githubID or githubRepo not provided' ,getGithubRepoCommitsURL, 'richkempinski', None)

    def test_GetGithubResponse_returningResponseOfTypeJSON(self): 
        mock_get_patcher = patch('Githubapi567HW04a.requests.get')
        mock_get = mock_get_patcher.start()
        githubResponse = [
        {
        "name": "csp"
        },
        {
        "name": "hellogitworld"
        },
        {
        "name": "helloworld"
        },
        {
        "name": "Mocks"
        },
        {
        "name": "Project1"
        },
        {
        "name": "richkempinski.github.io"
        },
        {
        "name": "threads-of-life"
        },
        {
        "name": "try_nbdev"
        },
        {
        "name": "try_nbdev2"
        }
        ]
        #self.mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = githubResponse
        mock_get.return_value.ok = True
        mock_get.return_value.status_code = 200
        response = getGithubResponse('https://api.github.com/users/richkempinski/repos')
        mock_get_patcher.stop()
        self.assertIsInstance(response, list)

    def test_GetGithubResponse_SizeIsGreatherThan0(self): 
        mock_get_patcher = patch('Githubapi567HW04a.requests.get')
        mock_get = mock_get_patcher.start()
        githubResponse = [
        {
        "name": "csp"
        },
        {
        "name": "hellogitworld"
        },
        {
        "name": "helloworld"
        },
        {
        "name": "Mocks"
        },
        {
        "name": "Project1"
        },
        {
        "name": "richkempinski.github.io"
        },
        {
        "name": "threads-of-life"
        },
        {
        "name": "try_nbdev"
        },
        {
        "name": "try_nbdev2"
        }
        ]
        #self.mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = githubResponse
        mock_get.return_value.ok = True
        mock_get.return_value.status_code = 200
        response = getGithubResponse('https://api.github.com/users/richkempinski/repos')
        mock_get_patcher.stop()
        self.assertNotEqual(len(response), 0)
        self.assertIsNotNone(response)

    def test_GetGithubRepos_SizeIsGreatherThan0(self):
        mock_get_patcher = patch('Githubapi567HW04a.requests.get')
        mock_get = mock_get_patcher.start()
        githubResponse = [
        {
        "name": "csp"
        },
        {
        "name": "hellogitworld"
        },
        {
        "name": "helloworld"
        },
        {
        "name": "Mocks"
        },
        {
        "name": "Project1"
        },
        {
        "name": "richkempinski.github.io"
        },
        {
        "name": "threads-of-life"
        },
        {
        "name": "try_nbdev"
        },
        {
        "name": "try_nbdev2"
        }
        ]
        #self.mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = githubResponse
        mock_get.return_value.ok = True
        mock_get.return_value.status_code = 200
        response = getGithubRepos('richkempinski')
        mock_get_patcher.stop()
        self.assertNotEqual(len(response), 0)
        self.assertIsNotNone(response)

    def test_GetGithubRepos_returningResponseOfTypeList(self): 
        mock_get_patcher = patch('Githubapi567HW04a.requests.get')
        mock_get = mock_get_patcher.start()
        githubResponse = [
        {
        "name": "csp"
        },
        {
        "name": "hellogitworld"
        },
        {
        "name": "helloworld"
        },
        {
        "name": "Mocks"
        },
        {
        "name": "Project1"
        },
        {
        "name": "richkempinski.github.io"
        },
        {
        "name": "threads-of-life"
        },
        {
        "name": "try_nbdev"
        },
        {
        "name": "try_nbdev2"
        }
        ]
        #self.mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = githubResponse
        mock_get.return_value.ok = True
        mock_get.return_value.status_code = 200
        response = getGithubRepos('richkempinski')
        mock_get_patcher.stop()
        self.assertIsInstance(response, list)

    def test_GetGithubRepos_ThrowingExceptionWhenIncorrectUserProvided(self): 
        self.assertRaises(Exception,'Github user not found' ,getGithubRepos, None)

    def test_GetGithubRepos_SizeIs0WhenRepoNotFound(self):
        mock_get_patcher = patch('Githubapi567HW04a.requests.get')
        mock_get = mock_get_patcher.start()
        githubResponse = []
        #self.mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = githubResponse
        mock_get.return_value.ok = True
        mock_get.return_value.status_code = 200
        response = getGithubRepos('sdfsdf')
        mock_get_patcher.stop()
        self.assertEqual(len(response), 0)

    def test_GetGithubRepoCommits_SizeIsGreatherThan0(self):
        mock_get_patcher = patch('Githubapi567HW04a.requests.get')
        mock_get = mock_get_patcher.start()
        githubResponse = [{},{},{},{}]
        #self.mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = githubResponse
        mock_get.return_value.ok = True
        mock_get.return_value.status_code = 200
        response = getGithubRepoCommits('richkempinski','hellogitworld')
        mock_get_patcher.stop()
        self.assertNotEqual(response, 0)
        self.assertIsNotNone(response)

    def test_GetGithubRepoCommits_returningResponseOfTypeInt(self): 
        mock_get_patcher = patch('Githubapi567HW04a.requests.get')
        mock_get = mock_get_patcher.start()
        githubResponse = [{},{},{},{}]
        #self.mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = githubResponse
        mock_get.return_value.ok = True
        mock_get.return_value.status_code = 200
        response = getGithubRepoCommits('richkempinski','hellogitworld')
        mock_get_patcher.stop()
        self.assertIsInstance(response, int)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

