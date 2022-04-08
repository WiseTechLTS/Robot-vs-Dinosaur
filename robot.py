from weapon import Weapon
weapon = Weapon

class Robot:
    def __init__(self, name):
        self.name = name 
        self.health = 150
        self.active_weapon = Weapon("Turok Axe", 2)

    def attack(self, dinosaur):
        if dinosaur.health != 0:
            dinosaur.health = dinosaur.health - self.weapon.attack_power 
            print(f'{self.name} critical damage {self.weapon.attack_power} done to {dinosaur.name}')
            print(f'{dinosaur.name} has {dinosaur.health} health remaining')
        self.dinosaur -= 65

class Weapon(Robot):
    def __init__(self):
        self.name = ("Weapon")
        self.attack_power = (int)
        super().__init__()
    def attack_power(self):
        self.attack_power = 65
        print(self.attack_power)