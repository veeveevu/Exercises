
#6.1
print("Exercise 6.1")
import random
def roll_a_dice():
    num1 = random.randint(1,6)
    return num1

while True:
    result_1 = roll_a_dice()
    if result_1 == 6:
        print(result_1)
        print("Congrats! You rolled a 6!")
        break
    else:
        print(result_1)
        result = roll_a_dice()


#6.2
print("Exercise 6.2")
def roll_dice_with_sides(sides):
    num2 = random.randint(1, sides)
    return num2
sides = int(input("How many sides does your dice have? "))

while True:
    result_2 = roll_dice_with_sides(sides)
    if result_2 == sides:
        print(result_2)
        print("Congrats! You rolled the max number on this dice!")
        break
    else:
        print(result_2)
        result_2 = roll_dice_with_sides(sides)


#6.3
print("Exercise 6.3")
def convert(input_3):
    num3 = input_3*3.785
    return num3
gallon = float(input("Enter the quantity of gasoline in gallons: "))

while True:
    result_3 = convert(gallon)
    if result_3 < 0:
        print("Negative inputs are invalid!")
        break
    else:
        print(f"In liters: {result_3}")
        gallon = float(input("Enter the quantity of gasoline in gallons: "))


#6.4
print("Exercise 6.4")
def integer_list(numbers):
    sum_list = 0
    for i in numbers:
        sum_list += i
    return sum_list

input_list = [1,7,2,4,8,9]
print(f"The input list is: {input_list}")

result_4 = integer_list(input_list)
print(f"Total sum is: {result_4}")

#6.5
print("Exercise 6.5")
def remove_uneven(number_list):
    new_list = []
    for number in number_list:
        if number % 2 == 0:
            new_list.append(number)
    return new_list

my_list = [1,2,3,4,5,6,7,8,9]
print(f"The input list is {my_list}")
print(f"New cut-down list: {remove_uneven(my_list)}")

#6.6
print("Exercise 6.6")
import math
def unit_price(diameter, price):
    area = ((diameter / 2) ** 2) * math.pi
    price_per_square_meter = price/area
    return price_per_square_meter

print(f"Pizza 1")
diameter1 = float(input("Insert diameter in centimeters: "))
price1 = float(input("Insert price in euros: "))
unit_price1 = unit_price(diameter1, price1)
print(f"The unit price is {unit_price1:.4f}")

print("Pizza 2")
diameter2 = float(input("Insert diameter in centimeters: "))
price2 = float(input("Insert price in euros: "))
unit_price2 = unit_price(diameter2, price2)
print(f"The unit price is {unit_price2:.4f}")

if unit_price1 < unit_price2:
    print("Pizza 1 is better in money value!")
elif unit_price1 > unit_price2:
    print("Pizza 2 is better in money value!")
else:
    print("Pizza 1 and pizza 2 offer same money value!")


