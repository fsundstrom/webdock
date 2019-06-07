throttle(['throttleDocker']) {
  node('docker') {
    wrap([$class: 'AnsiColorBuildWrapper']) {
      try{
        stage('Setup') {
          checkout scm
          sh '''
            cd ./docker
            ./build.sh
          '''
        }
        stage('Test'){
          parallel (
            "unit": {
              sh '''
                ./ci/test/unit.sh
              '''
            },
            "functional": {
              sh '''
                ./ci/test/functional.sh
              '''
            }
          )
        }
        stage('Deploy ') {
          sh '''
             docker run -d -p 7880:7880 test_web_app
          '''
        }
      }
      finally {
        stage('Cleanup') {
          sh '''
            echo "this would be docker cleanup"
          '''
        }
      }
    }
  }
}
