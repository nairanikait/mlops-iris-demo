
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/nairanikait/mlops-iris-demo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Retrain Model') {
            steps {
                sh 'python3 retrain.py'
            }
        }

        stage('Deploy Model') {
            steps {
                sh 'cp iris_model.pkl /opt/mlops-model/iris_model.pkl'
                sh 'ls -lh /opt/mlops-model/iris_model.pkl'
            }
        }
    }
}
