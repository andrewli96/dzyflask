#!/usr/bin/python
# coding=utf-8
import sys
import os

import flask
from flask import Flask, request, g
from flask_cors import CORS
from auth import *
from datetime import timedelta


from flask_jwt import JWT, jwt_required, current_identity


from uncompress import uncompress_task_manager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'
app.config['JWT_AUTH_HEADER_PREFIX'] = 'Bearer'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=3600)


jwt = JWT(app, authenticate, identity)

@app.route('/')
def home():
    return 'Welcome to flask-unrar-json!'

@app.route('/api/v1/unrar', methods=['POST'])
@jwt_required()
def query_med_rec():

    req = request.get_json()
    #print(req['path'])
    name, path = uncompress_task_manager(req['path'], req['name'])
    #print('uncompress finished')
    return flask.jsonify({"file_name":name, "file_path":path})

app.run(port='3001')
