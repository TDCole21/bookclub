pipeline{
    agent any
    stages{
        stage('Development Environment'){
            steps{
                sh 'echo "pre-install and install"'
                sh 'chmod 775 ./script/*'
                sh './script/before_installation.sh'

                sh 'MYSQL_HOST=\'34.89.55.248\''
                sh 'MYSQL_USER=\'root\''
                sh 'MYSQL_PASSWORD=\'\''
                sh 'MYSQL_DB=\'BOOKCLUB\''
                sh 'export MYSQL_HOST'
                sh 'export MYSQL_USER'
                sh 'export MYSQL_PASSWORD'
                sh 'export MYSQL_DB'

                sh 'source /home/Admin/watercooler/venv/bin/activate'
                sh './script/installation.sh'
                // sh './script/make_service.sh'
            }
        }
        stage('Wait for installation'){
            steps{
                
                sh 'sleep 20'
               
            }
        }
    }
}