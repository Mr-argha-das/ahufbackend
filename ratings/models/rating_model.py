from mongoengine import Document, StringField, FloatField
from pydantic import BaseModel

class FoodRatingTable(Document):
    foodid = StringField(required=True)
    userid = StringField(required=True)
    rating = FloatField(required=True)


class FoodRatingCreate(BaseModel):
    foodid : str
    userid : str
    rating : float
    
    
    