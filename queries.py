from abc import ABC, abstractclassmethod

class Query:
    
    def __init__(self, query_type, superQuery,min_price = None, max_price = None, offset = None,limit = None):

        if query_type == "pagination":
            PaginationQuery().createQuery(superQuery,offset,limit)
        elif query_type == "price_filter":
            PriceFilter().createQuery(superQuery = superQuery, min_price=min_price, max_price=max_price)
    
    def createQuery():
        pass

class PriceFilter(Query):
     def __init__(self):
         pass
     def createQuery(self,superQuery, min_price, max_price):
    
        if min_price:
            superQuery.append({"$match": {"price": {"$gte": min_price}} })
        if  max_price:
            superQuery.append({ "$match": {"price": {"$lte": max_price}}})
         

class PaginationQuery(Query):
    def __init__(self):
        pass

    def createQuery(self,superQuery, offset, limit):

        superQuery.append({ 
        "$facet": {
        "data": [{"$skip": offset},{"$limit": limit},{"$project": {"id": "$_id","_id": 0,"name": "$name","price": "$price","quantity": "$available_qty"}}],
        "page": [{"$skip": offset},{"$limit": limit},{"$count": "count" },{"$project": {"limit":"$count","total": "$count","nextOffset": {"$cond": [{"$lt": ["$count", limit]}, None, {"$add": [offset, limit]}]}}}]}})
        
