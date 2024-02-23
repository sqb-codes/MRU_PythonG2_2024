data = [
    {"id":101, "name":"Apple Iphone 14", "price":80000, "brand":"Apple"},
    {"id":102, "name":"Samsung Galaxy", "price":80000, "brand":"Samsung"},
    {"id":103, "name":"Puma Shoes", "price":5000, "brand":"Puma"},
    {"id":104, "name":"Adidas Shoes", "price":4000, "brand":"Adidas"}
    ]

'''
1. User wants to search a product.
    user can input product name or brand
2. Store search results in a new list
'''

user_search = input("Search product : ")
search_result = []
for i in range(len(data)):
    if data[i]["name"] == user_search or data[i]["brand"] == user_search:
        print(data[i])
        search_result.append(data[i])






