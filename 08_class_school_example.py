print("Inst. Name","  ","Strength")
class School:
    def __init__(self, name, size,):
        self.name = name
        self.size = size

    def printinformation(self):
        print(self.name, "  ",self.size)

s = School("Bhuvanendra",50)
c = School("Christking ",25)
s.printinformation()
c.printinformation()