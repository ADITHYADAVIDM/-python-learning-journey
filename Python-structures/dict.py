# customer = {} - empty dictonary
# dictinary = {key : value} - no duplicate keys are allowed
customer = {
    "name" : "david",
    "age" : "21",
    "is_verified" : True
}
print(customer["name"])# specifying exact key name is mandatory, otherwise error
print(customer.get("Name"))# specifying exact key name is !mandatory, results in "none"
print(customer.get("name"))
print(customer.get("Name", "Default value"))# has option for default value instead of none
customer["name"] = "john"# updating value
customer.update({"name" : "david"})# updating existing key-value pair using update method
customer.update({"email" : "david@gmail.com"})# add a new key-value pair
customer.pop("age")# removes the specified key-value pair
customer.popitem()# removes the latest key-value pair
customer.clear()# truncate the dictonary
keys = customer.keys() # returns all the keys as a list
values = customer.values() # returns all the values as a list
customer.items()# returnes a 2D list of each key value pair
for key, value in customer.items():
    print(f"{key} : {value}")