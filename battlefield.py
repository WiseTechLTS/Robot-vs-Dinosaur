from robot import Robot
from dinosaur import Dinosaur

robot = Robot("Robot", 150, 65)
robot.attack()
dinosaur = Dinosaur("Dinosaur", 150, 45)
dinosaur.attack()

class Battlefield:
    def __init__(self):
        self.robot = Robot
        self.dinosaur = Dinosaur 
    def __init__(robot):
        super().__init__()
    def __init__(dinosaur):
        super().__init__()


    def run_game(self):
        self.display_welcome = ()
        self.battle_phase = ()
        self.display_winner = ()
        
    def display_welcome(self):
        self.display_welcome = "Welcome to R O B O T vs D I N O S A U R"
        print(self.display_welcome)
    
    def battle_phase(self):
        pass

class Robot(Battlefield):
    def __init__(self):
        self.choice = ""
        self.health = int
        super().__init__()

    def battle_phase(self):
        self.dinosaur -= 65
        print(dinosaur.health - self.dinosaur)
class Dinosaur(Battlefield):
    def __init__(self):
        self.choice = ""
        self.health = int
        super().__init__()

    def battle_phase(self):
        self.robot -= 45        
        print(robot.health - self.robot)