from mongoengine import connect
from fastapi import FastAPI
from user.routes import userlogin 
from orders.routes import orderfood
from foods.routes import foodcreate
from favratie.routes import routes
from category.routes import categoryroutes
from adress.routes import addresrouter
from uploads import uploadroutes
from ratings.route import create_rating
from addToCart.routes import addtocartroute

app = FastAPI()




connect('AHUFBACKEND', host="mongodb+srv://avbigbuddy:nZ4ATPTwJjzYnm20@cluster0.wplpkxz.mongodb.net/AHUFBACKEND")



app.include_router(userlogin.router, tags=["User"])
app.include_router(foodcreate.router, tags=["Food / Product"])
app.include_router(orderfood.router, tags=["Orders"])
app.include_router(uploadroutes.router, tags=["Favrate"])
app.include_router(categoryroutes.router, tags = ["Category"])
app.include_router(addresrouter.router, tags=["User Address"])
app.include_router(uploadroutes.router, tags=["Upload Image"])
app.include_router(create_rating.router, tags=["Rating"])
app.include_router(addtocartroute.router, tags=["AddToCart"])

