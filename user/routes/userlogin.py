from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from user.model.usermodel import OTPModel, OTPTable
from user.model.usermodel import LoginUserModel, UserTable

from fastapi import APIRouter
import pyrebase
import secrets
import string
import requests
router = APIRouter()
import random
import json
# Initialize Firebase Admin SDK


# Request body model for sending OTP
class SendOTPRequest(BaseModel):
    phone_number: str

class PhoneNumber(BaseModel):
    phone_number: str

class VerifyOTP(BaseModel):
    token: str
    mobileno:str
    otp: str

# Endpoint to send OTP
@router.post("/api/v1/send-otp")
async def sendOtp(body: SendOTPRequest):
    otp = random.randint(1000, 9999)
    charset = string.ascii_letters + string.digits

# Generate a 32-character long string
    random_string = ''.join(secrets.choice(charset) for _ in range(32))
    url = f"https://alerts.prioritysms.com/api/v4?api_key=Ac1a8513fcbb491547ce6d47163745134&method=sms&message=Hello Dear, your OTP {otp} for login at https://www.diwamjewels.com&to={body.phone_number}&sender=DIWAMJ"
    response = requests.get(url)
    if response.status_code == 200:
        data = OTPTable(token=random_string, otp=str(otp))
        data.save()
        print("Request successful")
        print(response.text)  # Print the response from the server
        return {
            "message":"OTP Sent",
            "token": random_string,
            "status":True
        }
    else:
        print(f"Request failed with status code {response.status_code}")
        return {
            "message":"OTP Sent faild",
            "token": None,
            "status":False
        }
        
@router.post("/api/v1/verify-otp")
async def verifyOTP(body: VerifyOTP):
    findOtp = OTPTable.objects(token = body.token).first()
    
    if findOtp:
        if findOtp.otp == body.otp:
            findOtp.delete()
            finduser = UserTable.objects(emailorphone=body.mobileno).first()
            if finduser:
                 tojson = finduser.to_json()
                 fromjson = json.loads(tojson)
                 return {
                     "message":"User login Success",
                     "data":fromjson,
                     "status":True
                 }
            else:
                saveUser = UserTable(emailorphone = body.mobileno)
                saveUser.save()
                tojson = saveUser.to_json()
                fromjson = json.loads(tojson)
                return {
                    "message": "User create Sucess",
                    "data":fromjson,
                    "status":True
                }
        else:
            
            return {
                "message":"Mobile no is not verifyed",
                "data": None,
                "status":False
            }
    else:
        return {
                "message":"some thing went wrong",
                "data": None,
                "status":False
            }
# @router.post("/api/v1/user-login-create/phone/")
# async def loginPhone(body: LoginUserModel):
#     finduser = UserTable.objects(emailorphone=body.emailorphone).first()
#     if finduser:
#         tojson = finduser.to_json()
#         fromjson = json.loads(tojson)
#         return {
#             "message":"User login Success",
#             "data":fromjson,
#             "status":True
#         }
#     else:
#         saveUser = UserTable(emailorphone = body.emailorphone)
#         saveUser.save()
#         tojson = saveUser.to_json()
#         fromjson = json.loads(tojson)
#         return {
#             "message": "User create Sucess",
#             "data":fromjson,
#             "status":True
#         }