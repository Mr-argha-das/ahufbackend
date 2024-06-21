from mongoengine import Document, StringField
from pydantic import BaseModel
class UserTable(Document):
    emailorphone = StringField(required=True)
    name = StringField(required=False)
    email = StringField(required = False)
    phone = StringField(required = False)
    countrycode = StringField(required = False)
    gender = StringField(required=False)

class OTPTable(Document):
    token = StringField(required=True)
    otp = StringField(required=True)

class OTPModel(BaseModel):
    token : str
    otp : str
    

class CreateUserModel(BaseModel):
    emailorphone: str
    name : str
    email : str
    phone : str
    countrycode : str
    gender : str
    

class LoginUserModel(BaseModel):
    emailorphone: str
    
