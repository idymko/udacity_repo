# udacity_repo
This is a repository to gain familiarity with git and Github.

## Git Setup
Configuring user information used across all local repositories
* git commit -m “[descriptive message]”: commit your staged content as a new commit snapshot
* git config --global user.name “[firstname lastname]”: set a name that is identifiable for credit when review version history
* git config --global user.email “[valid-email]”: set an email address that will be associated with each history marker
* git config --global color.ui auto: set automatic command line coloring for Git for easy reviewing

## Basic git commands
* ls
* git clone url_to_github_repository: clone your repository to your local machine.
* git status
* git add project_one.py
* git commit -m ‘add project_one.py file’ 
* git push 
* git status
* rm -rf repository-name

## Branching 
* git branch: will show all available branches
* git branch: which shows all the branches you have available
* git checkout -b develop: You want to both create a new branch called develop and move to it.
* git push --set-upstream origin develop: You make changes to your develop branch. You add and commit your changes. Now you would like your branch to be available on your remote repository (on Github).
* git branch -d develop: Consider you have opened a pull request and it has been reviewed and merged into master. You now would like to remove the local version of the branch.
