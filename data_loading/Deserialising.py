"""
    For validation of any dictionary load 
    and for json use loads
"""
from pprint import pprint
from marshmallow import Schema,fields , post_load


"""
    Naive approch
"""
class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()

user_data_1 = {
    "name":"arnab",
    "email":"arnab"
}

schema = UserSchema()
result = schema.load(user_data_1)
# if not matching schema results validation error
pprint(result)

"""
    Better Approach 
"""
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

better_schema = BetterUserSchema()
result = better_schema.load(user_data_1)
print(result)