import re

txt=input("Enter a word:" )
x=re.search("Pol*",txt)
if (x):
	print("The charecter is correct")
else:
	print("The charecter is not correct")
y=re.findall("kukkundoor$",txt)
print(y)
if (y):
    print("Match Found")
else:
    print("Match not found")

