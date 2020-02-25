"""
Homework 05a - Isolate External Dependencies
Zephyr Zambrano

"""


import urllib.request
import json


def get_input(prompt):
    """ Gets input from the user. Keeps asking the user for input until they enter something. """
    while True: #makes sure the user enters something before going through the rest of the code
        s = input(prompt)
        if s == "": #handles the user pressing enter without typing text first
            print("\nOops! You forgot to enter some text! Please try again.")
        else:
            return s


def get_repo_data(user):
    """ Submits a request to the GitHub API to get the repository data from a specific
    GitHub user. Parses this data and returns a list of repos for that specific user.
    
    API Link: https://api.github.com/users/<ID>/repos
    """
    
    beginning = "https://api.github.com/users/"
    end = "/repos"

    url = beginning + user + end

    data = ""

    try: # attempts to send a request to the API
        data = urllib.request.urlopen(url).read().decode()
    except ValueError as e: # request is unsuccessful
        raise ValueError("Website cannot be reached. Please try again with valid input data.")
    else: # parse and return data
        data = json.loads(data)
        repo_list = []
        for item in data:
            for key, value in item.items():
                if key == "name":
                    repo_list.append(value)
        return repo_list


def get_commit_data(user, repo):
    """ Submits a request to the GitHub API to get the number of commits for
    a repository on a specific user's GitHub account. Parses this data and
    returns the number of commits in a specific repository.
    
    API Link: https://api.github.com/repos/<ID>/<REPO>/commits
    """
    
    beginning = "https://api.github.com/repos/"
    end = "/commits"

    url = beginning + user + "/" + repo + end

    data = ""

    try: # attempts to send a request to the API
        data = urllib.request.urlopen(url).read().decode()
    except ValueError as e: # request is unsuccessful
        raise ValueError("Website cannot be reached. Please try again with valid input data.")
    else: # parse and return data
        data = json.loads(data)
        return len(data)


def main():
    """ Gets repository and commit data from a specific GitHub user,
    and prints this data to the user. """

    print("Please enter a GitHub ID: \n")
    i = get_input("Enter text: ")
    print()
    repo_list = get_repo_data(i)

    # repo_list = get_repo_data("zephyrzambrano")
    # print(repo_list)

    commit_dict = {}

    for repo in repo_list:
        commits = get_commit_data("zephyrzambrano", repo)
        commit_dict[repo] = commits
    # print(commit_dict)

    for key, value in commit_dict.items():
        print(f"Repo: {key} -> Number of commits: {value}")


if __name__ == "__main__":
    main()
