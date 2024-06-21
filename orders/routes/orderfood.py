from fastapi import APIRouter
from fastapi.responses import JSONResponse
from orders.model.ordersmodel import OrdersAddModel, OrdersTable
from datetime import datetime
import json 
router = APIRouter()

@router.post("/api/v1/add-user-order")
async def createOrder(body: OrdersAddModel):
    foodid = []
    order = OrdersTable(
        foodid = body.foodid, 
        userid = body.userid, 
        totalamount = body.totalamount, 
        orderdate=f"{datetime.date}", 
        dropLat = body.dropLat,
        dropLong = body.dropLong,
        address = body.address,
        paidby = body.paidby,
        deliveryCharge = body.deliveryCharge
        )
    order.save()
    tojson = order.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"Order Created success",
        "data":fromjson,
        "status":True
    }


@router.get("/api/v1/get-user-orders/{userid}")
async def getUserOrders(userid: str):
    findorders = OrdersTable.objects(userid=userid).all()
    tojson = findorders.to_json()
    fromjson = json.loads(tojson)
    if(findorders):
        return {
            "message":"here is your orders",
            "data": fromjson,
            "status":True
        }
    else:
        return JSONResponse(
            status_code=302,
            content={
            "message":"orders not found",
            "data":fromjson,
            "status":False
        }
        )