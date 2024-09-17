class Vehicle:

    def __init__(self, make, model, year, price):
        self.make=make
        self.model=model
        self.year=year
        self.price=price
    
    def display_info(self):
        print(f"make: {self.make}  model: {self.model} year: {self.year}  price: {self.price}")

car=Vehicle("aaa", "bbb", "2024", "1000")
car.display_info()