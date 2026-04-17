class Vehicle:
    count = 0  # pole statyczne (klasy)

    def __init__(self, brand, model, year, mileage=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.__mileage = mileage  # pole prywatne
        Vehicle.count += 1  # inkrementacja licznika obiektów

    @property
    def mileage(self):
        return self.__mileage

    @mileage.setter
    def mileage(self, value):
        if value < self.__mileage:
            raise ValueError("Przebieg nie może zostać zmniejszony!")
        self.__mileage = value
 
    def drive(self, km):
        if km < 0:
            raise ValueError('Nie można jechać ujemną ilość km')
        self.__mileage += km

    def info(self):
        return f"{self.brand} {self.model} ({self.year}), przebieg: {self.__mileage} km"

    @staticmethod
    def get_count():
        return Vehicle.count

class Car(Vehicle):
    def __init__(self, brand, model, year, doors, mileage=0):
        super().__init__(brand, model, year, mileage)
        self.doors = doors

    def info(self):
        base = super().info()
        return f"{base}, drzwi: {self.doors}"


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, moto_type, mileage=0):
        super().__init__(brand, model, year, mileage)
        self.moto_type = moto_type

    def info(self):
        base = super().info()
        return f"{base}, typ motocykla: {self.moto_type}"


def show_vehicle(v):
    print(f'Informacje o pojeździe:\n{v.info()}')
    



car1 = Car('Toyota', 'Yaris', 2020, 5, 120000)
mot1 = Motorcycle('Yamaha', 'R1', 2026, 'ścigacz', 15)

mot1.drive(100)

print(car1.mileage)

car1.mileage = 123123

show_vehicle(car1)
show_vehicle(mot1)






















# # --- TEST ---
# car = Car("Toyota", "Corolla", 2018, 5, 120000)
# moto = Motorcycle("Yamaha", "MT-07", 2020, "sport", 15000)

# car.drive(150)
# # car._Vehicle__mileage = 0
# # car.__dict__["_Vehicle__mileage"] = 0
# moto.drive(40)


# show_vehicle(car)
# show_vehicle(moto)

# print("Liczba pojazdów:", Vehicle.get_count())




