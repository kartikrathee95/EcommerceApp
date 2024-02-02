# Order Base Model (Structure in which order will be saved in the DB)
from datetime import datetime
from pydantic import BaseModel, Field
from typing import List
from Models.Product import Product, BoughtItem
from Models.User import UserAddress

# Request Model for Order API
class RequestOrder(BaseModel):
    items: List[BoughtItem]
    user_address: UserAddress
    total_amount: int

class Order(BaseModel):
    createdOn: datetime = Field(default_factory=datetime.now)
    total_amount: int
    user_address: UserAddress
    items: List[BoughtItem]

    def __init__(self,items, total_amount, user_address):
        super().__init__(items = items, total_amount = total_amount, user_address = user_address)
   

