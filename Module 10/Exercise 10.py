#10.1
print("Exercise 10.1")
class Elevator:
    def __init__(self, bottom: int, top: int):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def go_to_floor(self, floor: int):
        self.floor = floor
        if floor < self.bottom or floor > self.top:
            print("Invalid floor in this building.")
            return
        
        print(f"You are now at floor {self.current_floor}.")
        if self.current_floor < floor:
            self.floor_up()
        elif self.current_floor > floor:
            self.floor_down()
        else:
            print(f"You are already at floor {self.floor}")

    def floor_up(self):
        while self.current_floor < self.floor:
            self.current_floor += 1
            print(f"    Going to floor {self.current_floor}...")
        print("You reach your floor!")

    def floor_down(self):
        while self.current_floor > self.floor:
            self.current_floor -= 1
            print(f"    Going to floor {self.current_floor}...")
        print("You reach your floor!")




hissi = Elevator(1, 10)
hissi.go_to_floor(6)
hissi.go_to_floor(1)
print("-"*50)

#10.2
print("Exercise 10.2")
class Building:
    def __init__(self, bottom: int, top: int, total_elevators: int):
        self.bottom = bottom
        self.top = top
        self.total_elevators = total_elevators
        self.elevator_list =[]
        for i in range(total_elevators):
            elevator = Elevator(self.bottom, self.top)
            self.elevator_list.append(elevator)

    def run_elevator(self, elevator_number: int, destination_floor: int):
        current_elevator = self.elevator_list[elevator_number - 1]
        print(f"Chosen elevator number {elevator_number} to go to floor {destination_floor}...")
        current_elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        print(f"There is a fire alarm!")
        for elevator in self.elevator_list:
            print(f"Elevator number {self.elevator_list.index(elevator) + 1} is going to bottom floor.")
            elevator.go_to_floor(self.bottom)
        print("Now all elevators are at bottom floor!")


karamalmi = Building(1, 9, 3)

#run elevator number 1 to floor 5 then to floor 3
karamalmi.run_elevator(1, 5)
karamalmi.run_elevator(1, 3)
#run elevator number 2 to floor 7
karamalmi.run_elevator(2, 7)
#run elevator number 3 to floor 4
karamalmi.run_elevator(3, 4)
print("-"*50)

#6.3
print("Exercise 6.3")
karamalmi.fire_alarm()


















