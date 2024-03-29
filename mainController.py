import json
from bson import json_util
from bson.objectid import ObjectId
from fastapi import FastAPI,APIRouter
from pymongo import MongoClient
from typing import Optional, Dict, List
from queries import Query
from Models import Order, Product, User


app = FastAPI()

#client for database reads and writes
client = MongoClient("mongodb://127.0.0.1:27017/database_ecommerce")
db = client['database_ecommerce']

@app.get("/product_list")
def fetch_products(offset:int , limit:int , min_price: Optional[int] = None, max_price: Optional[int] =  None):

    #db_write
    with open('product_inventory.json') as file:
        file_data = json.load(file)
    keys = ["name","price","available_units"]
    old_data = file_data[0]
    file_data[0] = {key: old_data[key] for key in keys}
    
    if isinstance(file_data, list):
        db['product_container'].insert_many(file_data)  
    else:
        db['produc_container'].insert_one(file_data)
    
    query = []
    # subquery to apply price filters

    Query(query_type= "price_filter",superQuery= query, min_price= min_price, max_price= max_price)

    #subquery to enable pagination
    
    Query(query_type="pagination", superQuery= query,offset= offset, limit= limit)

    out = list(db['product_container'].aggregate(query))
    
    return json.loads(json_util.dumps(out))


# Post request for accomodating large order data
@app.post("/create_order")
def create_order(order_input: Order.RequestOrder):

    order_created = Order.Order(
        items=order_input.items,
        total_amount = order_input.total_amount,
        user_address=order_input.user_address
    )

    # DB write
    db['order_container'].insert_one(order_created.dict())

    return order_created
