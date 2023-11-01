pipeline {
    agent any

    stages {
        stage('Code Quality') {
            steps {
                echo 'Checking code quality'
            }
        }

        stage('Unit Tests') {
            steps {
                echo 'Testing the Applications'
            }
        }

        stage('Build') {
            steps {
                echo 'Creating application Package'
            }
        }

        stage('Delivery') {
            steps {
                echo 'Uploading the artifact to a repository'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the Application'
            }
        }
    }
}
