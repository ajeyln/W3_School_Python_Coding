# to convert list to dictionary
x="SecondName FirstName Intials "
y= x.split(" ") #this will create list "y"
print("Type yourname with Firstname Secondname Intials")
a=input()
b = a.split(" ") #this will create input to list
resultdict = {}
for index in y:
    for value in b:
        resultdict[index] = value
        break
print(resultdict)
