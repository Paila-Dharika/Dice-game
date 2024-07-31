import random
def main():
     
     
    print("Welcome to the Two Dice Pig Game. You are Player 1!")
     
     
    p1dice = random.randrange(1,7)
    p1dice2 = random.randrange(1,7)
    p2dice = random.randrange(1,7)
    p2dice2 = random.randrange(1,7)
    Player1 = p1dice+p1dice2
    Player2 = p2dice+p2dice2
     
    while(Player1<100 or Player2<100):
         
         
        print("Player 1 dice 1 =",p1dice)
        print("Player 1 dice 2 =",p1dice2)
        print("Player 1 dice total =",Player1)
        print("Does player 1 want to hold?")
        choose1 = input("Enter y for yes or n for no.")
        if(choose1=="n"):
            print("Player 1 dice 1 =",p1dice)
            print("Player 1 dice 2 =",p1dice2)
            print("Player 1 dice total =",Player1)
            print("Does player 1 want to hold?")
            choose1 = input("Enter y for yes or n for no.")
        elif(choose1=="y"):
             
            print("It's player 2's turn.")
            print("Player 2 dice 2 =",p2dice)
            print("Player 2 dice 2 =",p2dice2)
            print("Player 2 dice total =",Player2)
            print("Does player 2 want to hold?")
            choose2 = input("Enter y for yes or n for no.")
         
     
     
     
     
main()
