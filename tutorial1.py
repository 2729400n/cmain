# Property of Kevin
# The code Below takes a number then multiplies
# it by the number -1. then does that gain and again until it gets to 1
# e.g. if the number which we will call n; is equal to 9 it would be
# 9*(9-1)*(9-1-1)*(9-1-1-1)...
# 9*8*7*6*5*4*3*2*1
# if n =0 the factorial function should return 1


import sys
import os
import subprocess
from pathlib import Path, WindowsPath


def is_older(age_1, age_2):
    if age_1 > age_2:
        print("Person with age_1 is older than person with age_2")
    elif age_2 > age_1:
        print("Person with age_2 is older than person with age_1")
    elif age_1 == age_2:
        print("Person with age_1 is the same age as person with age_2")


#


if len(sys.argv) < 3:
    print(
        f"Not enough Ages given to program\nrun the program with\n\n\tpython {sys.argv[0]} [age_1] [age_2]\n\n")
    sys.exit(1)

age_1_user_input = eval(sys.argv[1])
age_2_user_input = eval(sys.argv[2])
print("Age program starting up!")
print(f"age_1 = {age_1_user_input}")
print(f"age_2 = {age_2_user_input}")
if not (age_1_user_input and  age_2_user_input ):
    print("Age must be a decimal!")
    sys.exit(1)


age_1_user_input = float(age_1_user_input)
age_2_user_input = float(age_2_user_input)

is_older(age_1_user_input, age_2_user_input)

# The function is called factorial and it takes a number n
# n can only be an number in the range  [0, inf], and a whole number
# def factorial( n:int ):
# if ((n*-1)*(-1))
