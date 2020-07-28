# this is comment
class Vehicle:
    def __init__(self, vwheel, vcolor):
        self.wheel = vwheel
        self.color = vcolor
        
    def waganprop(self):
        print(self.wheel)
        print(self.color)
        
veh1 = Vehicle("Two Wheeler", "Red")
veh2 = Vehicle("Four Wheeler", "Grey")
veh1.waganprop()
veh2.waganprop()