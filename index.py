
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def revv(self):
        return "Vrrom vrooom vrooom!!!"

class Car(Vehicle):
    def revv(self):
        return "Vrrrrrrrooooooom!"
    pass

bmw = Car("BMW")
print(bmw.revv())
