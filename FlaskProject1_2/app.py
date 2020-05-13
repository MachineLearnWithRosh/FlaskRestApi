from flask import Flask
from flask_restful import Api
from security import authentication, identity

from flask_jwt import JWT
from user import UserRegister
from item import Item, ItemList

app = Flask(__name__)
app.secret_key = 'rose'
api = Api(app)

jwt = JWT(app, authentication, identity)

items = []


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == "__main__":
    app.run(port=5000, debug=True)
