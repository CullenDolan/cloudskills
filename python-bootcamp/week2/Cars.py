class Cars():
    def __init__(self, model, make, year):
        self.model = model
        self.make = make
        self.year = year
    

    def print_model(self):
        print(self.model)
    

    def print_year(self):
        print(self.year)


    def print_make_and_year(self):
        print(self.make)
        print(self.year)


my_cars = Cars("Rivian", "R1T", 2021)
my_cars.print_model()
my_cars.print_year()
my_cars.print_make_and_year()