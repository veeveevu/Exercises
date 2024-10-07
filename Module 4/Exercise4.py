#4.1
number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1

#4.2
num = input("Insert value in inches: ")
while True:
    if float(num) >= 0:
        print(f"In centimeters: {float(num)*2.54}")
        num = float(input("Insert another value in inches: "))
    else:
        print("Invalid!")

#4.3
largest = None
smallest = None
while True:
    value = input("Enter a number: ")
    if value == "":
        break
    else:
        value1 = float(value)
        if largest is None or value1 > largest:
            largest = value1
        if smallest is None or value1 < smallest:
            smallest = value1
if largest is not None and smallest is not None:
    print(f"Largest number: {largest}")
    print(f"Smallest number: {smallest}")

#4.4
import random
draw = random.randint(1, 10)
guess = int(input("Guess a number: "))
while guess != draw:
    if guess > draw:
        print("The number is too high")
    else:
        print("The number is too low")
    guess = int(input("Guess another number: "))
print("Correct!")

#4.5
correct_username = "python"
correct_password = "rules"
attempt = 0
while attempt < 5:
    username = input("Insert your username: ")
    passwrd = input("Insert your password: ")
    if username == correct_username and passwrd == correct_password:
        print("Welcome.")
        break
    else:
        print("Try again!")
    attempt += 1
if attempt == 5:
    print("Access denied")

#4.6
total_points = int(input("How many random points should we generate? "))
#test if N points belong A
import random
i = 0
n = 0
while i < total_points:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if (x**2 + y**2) < 1:
        n += 1
    i += 1
pi_value = 4*n/total_points
print(f"Approximate value of pi is {pi_value}")












