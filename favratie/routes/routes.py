from fastapi import APIRouter
from fastapi.responses import JSONResponse
from favratie.model.favmodel import FavmodelCreate, FavTable
import json
router = APIRouter()

@router.post("/api/v1/create-fav-food")
async def createFoodFav(body: FavmodelCreate):
    savedata = FavTable(userid = body.userid, foodid = body.foodid)
    savedata.save()
    return {
        "message":"Favrate added",
        "status":True
    }

@router.get("/api/v1/get-fav/{userid}")
async def getFavData(userid: str):
    findata = FavTable.objects(userid=userid)
    tojson = findata.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"Here is fav food",
        "data":fromjson,
        "status":True
    }