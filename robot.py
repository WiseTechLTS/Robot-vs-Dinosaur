from weapon import Weapon

weapon = Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 150
        self.active_weapon = Weapon("Turok Axe", 25)

    def attack(self, dinosaur):  
        
        pass
