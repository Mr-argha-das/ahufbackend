from mongoengine import Document, StringField, FloatField, IntField, BooleanField
from pydantic import BaseModel

class CategoryTable(Document):
    title = StringField(required=True)
    categoryType = StringField(required=True)
    status = BooleanField(requirted=True)
    images = StringField(required=True)
    
class CateGoryCreate(BaseModel):
    title:str
    categoryType:str
    status: bool
    images:str