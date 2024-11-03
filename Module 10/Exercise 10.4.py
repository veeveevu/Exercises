import random
#10.4
print("Exercise 10.4")
class Car:
    def __init__(self, reg_num: str, max_speed: float, current_speed: float = 0.0, distance: float = 0.0):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.distance = distance

    def accelerate(self, speed_change: float):
        new_speed = max(0.0, min(self.current_speed + speed_change, self.max_speed))
        self.current_speed = new_speed

    def print_speed(self):
        print(f"Car current speed is: {self.current_speed}")

    def drive(self, num_of_hours: float):
        self.distance += (num_of_hours * self.current_speed)

class Race:
    def __init__(self, name: str, kilometer: float, car_lists: list):
        self.name = name
        self.kilometer = kilometer
        self.car_lists = car_lists
        self.total_hours = 0
        self.winner = None

    def hour_passes(self):
        self.total_hours += 1
        for car in self.car_lists:
            car.accelerate(round(random.uniform(-10, 15), 2))
            car.drive(1)

    def print_status(self):
        print("-" * 88)
        print(f"{'Car':^7} {'Registration number':^25} {'Maximum speed (km/h)':^25} {'Final distance (km)':^25}")
        print("-" * 88)
        y = 1
        for x in self.car_lists:
            print(f"{y:^7} {x.reg_num:^25} {x.max_speed:^25} {round(x.distance, 2):^25}")
            y += 1
        print("-" * 88)

    def race_finished(self):
        for car in self.car_lists:
            if car.distance >= self.kilometer:
                self.winner = car
                return True
        return False

#----------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    list_of_car = []

    for i in range(10):
        registration_num = f"ABC-{i + 1}"
        maximum_speed = round(random.uniform(100, 200), 2)
        car = Car(registration_num, maximum_speed)
        list_of_car.append(car)

    new_race = Race("Grand Demolition Derby", 8000, list_of_car)
    print(f"Race: {new_race.name}\n"
          f"Distance: {new_race.kilometer} km")

    while True:
        new_race.hour_passes()
        race_status = new_race.race_finished()

        if new_race.total_hours % 10 == 0:
            print(f"🔹Status after {new_race.total_hours} hours")
            new_race.print_status()

        if race_status:
            break
    print(f"Race is finished!!!\n"
          f"Total hours: {new_race.total_hours}\n"
          f"Winner is car with registration number {new_race.winner.reg_num}")
    new_race.print_status()


