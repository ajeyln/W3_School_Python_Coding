x = 5 # assigning variable
y = "Hello, World!"
name = "ajey"
print(x)
print(y)
print(name)

#if the variable assigned inside the function , then the variable is applicable only to that function

def myfunc():
  
  x = "fantastic"
  print ("Python is " +x) # where + sign indicate the value added to the statement 
  
  myfun ()

#If we create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x) # out put - Python is fantastic

myfunc()

print("Python is " + x) # out put - Python is awesome

# If we use the global keyword , the variable can use inside as well out side

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) # out put - Python is fantastic
