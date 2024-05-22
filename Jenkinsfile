pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
    
        stage("Check source-container-compliance") {
            options {
                timeout(time: 30, unit: 'MINUTES')
            }
            steps {
                script {
                    stageStartTime = System.currentTimeMillis()
                    sourceContainerComplianceCheck()
                }
            }
            post {
                always {
                    script {
                        echo "stage complete"
                    }
                }
            }
        }
    }
}

def sourceContainerComplianceCheck() {
    echo "Running Compliance Check"
    stdout = sh(returnStdout: true, script: """python check_container.py 2>&1""").trim()
    echo "This is the output from the script: ${stdout}"
}
