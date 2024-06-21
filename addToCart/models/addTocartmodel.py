from mongoengine import Document,StringField,IntField
from pydantic import BaseModel
class AddtocartTable (Document):
    userid = StringField(required =True)
    quantity = IntField(required =True)
    foodId = StringField(required =True)
    foodoptionId = StringField(required=True)
    
class Addtocartcreatemodel(BaseModel):
    userid: str
    quantity:int
    foodId:str
    foodoptionId:str
