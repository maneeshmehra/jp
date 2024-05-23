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

    def maxRetries = 3
    def attempts = 1
    def retry = true

    while (retry && attempts <= maxRetries) {
        echo "Running Compliance Check (Attempt: ${attempts} of ${maxRetries})"
        def status = sh(returnStatus: true, script: """python check_container.py > output.txt 2>&1""")
        def output = readFile "output.txt"
        if (status == 0) {
            echo "The script executed successfully !"
            retry = false
        } else {
            echo "The script did not execute successfully !"
            attempts += 1
        }
		handleOutcome(output)
     }
}

def handleOutcome(output) {
	echo "Script Output: ${output}"
}
