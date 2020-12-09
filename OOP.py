class Car:
    wheels = 4
    doors = 4
    engine = True

car_one = Car()
car_two = Car()
print(car_one.doors)
print(car_two.doors)
print(Car.doors)

Car.doors = 2
car_one.doors = 7
print(car_one.doors)
print(car_two.doors)
print(Car.doors)