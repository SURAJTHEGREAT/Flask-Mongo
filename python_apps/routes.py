from __future__ import absolute_import

from flask import Flask, json, request

from pymongo import MongoClient

from common.util.authenticate import login

from logger.log import getLogger

import os

app = Flask(__name__)

# GENERATE THE LOG PATH FROM CURRENT FILE NAME
logpath = os.path.splitext(os.path.basename(__file__))[0] + '.log'

LOG = getLogger(__name__,logpath)

@app.route('/login', methods = ['POST'])

def login_route():
    #http://blog.luisrei.com/articles/flaskrest.html
    # for basic auth : http://flask.pocoo.org/snippets/8/
    try:

        if request.headers['Content-Type'] == 'application/json':

            content = request.json


            result = login(content)

        

    except Exception as e:

        print "Error occured is :" ,e



    return 'Flask dockerized'     

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
