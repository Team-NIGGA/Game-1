import time
import random
from random import randint
from time import sleep

random = randint(1,3)
print(random) # For Debbuging Purpose 
user = int(input('''

1-stone
2-paper
3-scissor

'''))

if random == user:
    print("tie")

elif random == 1 and user == 2:
    print("user wins")

elif random == 2 and user == 3:
    print("user wins")

elif random == 3 and user == 1:
    print("user wins")

else:
    print("Machine Wins!")
