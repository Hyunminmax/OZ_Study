from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self):
        pass
    
    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

    