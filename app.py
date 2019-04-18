# ./app.py

from flask import Flask, render_template, request, jsonify
import json
import time

# create flask app
app = Flask(__name__)

# index route, shows index.html view
@app.route('/')
def index():
    data = {"time": time.time()}
    return jsonify(data)

# endpoint for simple file IO
# return file handle to work with
@app.route('/createemptyfile', methods=['GET'])
def createEmptyFile():
    fpath = request.args.get('fpath')
    f = open(fpath, 'w+')
    data = {'id' : f}
    return jsonify(data)

# endpoint for writing to file
# takes in file handle
@app.route('/writetofile', methods=['GET'])
def writeToFile():
    f = request.args.get('fpath')
    info = request.args.get('info')
    f.write(info)
    data = {'id' : f}
    return jsonify(data)

# endpoint for creating to file, writing to it and returning information
# takes in file path
@app.route('/filework', methods=['GET'])
def fileWork():
    fpath = request.args.get('fpath')
    info = request.args.get('info')
    fp = open(fpath, 'w+')
    fp.write(info)
    fp.close()
    data = {'id' : True}
    return jsonify(data)

# run Flask app in debug mode
app.run(debug=True)