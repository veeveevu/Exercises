#7.1
print("Exercise 7.1")
spring = ("3", "4", "5")
summer = ("6", "7", "8")
autumn = ("9", "10", "11")
winter = ("12", "1", "2")

user_input = input("Give me a number of a month: ")

if user_input in spring:
    print("It's in spring!")
elif user_input in summer:
    print("It's in summer!")
elif user_input in autumn:
    print("It's in autumn!")
elif user_input in winter:
    print("It's in winter!")
else:
    print("Invalid month!")

#7.2
print("Exercise 7.2")
name_list = set()

while True:
    name_input = input("Enter a name (or enter an empty string to quit): ")
    if name_input == "":
        break
    elif name_input in name_list:
        print("Existing name!")
    else:
        name_list.add(name_input)
        print("New name added!")

print("List of all names:")
for i in name_list:
    print(i)

#7.3
print("Exercise 7.3")
airport_data = {
    "KATL" : "Hartsfield–Jackson Atlanta International Airport",
    "OMDB" : "Dubai International Airport",
    "KDFW" : "Dallas Fort Worth International Airport",
    "EGLL" : "Heathrow Airport",
    "RJTT" : "Tokyo Haneda Airport",
    "LTFM" : "Istanbul Airport",
    "KLAX" : "Los Angeles International Airport"
}

while True:
    choice = input("Type: \nA to enter a new airport \nB to fetch the information of an existing airport \nC to quit:\n").strip().lower()
    if choice == "c":
        break
    elif choice == "b":
        fetch_code = input("Enter the ICAO code: ").strip().upper()
        if fetch_code in airport_data:
            print(f"The corresponding airport is {airport_data[fetch_code]}")
        else:
            print("Airport not found!")
    elif choice == "a":
        enter_name = input("Enter airport name: ")
        enter_icao = input("Enter the corresponding ICAO code: ").strip().upper()
        if enter_icao in airport_data:
            print("Airport already exists.")
        else:
            airport_data[enter_icao] = enter_name
            print(f"Airport {enter_name} with ICAO code {enter_icao} is added.")
    else:
        print("Invalid choice!")

print("The final airport data list:")
for a,b in airport_data.items():
    print(f"{a} : {b}")
