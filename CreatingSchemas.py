from marshmallow import Schema,fields

# Creating model
class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email

# creating schema for our model

# using class
class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()

# using dictionary
UserSchema_using_dict = Schema.from_dict(
    {
        "name":fields.Str(),
        "email":fields.Email()
    }
)

"""
## dump is for serialising 
## load is for deserialising
"""