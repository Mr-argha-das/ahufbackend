from mongoengine import Document, StringField, FloatField, IntField, ListField
from pydantic import BaseModel


class OrdersTable(Document):
    userid = StringField(required=True)
    totalamount = StringField(required=True)
    orderdate = StringField(required=True)
    foodid = ListField(required= True)
    dropLat = StringField(required=True)
    dropLong = StringField(required=True)
    address = StringField(required=True)
    paidby = StringField(required=True)
    deliveryCharge = StringField(required=True)

class OrdersAddModel(BaseModel):
    userid:str
    totalamount:str
    foodid:list[str]  
    dropLat:str
    dropLong:str
    address:str
    paidby:str
    deliveryCharge:str
    