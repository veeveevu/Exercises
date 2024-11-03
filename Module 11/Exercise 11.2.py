# 11.2
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

class ElectricCar(Car):
    def __init__(self, reg_num: str, max_speed: float, battery_capacity: float):
        super().__init__(reg_num, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, reg_num: str, max_speed: float, tank_volume: float):
        super().__init__(reg_num, max_speed)
        self.tank_volume = tank_volume

if __name__ == "__main__":
    tesla = ElectricCar("ABC-15", 180, 52.5)
    toyota = GasolineCar("ACB-123", 165, 32.3)

    tesla.accelerate(120)
    toyota.accelerate(110)

    tesla.drive(3)
    toyota.drive(3)

    print(f"Electric car: {tesla.reg_num} travelled {tesla.distance} km")
    print(f"Gasoline car: {toyota.reg_num} travelled {toyota.distance} km")