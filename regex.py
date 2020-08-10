import re

txt = "The rain in Spain"
print(txt)

print("Find all lower case characters alphabetically between a and m")

#Find all lower case characters alphabetically between "a" and "m":

a = re.findall("[a-m]", txt)
print(a)

print("\n")
txt1 = "That will be 59 dollars"
print(txt1)
#Find all digit characters:
print("Find all digit characters")
b = re.findall("\d", txt1)
print(b)
print("\n")
txt3 = "hello world"
print(txt3)
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
print("Search for a sequence that starts with he , followed by two (any) characters, and an o")
c = re.findall("he..o", txt3)
print(c)
print("\n")
#Check if the string starts with 'hello':
print("Check if the string starts with hello")
d = re.findall("^hello", txt3)
if d:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
print("\n")
#Check if the string ends with 'world':
print("Check if the string ends with world")
e = re.findall("world$", txt3)
if e:
  print("Yes, the string ends with 'world'")
else:
  print("No match")

txt4 = "The rain in Spain falls mainly in the plain!"
print(txt4)
#Check if the string contains "ai" followed by 0 or more "x" characters:
print("Check if the string contains ai followed by 0 or more x characters")
f = re.findall("aix*", txt)
print(f)

if f:
  print("Yes, there is at least one match!")
else:
  print("No match")

print("\n")
#Check if the string contains "ai" followed by 1 or more "x" characters:
print("Check if the string contains ai followed by 1 or more x characters")
g = re.findall("aix+", txt4)

print(g)
print("\n")
if g:
  print("Yes, there is at least one match!")
else:
  print("No match")

print("\n")
#Check if the string contains "a" followed by exactly two "l" characters:
print("Check if the string contains a followed by exactly two l characters")
h = re.findall("aix+", txt4)
print(h)
if h:
  print("Yes, there is at least one match!")
else:
  print("No match")

print("\n")
#Check if the string contains "a" followed by exactly two "l" characters:
print("Check if the string contains a followed by exactly two l characters")
i = re.findall("al{2}", txt4)

print(i)
if i:
  print("Yes, there is at least one match!")
else:
  print("No match")
print("\n")

#Check if the string contains either "falls" or "stays":
print("Check if the string contains either falls or stays")
j= re.findall("falls|stays", txt4)

print(j)
if j:
  print("Yes, there is at least one match!")
else:
  print("No match")

