
import mongoengine
from mongoengine import Document, CASCADE



class User(Document):
    name = mongoengine.StringField(max_length=31, required=True)

    meta = {
        "indexes": [
            {"fields": ["name"], "sparse": True},
        ]
    }


class Calling(Document):
    call_duration = mongoengine.IntField(min=1)
    blocks =  mongoengine.IntField(min=1)
    user = mongoengine.ReferenceField(User, reverse_delete_rule=CASCADE)

    def calculate_total_blocks(self):
        if self.call_duration % 30 == 0:
            self.blocks = self.call_duration // 30
        else:
            self.blocks = self.call_duration // 30 + 1
