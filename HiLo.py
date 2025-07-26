import random
import math
MAXRANGE=2048
def HigherOrLower():
    x =random.randint(0,MAXRANGE)
    print(f"Bonus points if you guess it in {math.log2(MAXRANGE)//1+1}!")
    
    num_of_guesses =int(math.log2(MAXRANGE)//1+5)
    print(f"You get {num_of_guesses} guesses!")
    print(f"What number is x? x is between 0 and {MAXRANGE}!")
    for i in range(num_of_guesses):
        user_guess_of_x=int(input(">>> "))
        if user_guess_of_x == x:
            print(f"Well done that is x!")
            print(f"x was {x}")
            break
        else:
            print(f"Try again! {'higher' if x>user_guess_of_x else 'lower'}")
            print(f"Hint the number is greater than 0 less than {MAXRANGE}")

if __name__=='__main__':
    HigherOrLower()