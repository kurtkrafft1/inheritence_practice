from vehicle import Vehicle

class Tesla(Vehicle):

    def __init__(self, color, max_speed, model, owner, kwh):
        super().__init__(color, max_speed, model, owner)
        self.kwh = kwh 

    def drive(self):
        print("The Tesla drives itself!")
    
class Lexus(Vehicle):
    
    def __init__(self, color, max_speed, model, owner, mileage):
        super().__init__(color, max_speed, model, owner)
        self.mileage = mileage

    def drive(self):
        print(f"This is {self.owner}'s car, it is {self.color} and boy can he whip it")
    
class Tank(Vehicle):
    def __init__(self, color, max_speed, model, owner, mileage, passengers, loaded):
        super().__init__(color, max_speed, model, owner)
        self.mileage = mileage
        self.passengers = passengers
        self.loaded = loaded

    def armed_check(self):
        if self.loaded==True:
            print("careful dude, shes hot")
        else:
            print('We good, you want a beer?')

    def drive(self):
        print(f"this is {self.owner}'s car it is {self.color} and it started moving'")
    


    

class Airplane(Vehicle):

    def __init__(self, color, max_speed, model, owner, mileage, wing_span, passengers):
        super().__init__(color, max_speed, model, owner)
        self.mileage = mileage
        self.wing_span = wing_span
        self.passengers = passengers
    def drive(self):
        print('voooosh')



class AstonMartin(Vehicle):

    def __init__(self, color, max_speed, model, owner, mileage):
        super().__init__(color, max_speed, model, owner)
        self.mileage = mileage
    
    def drive(self):
        print("Out of no where James Bond slides into your car and pushes you out says 'sorry MI6 business' and just like that you knew, fuck that guy")
    

model_c = Tesla('White', 120, "model C", 'Kurt', 80)
gx470 = Lexus('Gold', 100, "GX470", 'Kurt', 300)
big_boy = Tank('Camo', 50, 'Big Boy', 'The Army', 400, 4, True)
fighter_jet = Airplane('silver', 400, 'Fighter Jet', 'The Navy', 1000,50,2)
db5 = AstonMartin('Silver', 200, 'db5', 'Gill Bates', 200)


print(model_c.color)
model_c.stop()
print(gx470.color)
gx470.stop()
print(fighter_jet.color)
fighter_jet.stop()
print(big_boy.color)
big_boy.stop()
print(db5.color)
db5.stop()