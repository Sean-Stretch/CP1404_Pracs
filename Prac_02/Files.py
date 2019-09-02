

# Part 1

user_name = input("Enter username: ")
out_file = open("name.txt", 'w')
out_file.write(user_name)
out_file.close()

# Part 2
in_file = open("name.txt", 'r')
user_name = in_file.read()
print("Your name is {}".format(user_name))
in_file.close()

# Part 3A

out_file = open("numbers.txt" 'w')
out_file.write("17\n42")
out_file.close()

# Part 3B


out_file = open("numbers.txt", 'w')
for i in range(5):
    out_file.write(input("Please enter some numbers: "))

number_list = [" "]
out_file = open("numbers.txt", 'r')
for number in out_file:
    add_to_list = out_file.readline()
    number_list.append(add_to_list)
print(number_list)


#in_file = open("numbers.txt", 'r')
#total = 0
#for line in in_file:
#     total += int(line)
# in_file.close()
# print(total)

