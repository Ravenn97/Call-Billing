from re import A, U
from tkinter import Y
import unittest
from apps.users import models
from apps.users.schemas.users import CallingSchema, UserSchema
from mongoengine import connect, disconnect, Document, StringField
from apps.users.models import User, Calling
from mongoengine.errors import ValidationError
from marshmallow.exceptions import ValidationError as MarshmallowValidationError
from mongoengine import DoesNotExist

class TestPerson(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connect('mongoenginetest', host='mongomock://localhost')

    @classmethod
    def tearDownClass(cls):
       disconnect()

    def test_valid_name(self):
        user = User(name='aaaaaaaa')
        user.save()
        user.reload()
        assert UserSchema().dump(user) ==  {'name': 'aaaaaaaa'}

    def test_invalid_name(self):
        user = User(name='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        with self.assertRaises(ValidationError):
            user.save()
        
    def test_invalid_name2(self):
        user = User(name='aaaaaaaaaaaaaaaaaaaaaa')
        user.save()
        user.reload()
        
        assert UserSchema().dump(user) !=  {'name': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'}
        
    def test_valid_call_duration1(self):
        user = User(name='aaaaaaaa')
        user.save()
        user.reload()
        call = Calling(user=user, call_duration=30)
        call.calculate_total_blocks()
        call.save()
        call.reload()
        assert CallingSchema().dump(call) ==  {'call_duration': 30, 'blocks': 1, 'user': {'name': 'aaaaaaaa'}}
    
    def test_valid_call_duration2(self):
        user = User(name='aaaaaaaa')
        user.save()
        user.reload()
        call = Calling(user=user, call_duration=100080)
        call.calculate_total_blocks()
        call.save()
        call.reload()
        assert CallingSchema().dump(call) ==  {'call_duration': 100080, 'blocks': 3336, 'user': {'name': 'aaaaaaaa'}}
    
    def test_valid_call_duration3(self):
        UserSchema().validate({"name":'aaaaaaaa'})
        CallingSchema().validate({"call_duration":1000001})
        user = User(name='aaaaaaaa')
        user.save()
        user.reload()
        call = Calling(user=user, call_duration=1000001)
        call.calculate_total_blocks()
        call.save()
        call.reload()
        # print(CallingSchema().dump(call))
        assert CallingSchema().dump(call) ==  {'call_duration': 1000001, 'blocks': 33334, 'user': {'name': 'aaaaaaaa'}}
    

    def test_invalid_call_duration(self):
        with self.assertRaises(MarshmallowValidationError):
            UserSchema().load({"name":'aaaaaaaa'})
            CallingSchema().load({"call_duration":0})    
            
    def test_invalid_call_duration2(self):
        with self.assertRaises(MarshmallowValidationError):
            UserSchema().load({"name":'aaaaaaaa'})
            CallingSchema().load({"call_duration":-111111})    

    def test_invalid_user(self):
        with self.assertRaises(DoesNotExist):
            models.User.objects.get(name="aaaaaaaa")

    def test_get_billing(self):
        try:
            user = models.User.objects.get(name="user1")
        except DoesNotExist:
            user = models.User(name="user1")
            user.save()
            user.reload()
        call1 = Calling(user=user, call_duration=1000001)
        call1.calculate_total_blocks()
        call1.save()
        call1.reload()
        
        
        call2 = Calling(user=user, call_duration=1234)
        call2.calculate_total_blocks()
        call2.save()
        call2.reload()

        calls = models.Calling.objects(user=user)
        call_count = calls.count()
        block_count = calls.sum("blocks")
        assert call_count == 2
        assert block_count == 33376   # 42 + 33334
if __name__ == '__main__':
    unittest.main()