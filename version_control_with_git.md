# Version Control with Git

Tarun Kumar, *Core Member DSC@DSU*

# Some questions to derive version control systems

- How do you share your code with your project partner?
    - Upload it somewhere? (Google Drive, email etc)
    - Share using USB or other hardware media?
- Can the above discussed methods allow the following:
    - Make changes to the code in parallel to you and simultaneously synchronize (without sharing the code back and forth)?
    - Keep track of whatever changes s(he) are making? (Code added/deleted/modified)
    - Know why those changes were made without them explicitly going over all the changes they made?
    - Move back to an older version of code after noticing the new changes are unwanted (causing bugs or are otherwise, we're talking hundreds of code lines added)

## What is a Version Control system?

- Tools to keep track of changes (history) of a directory and it's containing files

    (usually in our cases, ***Source Codes***)

- Keep information(metadata) about those changes
- So in short, something we need to properly collaborate and contribute.
    - Features of a version control system
        - Code collaboration
        - Keep a history of versions
        - Keeping metadata about versions (who, when, why, which/what)
        - Moving back and forth versions
        - and much more..
    - Examples of all commit VCS:
        - Google Docs
        - Notion

## What is Git?

Most commonly used Version Control system and the one we'll deep dive today.

Created by Linus Torvalds, the same guy behind ***Linux*** operating system.

Subversion, Mercurial are also famous version control systems.

## *And how does Git work?*

- **Git Data Model**
    - History as **Directed Acyclic Graphs (DAG)**
        - **Snapshots** (trees)

            or, more explicitly:

        - **Commits** (snapshots + metadata)
            - Parent (commit before)
            - Author
            - Message
            - Snapshot
    - **Repository**
        - A directory injected with Git version control
    - **Staging Area**
        - The place where you explicitly changes go before becoming a snapshot (a commit)

# Installing and integrating Git

Command-line interface

- Windows (CMD, Powershell)
- Linux/MacOS (Bash - zsh)

GUI based:

- Editor or IDE integration (Sublime, VSCode, Android Studio etc)
- [https://git-scm.com/downloads/guis](https://git-scm.com/downloads/guis)

# Working with git interface

- **Basic**

    - A description of command and it's usage:

        ```bash
        git help <command>
        ```

    - Initializing a git repository(local)

        ```bash
        git init
        ```

    - Adding files to staging area (to track their changes):

        ```bash
        git add <filename> #track a single file
        git add --all #track all files in the repository
        ```

    - Creating snapshots (commits)

        ```bash
        git commit
        git commit -m "message here" #write message without opening a editor
        ```

    - Checking the history of commits and changes we've made:

        ```bash
        git log
        git log -a --graph --decorate # A more beautiful way to visualize the tree
        git log -a --graph --decorate --oneline #Above but concise 
        ```

    - Checking specific differences we've made to tracked files (in ref with staging area):

        ```bash
        git diff <filename>
        git diff <commit> <filename> # difference between commits, not staging area
        ```

    - Creating a gitignore file
- **Collaborating and branching**

    - Creating an alternative branch in our current tree

        ```bash
        git branch # Shows all branches
        git branch <branch_name> # creates branch with name "branch_name" 
        ```

    - Working on branches

        ```bash
        git checkout <branch_name> # Change working branch to "branch_name"
        git checkout -b <branch_name> # Single command to create and checkout
        ```

    - Merging

        ```bash
        git merge <branch_name>

        # If you get conflicts during merging
        # and once you're done with fixing them: 
        git merge --continue
        ```

- **Remotes**

    - Show all the remotes where this repository is deployed

        ```bash
        git remote
        ```

    - Adding new remotes

        ```bash
        git remote add <remote_name> <url>
        ```

    - Pushing local repository changes to remote

        ```bash
        git push <remote> <local_branch>:<remote_branch>

        # in case upstream is not set up
        git branch --set-upstream-to=<remote>/<remote branch>
        # or setting upstream directly in pus
        ```

    - Syncing changes with remote

        ```bash
        git fetch # only retrieve changes
        git pull # git fetch and then merge
        ```

    - Starting from existing remote repository

        ```bash
        git clone <url>
        ```

# Working with Github interface

- Public vs private repositories
- Pull requests
- Difference between cloning and forking
- readme.md

# Things not covered?

- Open Source Licenses (what people can and cannot do with your code)
- Continuous Integration (auto deploy a piece of software once you push to a Github repo)
- Setting automated testing for Github repositories
- Some advanced commands worth looking into:

    ```bash
    git rebase # change merge tip from ancestor commit to something else
    git bisect # automate searching commit history in a binary fashion
    git stash # VERY useful to store changes
    git add -p # interactive adding, selecting which changes to add to staging
    ```

# Extra resources:

 

- Primary review source and motivation for this video, [Lecture 6: Version Control of Missing Semester](https://www.youtube.com/watch?v=2sjqTHE0zok)
- [Pro Git book](https://git-scm.com/book/en/v2) is the ultimate resource for learning and mastering Git, so it's suggested you read at least the first few chapters
- [Learn Git Branching](https://learngitbranching.js.org/) is for the ones who want to master the Git interface using interactive tutorials and tests.
- [Oh Shit, Git!?!](https://ohshitgit.com/) is exactly what you sound like when you make a mistake in Git (11 out of 10 times). A great resource as well to recover from those common pitfalls.
- [How to write good commit messages by FreeCodeCamp](https://www.freecodecamp.org/news/writing-good-commit-messages-a-practical-guide/) must watch guide on common commit message conventions to make the most out of your code contributions.