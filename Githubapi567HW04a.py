import requests
import json
"""
Created on Thu Mar 05 13:44:00 2021
You should write a function that will take as input a GitHub user ID. 
The output from the function will be a list of the names of the repositories that the user has, 
along with the number of commits that are in each of the listed repositories.

@author: dagrawa2 (Deeptidevi Agrawal)
"""

def getGithubID():
    githubID = input('Enter a GitHub ID: ')
    return githubID

def getGithubRepoURL(githubID):
    if githubID is None:
        raise Exception("GithubID not provided")
    return "https://api.github.com/users/%s/repos" %(githubID)

def getGithubRepoCommitsURL(githubID, githubRepo):
    if githubID is None or githubRepo is None:
        raise Exception("Either githubID or githubRepo not provided")
    return "https://api.github.com/repos/%s/%s/commits" %(githubID, githubRepo)

def getGithubResponse(githubURL):
    try:
        githubResponse = requests.get(githubURL)
        if githubResponse.status_code == 404:
            raise Exception("Github user not found")
        if githubResponse.status_code >= 400:
            raise Exception("Server error")
    except requests.HTTPError:
        raise Exception("HTTPError - invalid HTTP responses")
    except requests.ConnectionError:
        raise Exception("ConnectionError - network problem")
    except requests.Timeout:
        raise Exception("Timeout - request timed out")   

    return githubResponse.json()

def getGithubRepos(githubID):
    try: 
        repoResponse = getGithubResponse(getGithubRepoURL(githubID))
        githubRepos = []
        for repo in repoResponse:
            githubRepos.append(repo['name'])
    except Exception:
        raise
    return githubRepos

def getGithubRepoCommits(githubID, githubRepo):
    try: 
        commitResponse = getGithubResponse(getGithubRepoCommitsURL(githubID, githubRepo))       
    except Exception:
        raise
    return len(commitResponse)

def getGitHubReposAndCommitsForAUser(githubID):
    commitsPerRepo = []
    userRepos = getGithubRepos(githubID)
    for repo in userRepos:
        commitCount = getGithubRepoCommits(githubID,repo)
        commitsPerRepo.append('Repo: '+repo+' Number of commits: '+str(commitCount))
        #print(f'Repo: {repo} Number of commits: {commitCount}')
    return commitsPerRepo

def getGitHubReposAndCommits():
    githubUserID = getGithubID()
    commitsPerRepo = getGitHubReposAndCommitsForAUser(githubUserID)   
    for each in commitsPerRepo:
        print(each)
 
#getGitHubReposAndCommits()
#getGitHubReposAndCommitsForAUser("richkempinski")