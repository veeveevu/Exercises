#3.1
length = float(input("Enter the length of the zander: "))
below_size = 42 - length
if 0 < length < 42:
    print(f"Please release the fish back into the lake \nIt is {below_size}cm below the size limit ")
else:
    print("It is okay to catch")

#3.2
cabin = input("Enter the cabin class: ")
if cabin == "LUX":
    print("It is an upper-deck cabin with a balcony")
elif cabin == "A":
    print("It is an above the car deck, equipped with a window.")
elif cabin == "B":
    print("It is a windowless cabin above the car deck.")
elif cabin == "C":
    print("It is a windowless cabin below the car deck.")
else:
    print("Invalid cabin class")

#3.3
gender = input("Enter your gender: ")
hemoglobin = float(input("Enter your hemoglobin value: "))
if gender == "female":
    if 117 <= hemoglobin <= 155:
        print("Normal hemoglobin value")
    elif hemoglobin < 117:
        print("Low hemoglobin value")
    else:
        print("High hemoglobin value")
if gender == "male":
    if 134 <= hemoglobin <= 167:
        print("Normal hemoglobin value")
    elif hemoglobin < 134:
        print("Low hemoglobin value")
    else:
        print("High hemoglobin value")

#3.4
year = int(input("Enter a year: "))
if year % 100 == 0:
    if year % 400 == 0:
        print("It is a leap year.")
    else:
        print("It is not a leap year.")
elif year % 4 == 0:
    print("It is a leap year.")
else:
    print("It is not a leap year.")




