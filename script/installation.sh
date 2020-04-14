#!/bin/bash
source /var/lib/jenkins/workspace/watercooler-pipeline/venv/bin/activate
pip3 install flask
pip3 install flask_mysqldb
pip3 install pytest
pip3 install pytest-base-url
pip3 install urllib3
pip3 install coverage
source /var/lib/jenkins/.bashrc
python3 /var/lib/jenkins/workspace/watercooler-pipeline/app.py





# Old Code
# source venv/bin/activate
# source ~/.bashrc
# python3 app.py