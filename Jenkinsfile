pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/pooja-dange1501/student-registration-flask.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run App') {
            steps {
                bat 'python app.py'
            }
        }
    }
}
