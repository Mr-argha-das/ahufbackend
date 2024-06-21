from fastapi import APIRouter, HTTPException
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
from pydantic import BaseModel
from adress.models.models import AddressTable, AddressCreate
from bson import ObjectId
import json
import requests
router = APIRouter()
def get_address_from_lat_lon(latitude, longitude, api_key):
    url = 'https://api.opencagedata.com/geocode/v1/json'
    params = {
        'q': f'{latitude},{longitude}',
        'key': api_key,
        'language': 'en',
        'pretty': 1
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if data and 'results' in data and len(data['results']) > 0:
            return data['results'][0]['formatted']
        else:
            return "No address found"
    except requests.RequestException as e:
        return f"Request error: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

@router.post("/api/v1/address-add")
async def addressAdd(body: AddressCreate):
    saveData = AddressTable(
        userId = body.userId,
        address1 = body.address1,
        address2 = body.address2,
        landmark = body.landmark,
        city = body.city,
        state=body.state,
        pincode = body.pincode
    )
    saveData.save()
    tojson = saveData.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"Address added",
        "data": fromjson,
        "status":True
    }
    
    
    
@router.get("/api/v1/address-get/{userid}")
async def addressAdd(userid: str):
    saveData = AddressTable.objects(userId = userid)
   
    tojson = saveData.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"Address gets",
        "data": fromjson,
        "status":True
    } 

@router.put("/api/v1/address-update/{addressid}")
async def addressAdd(addressid: str, body: AddressCreate):
    saveData = AddressTable.objects.get(id = ObjectId(addressid))
    saveData.address1 = body.address1
    saveData.address2 = body.address2
    saveData.landmark = body.landmark
    saveData.city = body.city
    saveData.state = body.state
    saveData.pincode = body.pincode
    saveData.save()
    tojson = saveData.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"Address update scusses",
        "data": fromjson,
        "status":True
    } 

@router.get("/api/v1/get-address-geo/{lat}/{long}")
async def getAddressGeo(lat: float, long: float):
    api_key = '4a6c6e5af4d94090bd1f1f05a1bdd00b'
    address = get_address_from_lat_lon(lat, long, api_key)
    return {
        "messager":"Here is location",
        "data": address,
        "status":True
    }
    
    
    




class Location(BaseModel):
    ip: str
    latitude: float
    longitude: float

@router.get("/get_location", response_model=Location)
def get_location():
    try:
        # Get the public IP address of the server
        ip_response = requests.get('https://api.ipify.org?format=json')
        ip_response.raise_for_status()
        ip_address = ip_response.json()['ip']

        # Get the location information based on the IP address
        location_response = requests.get(f'https://ipinfo.io/{ip_address}/geo')
        location_response.raise_for_status()
        location_data = location_response.json()

        # Extract latitude and longitude
        loc = location_data['loc'].split(',')
        latitude = float(loc[0])
        longitude = float(loc[1])

        return Location(ip=ip_address, latitude=latitude, longitude=longitude)
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    