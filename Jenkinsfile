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
             if [ "$(docker ps -q -f name=test_web_app)" ]; then
                docker rm $(docker stop $(docker ps -a -q --filter name=test_web_app --format="{{.ID}}"))
             fi
             docker run -d -p 7880:7880 -name test_web_app test_web_app
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
