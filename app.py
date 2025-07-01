from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Automatically updated from ci/cd"})

 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
