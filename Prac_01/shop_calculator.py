"""
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen.
"""


total_cost = 0
valid_input = False
while valid_input is False:
    number_of_items = int(input("Enter number of items: "))
    if number_of_items > 0:
        valid_input = True
    else:
        print("Please enter a valid number")
for i in range(1, number_of_items + 1):
    cost = float(input("Please enter price of item: $"))
    total_cost += cost
if total_cost > 100:
    print("Total Price for {0:} items is ${1:.2f}".format(number_of_items, total_cost - (total_cost * 0.1)))
else:
    print("Total Price for {0:} items is {1:.2f}".format(number_of_items, total_cost))
