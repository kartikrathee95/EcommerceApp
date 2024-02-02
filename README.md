# EcommerceApp
# Step1: Clone the project on your editor
# Step2: Activate virtualenv : virtualenv\Scripts\activate
# Step3: Run: pip install -r requirements.txt
# Step4: Navigate to main(parent) directory and run uvicorn mainController:app --reload
# Step5: Run apis:
# Go to https://127.0.0.1:8000/docs:
# 2 APIS,
# 1. http://127.0.0.1:8000/list_products, args = [max_price, min_price, offset, limit], or pass in url like http://127.0.0.1:8000/list_products?offset=0&limit=1&min_price=0&max_price=100000
# 2. http://127.0.0.1:8000/create_order, Enter in request Body, in following format:
# POST REQUEST FORMAT 
{
  "items": [
    {
      "id": "string",
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
