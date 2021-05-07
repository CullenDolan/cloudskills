class Cars():
    # assigns values to object propertires
    def __init__(self,  make, model, year):
        self.make = make # defining the value does not allow anything to be passed in for this value
        self.model = model
        self.year = year
    

    def print_model(self):
        print(self.model)
    

    def print_year(self):
        print(self.year)


    def print_make_and_year(self):
        print(self.make)
        print(self.year)


my_cars = Cars("Rivian","R1T", 2021)
my_cars.print_model()
my_cars.print_make_and_year()
