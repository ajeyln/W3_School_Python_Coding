print("Simple string Format Method")
#Simple string Format Method
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
print("\n")
#String format using indexing method
print("String format using indexing method")
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
print("\n")
#String format using Named indexing method
print("String format using Named indexing method")
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

