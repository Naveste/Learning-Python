travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, visits, cities):
  new_country = {} #In order to add to the travel_log list we need to create a new empty dictionary that stores all the new data in it.
  new_country["country"] = country #add to the new_country dictionary, provide key and assign a value to it.
  new_country["visits"] = visits #add to the new_country dictionary, provide key and assign a value to it.
  new_country["cities"] = cities #add to the new_country dictionary, provide key and assign a value to it.
  travel_log.append(new_country) #add new item, new_country dictionary, to the list travel_log.

    
#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"]) #values provided according to the function's positional arguments.
print(travel_log)