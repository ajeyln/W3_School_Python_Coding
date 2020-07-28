import datetime
x=datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))
y=datetime.datetime(x.year, 1, 25)
print(y)