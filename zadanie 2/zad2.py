
import datetime as dt
from marshmallow import Schema, fields


class StudentSchema(Schema):
    id = fields.UUID(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Str(required=True)
    birth_day = fields.Date(required=True)


def serialize(id, first_name, last_name, mail, birth_day):
    student = {"id": id, "first_name" : first_name, "last_name": last_name, "email": mail, "birth_day":birth_day}
    schema = StudentSchema()
    result = schema.dumps(student)
    return result
