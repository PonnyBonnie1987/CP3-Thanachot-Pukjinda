class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("True On : Air")
class Car(Vehicle):
    pass
class Pickup(Vehicle):
    pass
class Van(Vehicle):
    pass
class EstateCar(Vehicle):
    pass

car1 = Car()
car1.turnOnAirConditioner()

Pickup1 = Pickup()
Pickup1.turnOnAirConditioner()

Van1 = Van()
Van1.turnOnAirConditioner()

EstateCar1 = EstateCar()
EstateCar1.turnOnAirConditioner()