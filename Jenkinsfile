pipeline{
    agent any
    stages{
        stage('Development Environment'){
            steps{
                sh 'echo "pre-install and install"'
                sh 'chmod 775 ./script/*'
                sh './script/before_installation.sh'
                // sh './script/installation.sh'
                sh './script/make_service.sh'
            }
        }
        stage('Wait for installation'){
            steps{
                
                sh 'sleep 20'
               
            }
        }
        // stage('URL Testing') {
        //     steps {
        //         sh 'echo "test page availability and status"'
        //         sh './script/url_testing.sh'

        //     }
        // }

        // stage('DB Testing') {
        //     steps {
        //         sh 'echo "test database structure and connection"'
        //         sh './script/db_testing.sh'

        //     }
        // }
    }
}