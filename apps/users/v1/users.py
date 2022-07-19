from marshmallow import ValidationError as MarshmallowValidationError
from mongoengine import DoesNotExist
from flask_restful import Resource, request

from apps.users.schemas.users import UserSchema, CallingSchema
from apps.users import models


class CallSaving(Resource):
    
    def put(self, user_name):
        _data = request.get_json()
        call_duration = _data["call_duration"]

        try:
            UserSchema().load({"name":user_name})
            CallingSchema().load({"call_duration":call_duration})
        except MarshmallowValidationError as e:
            return {"message":str(e)}, 400

        try:
            user = models.User.objects.get(name=user_name)
        except DoesNotExist:
            user = models.User(name=user_name)
            user.save()
            user.reload()
        the_calling = models.Calling(user=user, call_duration=call_duration)
        the_calling.calculate_total_blocks()
        the_calling.save()
        the_calling.reload()
        return {
            "message": "save the call success",
            "calling": CallingSchema().dump(the_calling),
        }, 200


class BillCalculating(Resource):
    def get(self, user_name):
        try:
            user = models.User.objects.get(name=user_name)
        except DoesNotExist:
            return  {"message":"user not found"}, 404
        calls = models.Calling.objects(user=user)
        call_count = calls.count()
        block_count = calls.sum("blocks")
        return {"call_count": call_count, "block_count": block_count}, 200
