
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code is available in the workspace'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the DevOps lab project'
                sh 'ls -la'
            }
        }

        stage('Test') {
            steps {
                echo 'Checking project files'
                sh 'test -d Exercises'
                sh 'find Exercises -type f'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
