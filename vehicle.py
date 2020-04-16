class Vehicle:
    def __init__(self, color, max_speed, model, owner):
        self.color = color.lower()
        self.max_speed = max_speed
        self.model = model
        self.owner = owner
    
    def drive(self):
        print('The vehicle is driving, wow')

    
    def turn(self, direction):
        print(f"The vehicle is turning {direction} direction")

    def stop(self):
        print('after the long grind and screech or rubber and steel the vehicle comes to halt')
        
    
    