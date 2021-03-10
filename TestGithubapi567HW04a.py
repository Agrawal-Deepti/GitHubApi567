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

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestGithubapi567HW04a(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def test_GetGithubRepoURL_GettingFormedCorrectlyUsingGithubID(self): 
        time.sleep(5)
        self.assertEqual(getGithubRepoURL('richkempinski'),'https://api.github.com/users/richkempinski/repos')

    def test_GetGithubRepoURL_ThrowingExceptionWhenGithubIDNotProvided(self): 
        time.sleep(5)
        self.assertRaises(Exception,'GithubID not provided' ,getGithubRepoURL, None)

    def test_GetGithubRepoCommitsURL_GettingFormedCorrectlyUsingGithubIDAndRepo(self): 
        time.sleep(5)
        self.assertEqual(getGithubRepoCommitsURL('richkempinski','hellogitworld'),'https://api.github.com/repos/richkempinski/hellogitworld/commits')

    def test_GetGithubRepoCommitsURL_ThrowingExceptionWhenGithubIDNotProvided(self): 
        time.sleep(5)
        self.assertRaises(Exception,'Either githubID or githubRepo not provided' ,getGithubRepoCommitsURL, None, 'hellogitworld')

    def test_GetGithubRepoCommitsURL_ThrowingExceptionWhenGithubRepoNotProvided(self): 
        time.sleep(5)
        self.assertRaises(Exception,'Either githubID or githubRepo not provided' ,getGithubRepoCommitsURL, 'richkempinski', None)

    def test_GetGithubResponse_ThrowingExceptionWhenIncorrectURLProvided(self): 
        time.sleep(5)
        self.assertRaises(Exception,'Github user not found' ,getGithubResponse, 'https://api.github.com/users//repos')

    def test_GetGithubResponse_returningResponseOfTypeJSON(self): 
        time.sleep(5)
        self.assertIsInstance(getGithubResponse('https://api.github.com/users/richkempinski/repos'), list)

    def test_GetGithubResponse_SizeIsGreatherThan0(self): 
        time.sleep(5)
        self.assertNotEqual(len(getGithubResponse('https://api.github.com/users/richkempinski/repos')), 0)
        self.assertIsNotNone(getGithubResponse('https://api.github.com/users/richkempinski/repos'))

    def test_GetGithubRepos_SizeIsGreatherThan0(self):
        time.sleep(5)
        self.assertNotEqual(len(getGithubRepos('richkempinski')), 0)
        self.assertIsNotNone(getGithubRepos('richkempinski'))

    def test_GetGithubRepos_returningResponseOfTypeList(self): 
        time.sleep(5)
        self.assertIsInstance(getGithubRepos('richkempinski'), list)

    def test_GetGithubRepos_ThrowingExceptionWhenIncorrectUserProvided(self): 
        time.sleep(5)
        self.assertRaises(Exception,'Github user not found' ,getGithubRepos, None)

    def test_GetGithubRepos_SizeIs0WhenRepoNotFound(self):
        time.sleep(5)
        self.assertEqual(len(getGithubRepos('sdfsdf')), 0)

    def test_GetGithubRepoCommits_SizeIsGreatherThan0(self):
        time.sleep(5)
        self.assertNotEqual(getGithubRepoCommits('richkempinski','hellogitworld'), 0)
        self.assertIsNotNone(getGithubRepoCommits('richkempinski','hellogitworld'))

    def test_GetGithubRepoCommits_returningResponseOfTypeInt(self): 
        time.sleep(5)
        self.assertIsInstance(getGithubRepoCommits('richkempinski','hellogitworld'), int)

    def test_GetGithubRepoCommits_ThrowingExceptionWhenIncorrectUserRepoProvided(self): 
        time.sleep(5)
        self.assertRaises(Exception,'Github user not found' ,getGithubRepoCommits, None, None)

    def test_GetGithubRepoCommits_SizeIs0WhenRepoNotFound(self):
        time.sleep(5)
        self.assertEqual(getGithubRepoCommits('sdfsdf','hellogitworld'), 0)

    def test_getGitHubReposAndCommitsForAUser_returningResponseOfTypeList(self): 
        time.sleep(5)
        self.assertIsInstance(getGitHubReposAndCommitsForAUser('richkempinski'), list)

    def test_getGitHubReposAndCommitsForAUser_ThrowingExceptionWhenIncorrectUserRepoProvided(self):
        time.sleep(5)
        self.assertRaises(Exception,'Github user not found' ,getGitHubReposAndCommitsForAUser, None)

    def test_getGitHubReposAndCommitsForAUser_SizeIs0WhenRepoNotFound(self):
        time.sleep(5)
        self.assertEqual(len(getGitHubReposAndCommitsForAUser('sdfsdf')), 0)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

