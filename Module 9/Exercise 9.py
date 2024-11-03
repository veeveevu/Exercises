import random
#9.1
print("Exercise 9.1")
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

#-----------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    car0 = Car("ABC-123", 142)

    print(f"Car registration number: {car0.reg_num}, maximum speed: {car0.max_speed} km/h")

    # 9.2
    print("Exercise 9.2")

    car0.accelerate(30)
    car0.accelerate(70)
    car0.accelerate(50)
    car0.print_speed()

    car0.accelerate(-200)
    car0.print_speed()

    # 9.4
    print("Exercise 9.4")
    cars = []
    for i in range(10):
        registration_num = f"ABC-{i + 1}"
        maximum_speed = round(random.uniform(100, 200), 2)
        car = Car(registration_num, maximum_speed)
        cars.append(car)

    total_distance = 0
    winner = None
    while total_distance < 10000:
        for car in cars:
            car.accelerate(round(random.uniform(-10, 15), 2))
            car.drive(1)
            if car.distance >= total_distance:
                total_distance = car.distance
                winner = car

    # -------------------------------------------------------------
    print("-" * 88)
    print(f"{'Car':^7} {'Registration number':^25} {'Maximum speed (km/h)':^25} {'Final distance (km)':^25}")
    print("-" * 88)
    y = 1
    for x in cars:
        print(f"{y:^7} {x.reg_num:^25} {x.max_speed:^25} {round(x.distance, 2):^25}")
        y += 1
    print("-" * 88)

    print(f"The winner is the car with registration number: {winner.reg_num}")
