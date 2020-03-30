#!/bin/bash

source /var/lib/jenkins/workspace/SFIA1-pipeline/venv/bin/activate

source /var/lib/jenkins/.bashrc

coverage run -m pytest ./test/db_testing.py

coverage report