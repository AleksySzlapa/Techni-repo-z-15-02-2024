
from marshmallow import Schema, fields, ValidationError

class StudentSchema(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Email(required=True)
    birth_date = fields.Date(format='%Y-%m-%d', required=True)

def serialize_student_data(student_data):
    schema = StudentSchema()
    try:
        serialized_data = schema.dump(student_data)
        return serialized_data
    except ValidationError as e:
        return str(e)