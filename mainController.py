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

@app.get("/products")
def fetch_products(offset:int , limit:int , min_price: Optional[int] = None, max_price: Optional[int] =  None):

    #db_write
    with open('product_inventory.json') as file:
        file_data = json.load(file)
    keys = ["name","price","available_units"]
    old_data = file_data[0]
    file_data[0] = {key: old_data[key] for key in keys}
    
    if isinstance(file_data, list):
        db['products'].insert_many(file_data)  
    else:
        db['products'].insert_one(file_data)
    
    query = []
    # subquery to apply price filters

    Query(query_type= "price_filter",superQuery= query, min_price= min_price, max_price= max_price)

    #subquery to enable pagination
    
    Query(query_type="pagination", superQuery= query,offset= offset, limit= limit)

    out = list(db['products'].aggregate(query))

    if len(out)>0 and len(out[0]['page'])>0:
        out[0]['page'][0]['limit'] = limit
        
    return json.loads(json_util.dumps(out))


# API to create an order
@app.post("/orders")
def create_order(order_input: Order.RequestOrder):

    order_created = Order.Order(
        items=order_input.items,
        total_amount = order_input.total_amount,
        user_address=order_input.user_address
    )

    # DB write
    db['order'].insert_one(order_created.dict())

    return order_created
