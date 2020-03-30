#!/bin/bash

source /var/lib/jenkins/workspace/bookclub/venv/bin/activate

source /var/lib/jenkins/.bashrc

coverage run -m pytest ./test/db_testing.py

coverage report