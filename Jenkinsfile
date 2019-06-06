throttle(['throttleDocker']) {
  node('docker') {
    wrap([$class: 'AnsiColorBuildWrapper']) {
      try{
        stage('Setup') {
          checkout scm
          sh '''
            ./docker/build.sh
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
             docker run test_web_app -p 7880:7880 -d
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
