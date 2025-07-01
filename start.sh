#!/bin/bash
cd ~/flaskapptest
source venv/bin/activate
export FLASK_APP=app.py
export FLASK_ENV=production
nohup flask run --host=0.0.0.0 --port=8000 > flask.log 2>&1 &

