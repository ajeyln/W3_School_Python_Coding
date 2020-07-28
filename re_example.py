import re

txt=input("Enter a word:" )
x=re.search("Pol*",txt)
if x:
	print("The charecter is correct")
else:
	print("The charecter is not correct")