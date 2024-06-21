from mongoengine import Document, StringField
from pydantic import BaseModel

class FavTable(Document):
    userid = StringField(required=True)
    foodid = StringField(required=True)
    

class FavmodelCreate(BaseModel):
    userid : str
    foodid : str