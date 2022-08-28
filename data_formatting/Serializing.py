from pprint import pprint
from marshmallow import Schema,fields

# Creating model
class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email

class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()

user = User(name="arnab",email="email")
schema = UserSchema()

# python dictionary
dict_result = schema.dump(user)
pprint(dict_result)

# json
json_result = schema.dumps(user)
pprint(json_result)

# handling collection of objects together
user1 = User(name="arnab",email="email")
user2 = User(name="arnab1",email="email1")
users = [user1,user2]
# collection_schema = UserSchema(many=True)
# collection_result = schema.dump(users)
# or
collection_schema = UserSchema()
collection_result = schema.dump(users,many=True)
pprint(collection_result)