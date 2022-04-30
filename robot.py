from weapon import Weapon

weapon = Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 150
        self.active_weapon = Weapon("Turok Axe", 15)

    def attack(self, dinosaur):  
        dinosaur.health = dinosaur.health - self.active_weapon.attack_power
        print("Robot attack over")
        return dinosaur.health 