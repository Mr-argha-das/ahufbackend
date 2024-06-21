from mongoengine import Document, StringField, FloatField, IntField, BooleanField, ListField
from pydantic import BaseModel

class FoodTable(Document):
    title = StringField(required=True)
    image = StringField(required = True)
    categoryid = StringField(required=True)
    foodtype = StringField(required=True)
    recomandate = BooleanField(required=True)

class FoodOtherDetailsTable(Document):
    foodId = StringField(required=True)
    title = StringField(required=True)
    price = IntField(required=True)

class FoodOtherDeatailsCreate(BaseModel):
    foodId : str
    title : str
    price : int

class FoodCreate(BaseModel):
    title: str
    categoryid: str
    image: str
    foodtype: str
    recomandate: bool