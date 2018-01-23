#!/usr/bin/env bash
cd /var/www
export LC_ALL=C.UTF-8
export FLASK_APP=/var/www/main.py
export SERVER_NAME=192.168.0.119:5001
export DEBUG=1
apt-get -y install python3 sudo
apt-get -y install python3-virtualenv
apt-get install -y python3-pip
python3 -m virtualenv --python=python3.5 virtualenv
source virtualenv/bin/activate
pip3 install -r requirements.txt
./virtualenv/bin/flask run --host=0.0.0.0 --port=5000