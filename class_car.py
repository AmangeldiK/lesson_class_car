class Car:

    def __init__(self, make, model, year, odometer=0, fuel=70):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer
        self.fuel = fuel
        self.__add_distance
        self.__subtract_fuel


    def drive(self, km):
        self.km = km
        if self.km < self.fuel * 10:
            print('Let\'s drive!')    
        else: 
            print('Let\'s Need more fuel, please, fill more!')
    
    def __str__(self):
        return f'Brand: {self.make}, Model: {self.model}, Release: {self.year}, Odometer: {self.odometer + self.km}km, Subtract_fuel: {((self.fuel * 10) - self.km) / 10}liter'


    def __add_distance(self,km):
        self.km = km
        self.km + self.odometer
        return self.odometer
        

    def __subtract_fuel(self, km):
        self.km = km
        return self.km / 10

    
car1 = Car('Lexus', 'RX-400', 2011, fuel=70)
car1.drive(64)
print(car1)





    
        