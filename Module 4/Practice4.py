smallest = 0
largest = 0
#smallest = smallest = 0
user_input = input("Number: ")

if user_input != "":
    number = float(user_input)
    smallest = largest = number

while user_input != "":
    number = float(user_input)

    if number < smallest:
        smallest = number
    if number > largest:
        largest = number
    user_input = input("Number: ")

print(f"Smallest: {smallest}")
print(f"Largest: {largest}")
