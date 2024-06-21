from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ratings.models.rating_model import FoodRatingCreate, FoodRatingTable
import json

router = APIRouter()

@router.post("/api/v1/add-rating")
async def addRating(body: FoodRatingCreate):
    rating = FoodRatingTable(
        foodid = body.foodid,
        userid = body.userid,
        rating = body.rating
    )
    rating.save()
    tojson = rating.to_json()
    fromjson = json.loads(tojson)
    return {
        "message": "Thank your for rating",
        "data":fromjson,
        "status":True
    }