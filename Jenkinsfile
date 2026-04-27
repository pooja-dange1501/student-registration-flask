pipeline {
    agent any

    environment {
        PYTHON = "C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Upgrade Pip') {
            steps {
                bat "\"${PYTHON}\" -m pip install --upgrade pip"
            }
        }

        stage('Install Dependencies') {
            steps {
                bat "\"${PYTHON}\" -m pip install -r requirements.txt"
            }
        }

        stage('Run Flask App (Background)') {
            steps {
                bat 'start "" /B "' + env.PYTHON + '" app.py'
            }
        }
    }

    post {
        success {
            echo '✅ Build Successful - Flask App Started'
        }
        failure {
            echo '❌ Build Failed - Check logs'
        }
    }
}