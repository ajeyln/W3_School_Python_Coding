class Name:
    def __init__(self,fname):
        self.fname=fname
    
    def PrintName(self):
       print(self.fname)

class Display(Name):
    def __init__(self,fname,lname):
        Name.__init__(self,fname)
        self.lname = lname

    def DisplayName(self):
        firstname = self.fname
        lastname = self.lname
        myiter2  = iter(firstname)
        myiter3  = iter(lastname)
        print(next(myiter2))
        print(next(myiter2))
        print(next(myiter2))
        print(next(myiter2))
        print(next(myiter2))
        print(next(myiter3))
        print(next(myiter3))
        print(next(myiter3))
        print(next(myiter3))
        print(next(myiter3))

x=Name("Ajeya")
x.PrintName()
y=Display("Radha","Nayak")
y.DisplayName()
