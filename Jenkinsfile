node {
  try {
    stage('Clone') { git branch: 'main', url: 'https://github.com/Ishaan-007/test-app.git' }

    stage('Build') {
      sh '''
        python3 -m venv venv
        . venv/bin/activate
        pip install --upgrade pip
        pip install -r requirements.txt
      '''
    }

    stage('Test') {
      sh '''
        . venv/bin/activate
        pytest
      '''
    }
    echo "Scripted Pipeline succeeded"
  } catch (e) {
    echo "Scripted Pipeline failed"
    throw e
  }
}