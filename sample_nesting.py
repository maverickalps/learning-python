capitals = { 
    "France": "Paris",
    "Germany": "Berlin",
}

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Stuttgart"]
# }

# # print lille
# print(travel_log["France"][1])
# nested_list = ["a", "b", ["c", "d"], "e"]
# print(nested_list[2][0])



travel_log = {
    "France": {
        "cities_visited":["Paris", "Lille", "Dijon"],
        "total_visits": 8},
    "Germany": {"cities_visited" : ["Berlin", "Stuttgart"]
                , "total_visits": 5}
 }   
# print stuttgart
print(travel_log["Germany"]["cities_visited"][1])