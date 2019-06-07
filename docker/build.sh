#!/usr/bin/env bash

# auto docker build
# By Frank Sundstrom
# and now Joe Garcia

TAG="Test_web_app"

cp -rf ../app .
cp -f ../run.py .
# cat << EOF > run.py
# #!/usr/bin/env python
# from app import app
# app.run (host='0.0.0.0', port=8008, debug=False)
# EOF

chmod 755 run.py

if [ -e .proxy ]; then
  # the .proxy file should contain the following if needed:
  # proxy_https='https://<user>:<password>@<proxy>:<port>'
  # proxy_http='http://<user>:<password>@<proxy>:<port>'
  . .proxy
  docker build \
  --build-arg https_proxy=${proxy_https} \
  --build-arg http_proxy=${proxy_http} \
  -t ${TAG} .
else
  docker build -t ${TAG} .
fi

rm -rf app
rm -f run.py
