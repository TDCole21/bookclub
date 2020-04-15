pipeline{
    agent any
    stages{
        stage('Development Environment'){
            steps{
                sh 'echo "pre-install and install"'
                sh 'chmod 775 ./script/*'
                sh './script/before_installation.sh'
                sh './script/installation.sh'
            }
        }
        stage('Wait for installation'){
            steps{
                
                sh 'sleep 20'
               
            }
        }
    }
}