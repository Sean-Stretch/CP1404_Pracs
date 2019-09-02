"""
"quick picks" lottery ticket generator
Write a program that asks the user how many "quick picks" they wish to generate.
The program then generates the amount of lines the user entered. Each line consists of 6 random numbers between 1 and 45.
THe values 1 - 45 should be stored as constants.
"""
import random

MIN_RANDOM = 1
MAX_RANDOM = 45

number_of_quick_picks = int(input("Enter number of quick picks: "))
while number_of_quick_picks not in range(MIN_RANDOM, MAX_RANDOM + 1):
    number_of_quick_picks = int(input("Enter number of quick picks: "))

# creates list of picks

# loops for the amount of picks requested
for pick in range(number_of_quick_picks):

    quick_picks = []
    for picks in range(6):
        quick_pick = random.randint(MIN_RANDOM, MAX_RANDOM)
        while quick_pick in quick_picks:
            quick_pick = random.randint(MIN_RANDOM, MAX_RANDOM)
        quick_picks.append(quick_pick)
    print(sorted(quick_picks))