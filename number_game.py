import random

print("Guessing Game")
print("Select a range from which you want to guess:")
while True:
    start_value = input ("Enter an integer start value\n")
    try:
        start_int = int(start_value)
        break
    except ValueError:
        print("Lets try again")
while True:
    end_value = input ("Enter an integer end value\n")
    try:
        end_int = int(end_value)
        break
    except ValueError:
        print("Lets try again")        
rand_num = random.randint(start_int,end_int)
chance = 5
guess_counter = 0
while guess_counter < chance:
    guess_counter+=1
    user_num = int(input("What do you think it is?\n"))
    if user_num == rand_num:
        print(f"You guessed it right in {guess_counter} tries")
        break
    elif user_num < rand_num:
        print(f"You gussed it too low, you have {chance-guess_counter} tries left")
    else:
        print(f"You gussed it too high, you have {chance - guess_counter } tries left")
    

