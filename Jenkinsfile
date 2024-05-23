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
    def status = sh(returnStatus: true, script: """python check_container.py > output.txt 2>&1""")
    def output = readFile "output.txt"
    if (status == 0) {
        echo "The script executed successfully !"
    } else {
        echo "The script did not execute successfully !"
    }
    echo "Script Output: ${output}"
}
