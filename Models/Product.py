from pydantic import BaseModel

class Product(BaseModel):
    id: str
    name: str
    price: int
    available: int


# creates bought item object for user
class BoughtItem(BaseModel):
    id: str
    count: int
