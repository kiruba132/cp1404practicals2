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
with open('numbers.txt', 'r') as file:
    Digit1 = int(in_file.readline())
    Digit2 = int(in_file.readline())
    print(f"Sum of first two numbers: {Digit1 + Digit2}")

# 4. Print the total of all numbers in 'numbers.txt'
total = 0
for line in in_file:
    number = int(line.strip())
    total += number
print("The sum of all lines is", total)
