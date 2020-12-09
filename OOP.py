class Car:
    wheels = 4
    doors = 4
    engine = True

    def __init__(self, model, year, make="Toyota"):
        self.make = make
        self.model = model
        self.year = year
        self.gas = 100
        self.is_moving = False

    def __str__(self):
        return f'{self.make} {self.model} {self.year}'

    def __eq__(self, other):
        return self.make == other.make and self.model == other.model

    def stop(self):
        if self.is_moving:
            print("the car has stopped")
            self.is_moving = False
        else:
            print('The car is already stopped')

    def go(self, speed):
        if self.use_gas():
            if not self.is_moving:
                print('The Car start moving')
                self.is_moving = True
            print(f'The Car is going {speed}')
        else:
            print('You have run out of gas')
            self.stop()

    def use_gas(self):
        self.gas -= 50
        if self.gas <= 0:
            return False
        else:
            return True

car_one = Car("Corolla", 2005)
car_two = Car("Camry", 2017)
car_three = Car("Desoto", 1948)

if car_one == car_two:
    print("equal")
else:   
    print("not equal")