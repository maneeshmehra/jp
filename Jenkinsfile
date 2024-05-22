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
    def sout = new StringBuilder(), serr = new StringBuilder()
    def proc = 'ls /badDir'.execute()
    proc.consumeProcessOutput(sout, serr)
    proc.waitForOrKill(1000)
    println "out> $sout\nerr> $serr"
}
