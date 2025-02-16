# udacity_repo
This is a repository to gain familiarity with git and Github.

## Git Setup
Configuring user information used across all local repositories
* git commit -m “[descriptive message]”: commit your staged content as a new commit snapshot
* git config --global user.name “[firstname lastname]”: set a name that is identifiable for credit when review version history
* git config --global user.email “[valid-email]”: set an email address that will be associated with each history marker
* git config --global color.ui auto: set automatic command line coloring for Git for easy reviewing

## Basic git commands
* ls: get all files in current directory
* git clone url_to_github_repository: clone your repository to your local machine.
* git status
* git add project_one.py
* git commit -m ‘add project_one.py file’ 
* git push: frequently used to move local code to the cloud version of the repository
* git status
* rm -rf repository-name: remove a directory via terminal 

## Branching 
* git branch: will show all available branches
* git checkout -b develop: You want to both create a new branch called develop and move to it.
* git push --set-upstream origin develop: You make changes to your develop branch. You add and commit your changes. Now you would like your branch to be available on your remote repository (on Github).
* git checkout: used to move across branches that have already been created
* git branch -d develop: Consider you have opened a pull request and it has been reviewed and merged into master. You now would like to remove the local version of the branch.

## Git log
* git log: View the log history
* git checkout bc90f2cbc9dc4e802b46e7a153aa106dc9a88560: revert to a commit 
* git checkout develop: switch to develop branch
* git merge --no-ff friend_groups: Merge the friend_groups branch into the develop branch
* git push origin develop: Push your changes to the remote repository