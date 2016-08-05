# coding: utf-8

import gevent.monkey
gevent.monkey.patch_all()

import time

from flask import Flask
from gevent.wsgi import WSGIServer


app = Flask(__name__)


@app.route('/sleep', methods=['GET'])
def sleep():
    time.sleep(5)
    return 'sleep: 5s.'


@app.route('/do', methods=['GET'])
def do():
    return 'do when the other sleep'



if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000, debug=True)
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()
