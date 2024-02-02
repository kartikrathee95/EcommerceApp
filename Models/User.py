from pydantic import BaseModel

# User Address Information

class UserAddress(BaseModel):
    city: str
    country: str
    zip_code: str


class User(BaseModel):
    id: str
    address: UserAddress
    