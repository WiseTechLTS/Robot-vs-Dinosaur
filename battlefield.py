from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Robot("Robot", 55)
        self.dinosaur = Dinosaur("Dinosaur", 45)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
    
    def display_welcome(self):
    # display a message
        print("Welcome to Robot VS Dinosaur")
    
    
    def battle_phase(self):
    # use a while loop to allow both sides to attack eachother until one has no health
       

            
    def display_winner(self):
        # use if statement to check if dino has health, display dino as winner 
        # else display robot as winner
     