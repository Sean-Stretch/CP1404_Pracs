"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if score not in range(0, 101):
    print("Invalid score")
else:
    if score > 100:
        print("Invalid score")
    if score >= 90:
        print("Excellent")
    if score >= 50:
        print("Passable")
    if score < 50:
        print("Bad")