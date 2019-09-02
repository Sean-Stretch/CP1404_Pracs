list_of_numbers = []
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

for number in range(5):
    user_numbers = int(input("enter number: "))
    list_of_numbers.append(user_numbers)
print(list_of_numbers)
print("First number is: {}".format(list_of_numbers[0]))
print("Last number is: {}".format(list_of_numbers[-1]))
print("Largest number is: {}".format(max(list_of_numbers)))
print("Smallest number is: {}".format(min(list_of_numbers)))
print("Average of all numbers is: {}".format(sum(list_of_numbers) // len(list_of_numbers)))

user_name = input("Please enter your username: ")
if user_name not in usernames:
    print("Access Denied")
else:
    print("Access Granted")


