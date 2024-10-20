#5.1
print("Exercise 5.1")
import random
number_of_dices = int(input("How many dices you want to roll? "))
total_sum = 0
for i in range(number_of_dices):
    dice = random.randint(1,6)
    total_sum += dice
print(f"The sum of your {number_of_dices} dices are: {total_sum}")

#5.2
print("Exercise 5.2")
number_list = []
while True:
    input_number = input("Enter a number (or input empty string to quit): ")
    if input_number == "":
        break
    else:
        number_list.append(float(input_number))
number_list.sort(reverse = True)
print(f"5 greatest numbers are: {number_list[0:5]}")

#5.3
print("Exercise 5.3")
input_integer = int(input("Enter an integer: "))
if input_integer < 0:
    print("Number is negative, cannot be a prime number.")
elif input_integer == 0 or input_integer == 1:
    print("This is not a prime number.")
else:
    for i in range(2, input_integer):
        if input_integer % i == 0:
            print("This is not a prime number.")
            break
        i += 1
    else:
        print("This is a prime number.")

#5.4
print("Exercise 5.4")
city_list =[]
for times in range(0,5):
    name = input("Give a name of a city: ")
    city_list.append(name)
print("Names of 5 cities: ")
for city in city_list:
    print(city)
