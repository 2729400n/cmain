import random

def createGame():
    x=random.randint(0,255) # pick a random number x between 0 and 100 ; can include 0 or 100
    y,z = [ random.randint(1,20) for i in range(2)] # pick to random number y and z between 0
    print(f"x % {y}= {x%y}")
    print(f"x % {z}= {x%z}")
    print("What number is X? X is between 0 and 100!")

    for i in range(10):
        user_guess_of_x=int(input(">>> "))
        if user_guess_of_x == x:
            print(f"Well done that is x!")
            print(f"x={x},\ny={y},\nz={z}")
            break
        else:
            print("Try again!")




createGame()


# 4 !
# 24 !
# 44 
# 64
# 84