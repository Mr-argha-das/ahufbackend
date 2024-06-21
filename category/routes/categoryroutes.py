from category.models.models import CateGoryCreate, CategoryTable
from datetime import datetime
from fastapi import APIRouter
import json
router = APIRouter()
@router.post("/api/v1/add/category")
async def categoryAdd(body: CateGoryCreate):
    categoryAdd = CategoryTable(
      title=body.title,
      categoryType=body.categoryType,
      status=body.status,
      images=body.images
    )
    categoryAdd.save()
    tojson = categoryAdd.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"Category added",
        "data": fromjson,
        "status":True
    }

@router.get("/api/v1/get/all-category")
async def getCategory():
    data = CategoryTable.objects.all()
    tojson = data.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"Here is Category",
        "data":fromjson,
        "status":True
    }