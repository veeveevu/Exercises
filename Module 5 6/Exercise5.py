#5.1
import random
num_of_dices = int(input("How many dices you want to roll? "))
total_sum = 0
for i in range(num_of_dices):
    dice = random.randint(1,6)
    total_sum += dice
print(f"The sum of the numbers: {total_sum}")

#5.2
number_list = []
number = input("Enter a number (or press Enter to quit): ")
while number != "":
    number_list.append(float(number))
    number = input("Enter a number (or press Enter to quit): ")
number_list.sort(reverse = True)
print(f"5 numbers: {number_list[0:5]}")

#5.3
user_input = int(input("Enter an integer: "))
if user_input < 0:
    print("Number is negative, cannot be a prime number.")
elif user_input == 0 or user_input == 1:
    print("This is not a prime number.")
else:
    for i in range(2, user_input):
        if user_input % i == 0:
            print("This is not a prime number")
            break
        i += 1
    else:
        print("This is a prime number")

#5.4
cities =[]
for times in range(0,5):
    name = input("Give a name of a city: ")
    cities.append(name)
print("Names of 5 cities: ")
for i in cities:
    print(i)
