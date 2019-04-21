#P5HW1- Rock, Paper, Scissor Game
#CTI-110
#Ciera Dunigan-Hogan
#18 April 2019
#


#import random module 
import random 
  
print("Rock, paper, scissor rules: \n"
                                +"Rock vs Paper = Paper wins \n"
                                + "Rock vs Scissor = Rock wins \n"
                                +"Paper vs Scissor = Scissor wins \n") 
  
while True: 
    print("Enter choice \n 1. Rock \n 2. Paper \n 3. Scissor \n") 
      
#Get input from user 
    uChoice = int(input("User turn: ")) 

 
    while uChoice > 3 or uChoice < 1: 
        uChoice = int(input("Enter a valid number (1, 2, or 3): ")) 
          
#Variables
    if uChoice == 1: 
        rps = 'Rock'
    elif uChoice == 2: 
        rps = 'paper'
    else: 
        rps = 'scissor'
          
#Print users choice  
    print("You chose: " + rps) 
  
#Computer output
    cChoice = random.randint(1, 3) 
      
    while cChoice == uChoice: 
        cChoice = random.randint(1, 3)
        
    if cChoice == 1: 
        cRPS = 'Rock'
    elif cChoice == 2: 
        cRPS = 'paper'
    else: 
        cRPS = 'scissor'
          
    print("Computer chose: " + cRPS) 
  
    print( rps + " vs " + cRPS) 
  
    if((uChoice == 1 and cChoice == 2) or
      (uChoice == 2 and cChoice ==1 )): 
        print("Paper wins, ", end = "") 
        result = "Paper"
          
    elif((uChoice == 1 and cChoice == 3) or
        (uChoice == 3 and cChoice == 1)): 
        print("Rock wins, ", end = "") 
        result = "Rock"
    else: 
        print("Scissor wins, ", end = "") 
        result = "Scissor"
  
#Display results
    if result == uChoice: 
        print("user beats computer!") 
    else: 
        print("computer beats user!") 
          
    print("Do you want to play again? (Y/N)") 
    ans = input() 
  
  
    if ans == 'n' or ans == 'N': 
        break
      
print("Thanks for playing!") 
