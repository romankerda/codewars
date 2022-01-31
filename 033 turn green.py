class SmartTrafficLight:
    def __init__(self, st1, st2):
        self.st1 = Street(*st1)
        self.st2 = Street(*st2)
        
    def turngreen(self):
        result = ''
        if self.st1.cars == self.st2.cars:
            return None
        elif self.st1.cars > self.st2.cars:
            self.st1.cars = 0
            return self.st1.name
        else:
            self.st2.cars = 0 
            return self.st2.name
    
class Street:
    def __init__(self, cars, name):
        self.cars = cars
        self.name = name
            
    
    
    
    
t = SmartTrafficLight([42, '27th ave'], [72, '3rd st'])