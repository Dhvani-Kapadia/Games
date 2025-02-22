
import random
print("Lets play rock paper & sissor")
print("Enter out of the three options:")
print("Rock -> r")
print("Paper -> p")
print("Scissor -> s")
print("To quit enter any other character")

options = ["r","p","s"]
while True:
    player1= input("Whats your choice:").lower()
    player2 = random.choice(options)
   #user is player1; computer is player2 
    if player1 == player2:
        print("Its a draw")
    elif(player1 == 'r' and player2 == 's') or (player1 == 'p' and player1 == 'r') or (player1 == 's' and player1 == 'r') :
        print("You win!")
        print(f"My choice was {player2}")
    
    elif player1 not in options:
        print("The game has now ended")
        break
    else:
        print("Better luck next time")
        print(f"My choice was {player2}")

