#2.1
name=input("What is your name? ")
print("Hello, " + name + "!")

#2.2.
radius=float(input("Insert the radius of a circle: "))
import math
area=radius**2*math.pi
print(f"Area: {area:.2f}")

#2.3
length=float(input("Insert the length of a rectangle: "))
width=float(input("Insert the width: "))
perimeter=2*(length+width)
area_rectangle=length*width
print(f"Perimeter: {perimeter:.2f} \nArea: {area_rectangle:.2f}")

#2.4
number1=int(input("Insert the first integer number: "))
number2=int(input("Insert the second integer number: "))
number3=int(input("Insert the third integer number: "))
sum123=number1+number2+number3
product=number1*number2*number3
average=sum123/3
print(f"Sum = {sum123}")
print(f"Product = {product}")
print(f"Average = {average:.2f}")

#2.5
print("Enter these medieval units: ")
talent=float(input("Talents: "))
pound=float(input("Pounds: "))
lot=float(input("Lots: "))
total_lots=talent*20*32+pound*32+lot
all_grams=total_lots*13.3
kilograms=int(all_grams//1000) #// means division for integer result
grams=all_grams%1000 #% means modulo (remainder of dividing)
print(f"The total weight in modern units: \n{kilograms} kilograms and {grams:.2f} grams.")

#2.6
import random #Python's random module
number1=random.randint(0,9)
number2=random.randint(0,9)
number3=random.randint(0,9)
print(f"3 digit code: {number1} {number2} {number3}")

number4=random.randint(1,6)
number5=random.randint(1,6)
number6=random.randint(1,6)
number7=random.randint(1,6)
print(f"4 digit code: {number4} {number5} {number6} {number7}")

