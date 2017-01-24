from flask_restful import fields

bucket_item_inputs = {
    "id": fields.String,
    "title": fields.String,
    "description": fields.String,
    "done": fields.Boolean,
    "date_created": fields.DateTime(dt_format='rfc822'),
    "date_modified": fields.DateTime(dt_format='rfc822')
}

bucket_inputs = {
    "id": fields.String,
    "title": fields.String,
    "description": fields.String,
    "items": fields.Nested(bucket_item_inputs),
    "created_by": fields.String,
    "date_created": fields.DateTime(dt_format='rfc822'),
    "date_modified": fields.DateTime(dt_format='rfc822')
}

user_inputs = {
    "id": fields.Integer,
    "username": fields.String,
    "email": fields.String
}
