import re

#Return a list containing every occurrence of "ai":

txt = "The rain in Spain"
a = re.findall("ai", txt)
print(a)
print("\n")

b = re.search("\s", txt)
print("The first white-space character is located in position:", b.start()) 
print("\n")

#Split the string at every white-space character:
print("Split the string at every white-space character")
c = re.split("\s", txt)
print(c)
print("\n")

#Split the string at the first white-space character:
print("Split the string at the first white-space character")
d = re.split("\s", txt, 1)
print(d)


#Replace the first two occurrences of a white-space character with the digit 9:
print("Replace the first two occurrences of a white-space character with the digit 9")
e = re.sub("\s", "9", txt, 2)
print(e)
print("\n")

#Replace the first two occurrences of a white-space character with the digit 9:
print("Replace the first two occurrences of a white-space character with the digit 9")
f = re.sub("\s", "9", txt, 2)
print(f)
print("\n")

#The search() function returns a Match object:
print("#The search() function returns a Match object")
g = re.search("ai", txt)
print(g)
print("\n")

#Search for an upper case "S" character in the beginning of a word, and print its position:
print("Search for an upper case S character in the beginning of a word, and print its position")
h = re.search(r"\bS\w+", txt)
print(h.span())
print("\n")

#The string property returns the search string:
print("The string property returns the search string")
i = re.search(r"\bS\w+", txt)
print(i.string)

#Search for an upper case "S" character in the beginning of a word, and print the word:
print("Search for an upper case S character in the beginning of a word, and print the word")
j = re.search(r"\bS\w+", txt)
print(j.group())







