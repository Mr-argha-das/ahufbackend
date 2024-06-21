from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ratings.models.rating_model import FoodRatingCreate, FoodRatingTable
from foods.models.foodmodel import FoodCreate, FoodTable, FoodOtherDeatailsCreate, FoodOtherDetailsTable
import json
from bson import ObjectId
router = APIRouter()

@router.post("/api/v1/food-create")
async def createFood(body: FoodCreate):
    food = FoodTable(
        title = body.title, 
        image = body.image, 
        foodtype = body.foodtype, 
        categoryid = body.categoryid,
        recomandate = body.recomandate
        )
    food.save()
    tojson = food.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"Food Created Succes", 
        "data":fromjson,
        "nextapi":"/api/v1/add-food-other-details",
        "status":True
    }

@router.post("/api/v1/add-food-other-details")
async def createFoodOtherDetails(body: FoodOtherDeatailsCreate):
    foodotherDetails =  FoodOtherDetailsTable(foodId = body.foodId, title=body.title, price=body.price)
    foodotherDetails.save()
    tojson = foodotherDetails.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"Food Details Added",
        "data":fromjson,
        "status":True
    }
    
@router.get("/api/v1/get-foods-options/{foodid}")
async def getFoodsOptions(foodid:str):
    data = FoodOtherDetailsTable.objects(foodId=foodid)
    tojson = data.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"Here Is food's Options",
        "data":fromjson,
        "status":True
    }
@router.get("/api/v1/all-foods")
async def allFoods():
    actuldata = []
    allfoods = FoodTable.objects.all()
    data_list = list(allfoods)
    for value in data_list:
        print(value.id)
        foodRating = FoodRatingTable.objects(foodid=str(value.id)).all()
        prices = FoodOtherDetailsTable.objects(foodId=str(value.id)).all()
        print(foodRating)
        priceTojson = prices.to_json()
        priceTofromJson = json.loads(priceTojson)
        tojsonR = foodRating.to_json()
        fromjosR = json.loads(tojsonR)
        tojson = value.to_json()
        fromjson = json.loads(tojson)
        
        actuldata.append({
            "food": fromjson,
            "rating":fromjosR,
            "prices":priceTofromJson
        })
        
    
    return {
        "message":"here is all food",
        "data":actuldata,
        "status":True
    }
    
@router.get("/api/v1/search/food/{text}")
async def searchFood(text: str):
    actuldata = []
    findFood = FoodTable.objects(title__icontains=text)
    data_list = list(findFood)
    for value in data_list:
        print(value.id)
        foodRating = FoodRatingTable.objects(foodid=str(value.id)).all()
        print(foodRating)
        tojsonR = foodRating.to_json()
        fromjosR = json.loads(tojsonR)
        tojson = value.to_json()
        fromjson = json.loads(tojson)
        
        actuldata.append({
            "food": fromjson,
            "rating":fromjosR
        })
    return {
        "message":"here is all food",
        "data":actuldata,
        "status":True
    }

    
    
@router.get("/api/v1/foodtype/food/{query}")
async def getFoodByType(query: str):
    actuldata = []
    allfoods = FoodTable.objects(foodtype=query)
    data_list = list(allfoods)
    for value in data_list:
        print(value.id)
        foodRating = FoodRatingTable.objects(foodid=str(value.id)).all()
        print(foodRating)
        tojsonR = foodRating.to_json()
        fromjosR = json.loads(tojsonR)
        tojson = value.to_json()
        fromjson = json.loads(tojson)
        
        actuldata.append({
            "food": fromjson,
            "rating":fromjosR
        })
        
    
    return {
        "message":"here is all food",
        "data":actuldata,
        "status":True
    }


@router.get("/api/v1/recomanded/food")
async def searchFood():
    findFood = FoodTable.objects(recomandate=True)
    tojson = findFood.to_json()
    fromjson = json.loads(tojson)
    return {
        "message" : "Here is food",
        "data" : fromjson,
        "status" : True
    }
    