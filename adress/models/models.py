from mongoengine import Document, StringField, FloatField
from pydantic import BaseModel

class AddressTable(Document):
    userId = StringField(required=True)
    address1 = StringField(required=True)
    address2 = StringField(required=True)
    landmark = StringField(required=True)
    city = StringField(required= True)
    state=StringField(required=True)
    pincode = StringField(required=True)
    
    
class AddressCreate(BaseModel):
    userId: str
    address1: str
    address2: str
    landmark: str
    city: str 
    state: str
    pincode: str