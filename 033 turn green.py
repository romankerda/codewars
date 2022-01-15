class SmartTrafficLight:
    def __init__(self, st1, st2):
        self.st1 = st1
        self.st2 = st2
        
    def turngreen(self):
        result = ''
        if self.st1[0] == self.st2[0]:
            return None
        elif self.st1[0] > self.st2[0]:
            result = st1[1]
            self.st1[1] = 0
        else:
            result = st1[1]
            self.st2[2] = 0 
        return result
            
    
    
    
    
t = SmartTrafficLight([42, '27th ave'], [72, '3rd st'])