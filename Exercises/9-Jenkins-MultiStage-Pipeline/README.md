# Exercise 9: Jenkins Multi-Stage Pipeline

## Objective
To implement a Jenkins pipeline that builds, tests, deploys, and verifies a Python Flask application.

## Tools Used
- Jenkins
- Docker
- Python 3
- Flask
- Git and GitHub

## Pipeline Stages
1. Build: Create a Python virtual environment and install dependencies.
2. Test: Run unit tests using unittest.
3. Deploy: Copy the application files into the deployment directory.
4. Run Application: Start the Flask application.
5. Test Application: Verify the HTTP status and application response.

## Result
The Jenkins multi-stage pipeline executed successfully, and the deployed Flask application returned the expected response.

## Conclusion
Successfully implemented and tested a multi-stage Jenkins pipeline for a Python Flask application.
