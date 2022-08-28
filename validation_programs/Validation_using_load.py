from pprint import pprint
from marshmallow import Schema,fields , post_load , ValidationError

class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email

class BetterUserSchema(Schema):
    name = fields.Str()
    email = fields.Email()

    @post_load
    def make_user(self,data,**kwargs):
        return User(**data)

user_data_1 = {
    "name":"arnab",
    "email":"arnab"
}

better_schema = BetterUserSchema()
try:
    result = better_schema.load(user_data_1)
    pprint(result)
except ValidationError as err:
    print(err.messages) ## getting which data was invalid
    print(err.valid_data) ## getting which data was valid
