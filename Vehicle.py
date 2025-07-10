class Vehicle:
    def navigate(self):
        print("navigate via vehicle")
class Car(Vehicle):
    def navigate(self):
        print("vehicle via car")
class Bicycle(Vehicle):
    def navigate(self):
        print("vehicle via Bicycle")
v=Bicycle()
v.navigate()
c=Car()
c.navigate()
for v in [Car(),Bicycle()]:
    v.navigate()