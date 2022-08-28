from marshmallow import Schema , fields , validate , ValidationError
from pprint import pprint

class UserSchema(Schema):
    name = fields.Str(validate=validate.Length(min=1))
    permission = fields.Str(validate=validate.OneOf(["read", "write", "admin"]))
    age = fields.Int(validate=validate.Range(min=18, max=40))
    surname = fields.Str(default="arnab")
    r_date = fields.Date(required=True)

in_data = {"name": "", "permission": "invalid", "age": 71}

"""
    partial is use to skip required validation
    partial = True for skipping all fields required
    partial=(field_name,) for skipping skipping required specific fields
"""
try:
    UserSchema().load(in_data,partial=True)
except ValidationError as err:
    pprint(err.messages)

