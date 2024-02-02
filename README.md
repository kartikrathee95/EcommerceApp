# EcommerceApp
# Step1: Clone the project on your editor
# Step2: Activate virtualenv : virtualenv\Scripts\activate
# Step3: Navigate to main(parent) directory and run uvicorn mainController:app --reload
# Step4: Run apis:
Go to https://127.0.0.1:8000/docs:
2 APIS,
1. product_listing, args = [max_price, min_price, offset, limit]
2. order_creation, Enter in request Body, in exactly following format, you can replace the values:
3. {
  "items": [
    {
      "id": "strkdkn291ing",
      "count": 0
    }
  ],
  "user_address": {
    "city": "string",
    "country": "string",
    "zip_code": "string"
  },
  "total_amount": 1000
}
add more items, like
{
  "items": [
    {
      "id": "string",
      "count": 10
    },
   {
   "id":"123445566",
   "count":100
   }
  ],
  "user_address": {
    "city": "string",
    "country": "string",
    "zip_code": "string"
  },
  "total_amount": 1000
}
