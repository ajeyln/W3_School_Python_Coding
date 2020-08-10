import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
print("The base json file is:")
print(x)
print("\n")

print("Conversion from json to dictionary")
# parse x:
y = json.loads(x)
print("The converted dictionary is")
print(y)
# the result is a Python dictionary:
print("The value of age in this dictionary is :", +y["age"])


print("\n")
print("*****************************************************")
print("Conversion from Dictionary to jason")

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
