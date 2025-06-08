# files.py

# 1. Ask the user for their name and write it to 'name.txt'
out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)
out_file.close()

# 2. read() method
in_file = open('name.txt', 'r')
name_from_file = in_file.read().strip()
in_file.close()
print(f"Hi {name_from_file}!")

# 3. Read the first two numbers from 'numbers.txt' and print their sum
with open('numbers.txt', 'r') as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
print(f"Sum of first two numbers: {first_number + second_number}")

# 4. Print the total of all numbers in 'numbers.txt'
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line.strip())
        total += number
print(f"The sum of all lines is {total}")
