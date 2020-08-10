import os
# creating a file
print("Creating new file")
f = open("samplefile.txt", "x")

#Deleting file
print("Deleting file")
os.remove("sample.txt")