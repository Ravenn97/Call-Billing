from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1, max=31))

class CallingSchema(Schema):
    call_duration = fields.Integer(required=True, validate=validate.Range(min=1))
    blocks = fields.Integer(required=False)
    user = fields.Nested(UserSchema, required=True)