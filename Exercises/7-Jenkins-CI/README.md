# Exercise 7: Jenkins CI Pipeline

## Objective

To implement a Continuous Integration (CI) pipeline using Jenkins that retrieves source code from GitHub, checks project files, and executes automated Python unit tests.

## Tools and Technologies

* Jenkins
* Docker
* Git and GitHub
* Python 3
* Python `unittest` framework
* Declarative Jenkins Pipeline

## Procedure

1. Started Jenkins using Docker and completed the initial Jenkins setup.
2. Created a Jenkins Pipeline job named `Exercise-7-Jenkins-CI`.
3. Connected the job to the GitHub repository using Pipeline Script from SCM.
4. Configured the pipeline to use `Exercises/7-Jenkins-CI/Jenkinsfile`.
5. Created Python unit tests in `tests/test_pipeline.py`.
6. Configured the pipeline to check out the repository, verify project files, and execute the Python tests.
7. Enabled Poll SCM to periodically check for repository changes and trigger a build when a new commit is detected.
8. Committed and pushed changes to GitHub using Git commands in the terminal.

## Pipeline Stages

### 1. Checkout

Displays the exercise name and runs as part of the Jenkins pipeline after source checkout.

### 2. Build

Lists the checked-out project files and verifies that the `Exercises` directory exists.

### 3. Test

Runs Python unit tests using the command:

`python3 -m unittest discover -s Exercises/7-Jenkins-CI/tests -p "test_*.py"`

The tests verify the pipeline message and exercise number.

## Result

The Jenkins pipeline successfully checked out the GitHub repository, verified the project structure, and executed two Python unit tests. Poll SCM was also verified by observing Jenkins automatically trigger a build after a repository change.

## Conclusion

A Jenkins Continuous Integration pipeline was implemented successfully with GitHub integration and automated Python testing. The exercise demonstrates source control integration, automated build execution, test discovery, and change-based build triggering.

