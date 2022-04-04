from weapon import Weapon

weapon = Weapon('Weapon', 33)

class Robot:
    def __init__(self, name):
        self.name = ""
        self.health = 150
        self.active_weapon = Weapon
    
    def set_name(self):
        self.name = "Robot"
    
    def attack(self,dinosaur):
        
        
