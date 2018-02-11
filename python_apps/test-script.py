from flask import Flask
from pymongo import MongoClient
app = Flask(__name__)

@app.route('/')
def hello_world():
    
    client = MongoClient()
    if client:
         print 'Client connected'
    return 'Flask Dockerized'      

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
