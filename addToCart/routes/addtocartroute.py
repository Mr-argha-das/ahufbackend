from fastapi import APIRouter
from fastapi.responses import JSONResponse
from addToCart.models.addTocartmodel import Addtocartcreatemodel,AddtocartTable
from foods.models.foodmodel import FoodTable, FoodOtherDetailsTable

import json
from bson import ObjectId
router = APIRouter()

@router.post("/api/v1/addtocart")
async def addtocart (body: Addtocartcreatemodel):
    addtocartdata = AddtocartTable(
        quantity = body.quantity,
        foodId = body.foodId,
        userid = body.userid,
        foodoptionId = body.foodoptionId
    )
    addtocartdata.save()
    tojson = addtocartdata.to_json()
    fromjson = json.loads(tojson)
    return {
        "message": "Your Product Added To Cart",
        "data":fromjson,
        "status":True
    }



@router.get("/api/v1/addtocart-data/{userid}")
async def cartdata(userid:str):
    actualdata = []
    discoutnprice = 0
    acuttalprice = 0
    usercarts = AddtocartTable.objects(userid = userid)
    v = list(usercarts)
    print(v)
    for value in v:
        print(value.id)
        
        food = FoodTable.objects.get(id=ObjectId(f'{value.foodId}'))
        foodoptions = FoodOtherDetailsTable.objects.get(id=ObjectId(value.foodoptionId))
        fooddata = food.to_json()
        foodjson = json.loads(fooddata)
        cart = value.to_json()
        cartjson = json.loads(cart)
        foodoptionsTojson = foodoptions.to_json()
        foodoptionsFromjson = json.loads(foodoptionsTojson)
        actualdata.append({
            "food": foodjson,
            "cart": cartjson,
            "price": foodoptionsFromjson
        })
        discoutnprice = discoutnprice  + foodoptions.price * value.quantity
        acuttalprice = acuttalprice  + foodoptions.price * value.quantity
          
        
    return {"message":"Cart Data Found",
    "data": {
        "food": actualdata,
        "totalprice": discoutnprice,
        "acuttalprice":acuttalprice
    },
    "status": True
    }

@router.delete("/api/v1/cart-delete/{id}")
async def deletecart(id:str):
    findData = AddtocartTable.objects.get(id=ObjectId(id))
    findData.delete()
    return {"status": "success",}    

@router.delete("/api/v1/cart-delete-all/{userid}")
async def deletecartall(userid:str):
    findData = AddtocartTable.objects(userid = userid)
    findData.delete()
    return {"status": "success",}    



    
