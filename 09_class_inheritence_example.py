class School:
    def __init__(self,name,strength,uniform):
        self.name = name
        self.strength = strength
        self.uniform = uniform
    
    def PrintDetails(self):
        print(self.name,self.strength,self.uniform)

class Institution(School):
    def __init__(self,name,strength,uniform,principal,teachers):
        School.__init__(self,name,strength,uniform)
        self.principal = principal
        self.teachers = teachers

    def institution_details(self):
        print(self.name,"  ",self.strength,"         ",self.uniform," ",self.principal,self.teachers)

x = Institution("Christ king",250,"White & Black","Michel",15)
y = Institution("Board",500,"White & Blue","Thimappa",25)
z = Institution("Bhuvanendra",1000,"White & Grey","Ravindra Bhat",40)
x.institution_details()
y.institution_details()
z.institution_details()
