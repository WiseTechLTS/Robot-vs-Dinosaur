from robot import Robot
from dinosaur import Dinosaur

robot = Robot("Robot")
dinosaur = Dinosaur("Dinosaur", 12)

class Battlefield:
    def __init__(self):
        self.robot = Robot("Robot", 15)
        self.dinosaur = Dinosaur("Dinosaur", 12)

    def run_game(self):
        self.display_welcome(self)
        self.battle_phase(self)
        self.display_winner(self)
    
    def display_welcome(self):
    # display a message
        print("Welcome to Robot VS Dinosaur")
    
    
    def battle_phase(self):
    # use a while loop to allow both sides to attack eachother until one has no health
        while(robot.health or dinosaur.health >0):
            robot.attack(dinosaur)
            print(robot.health, "robot health")
            if(dinosaur.health >0):
                dinosaur.attack(robot)
                print(dinosaur.health, "dino health")
            else:
                print("Battle Phase over")
                return True       

            
    def display_winner(self):
        # use if statement to check if dino has health, display dino as winner 
        # else display robot as winner
        if(dinosaur.health >0):
            print("Dinosaur is the winner")
        else:
            print("Robot wins!")