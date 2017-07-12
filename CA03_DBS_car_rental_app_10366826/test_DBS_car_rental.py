## student number: 10366826
## student name: Alan Kirwan

## importing testing library
import unittest

## creating the Dealership class along with the nested functions
class Dealership(object):

    def __init__(self):
        self.electric_cars = []
        self.petrol_cars = []
        self.diesel_cars = []
        self.hybrid_cars = []
        self.customer = []
## creating special lists for car types and
## additional list for customer account

## function created for setting the current stock levels
    def create_current_stock(self):
        for i in range(4):
           self.electric_cars.append(ElectricCar())
        for i in range(20):
           self.petrol_cars.append(PetrolCar())
        for i in range(8):
           self.diesel_cars.append(DieselCar())
        for i in range(8):
           self.hybrid_cars.append(HybridCar())

## function created for displaying up to date stock
## levels on the user-interface and customer account info
    def stock_count(self):
        print 'Petrol cars in stock: ' + str(len(self.petrol_cars))
        print 'Electric cars in stock: ' + str(len(self.electric_cars))
        print 'Diesel cars in stock: ' + str(len(self.diesel_cars))
        print 'Hybrid cars in stock: ' + str(len(self.hybrid_cars))
        print '\nCustomer Acc: ',self.customer,'vehicle(s) rented'


## function created for registering a new car
## rental and notifying the user
    def rent(self, car_list, amount):
        if len(car_list) < amount:
            print "\nI'm sorry! I'm afraid we don't have that many cars available!\nCheck what's currently available below:\n"
            return
        elif len(car_list) >= amount:
            print "\nSUCCESS! Your vehicle(s) have been reserved and are waiting for you with a full tank of gas!\n"
        total = 0
        while total < amount:
           car_list.pop()
           total = total + 1
        self.customer.append(amount)

## function created for navigating the user to
## the returns section in the user-interface
    def returncar(self, amount):
        carlist = ['Petrol [1]','Diesel [2]','Electric [3]','Hybrid [4]']
        for op in carlist:
            print op.rjust(38)
        ans = raw_input('Select the car type you wish to return from the list above [1-4]: ')
        if ans == '1':
            self.newreturn(self.petrol_cars, amount)
        elif ans == '2':
            self.newreturn(self.diesel_cars, amount)
        elif ans == '3':
            self.newreturn(self.electric_cars, amount)
        elif ans == '4':
            self.newreturn(self.hybrid_cars, amount)
        elif amount != int:
            print "Invalid Input"
        else:
            print "Invalid Input"

## function created for the processing of the
## return along with updating the customer account info
    def newreturn(self, car_list, amount):
        if self.customer >= amount:
            print "\nYou have returned ",amount," vehicles out of",self.customer,"\n"
        else:
            return ValueError
        total = 0
        while total < amount:
           car_list.append(amount)
           total = total + 1
        self.customer.append(-amount)

## function created for navigating the user
## to make a new rental in the interface
    def process_rental(self):
        answer = raw_input('\n\nLooking to Rent or Return a car? y/n ')
        if answer == 'y':
            if len(self.electric_cars)+len(self.diesel_cars)+len(self.hybrid_cars)+len(self.petrol_cars) == 0:
                print "\nSorry nothing to rent, please try again.\n"
            answer = raw_input('Select a car type from the list above [1-4], or select [5] for Returns: ')
        elif answer != 'y':
            return ValueError('\nINVALID INPUT - Please Try Again...\n')
        try:
            amount = int(raw_input('How many vehicles do you need (or wish to return)? '))
        except:
            print ValueError('\nINVALID INPUT - Please Try Again...\n')
        try:
            if answer == '1':
                self.rent(self.petrol_cars, amount)
            elif answer == '2':
                self.rent(self.diesel_cars, amount)
            elif answer == '3':
                self.rent(self.electric_cars, amount)
            elif answer == '4':
                self.rent(self.hybrid_cars, amount)
            elif answer == '5':
                self.returncar(amount)
            else:
                print ValueError('\nINVALID INPUT - Please Try Again...\n')
        except:
            return ValueError('\nINVALID INPUT - Please Try Again...\n')
        self.stock_count()

# Define a class for my car

class Car(object):
    # implement the car object.

    def __init__(self):
        self.__colour = ''
        self.__make = ''
        self.__mileage = 0
        self.engineSize = ''

    def getColour(self):
        return self.__colour

    def getMake(self):
        return self.__make

    def getMileage(self):
        return self.__mileage

    def setColour(self, colour):
        self.__colour = colour

    def setMake(self, make):
        self.__make = make

    def setMileage(self, mileage):
        self.__mileage = mileage

    def paint(self, colour):
        self.__colour = colour
        return self.__colour

    def move(self, distance):
        self.__mileage = self.__mileage + distance
        return self.__mileage


## function for setting and retrieving value for
## number of fuel cells for the electric car class
class ElectricCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1

    def getNumberFuelCells(self):
        return self.__numberFuelCells

    def setNumberFuelCells(self, value):
        self.__numberFuelCells = value

## function for setting and retrieving value for
## number of fuel cells for the petrol car class
class PetrolCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberCylinders = 1

    def getNumberCylinders(self):
        return self.__numberCylinders

    def setNumberCylinders(self, value):
        self.__numberCylinders = value

## function for setting and retrieving value for
## number of fuel cells for the diesel car class
class DieselCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberCylinders = 1

    def getNumberCylinders(self):
        return self.__numberCylinders

    def setNumberCylinders(self, value):
        self.__numberCylinders = value

## function for setting and retrieving value for
## number of fuel cells for the hybrid car class
class HybridCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberCylinders = 1

    def getNumberCylinders(self):
        return self.__numberCylinders

    def setNumberCylinders(self, value):
        self.__numberCylinders = value


class TestDealership(unittest.TestCase):

    def setUp(self):
        self.deal = Dealership()

	## testing the Dealership functionality
    def test_create_current_stock(self):
        self.assertFalse(self.deal.create_current_stock())

    def test_stock_count(self):
        self.assertFalse(self.deal.stock_count())

    def test_rent(self):
        self.assertEqual(None,self.deal.rent("1","10"))

    def test_returncar(self):
        self.assertEqual(None,self.deal.returncar(str))

    def test_newreturn(self):
        self.assertEqual(ValueError,self.deal.newreturn(str,str))

    def test_process_rental(self):
        self.assertTrue(self.deal.process_rental())
        self.assertRaises(self.deal.process_rental())


class TestElectricCar(unittest.TestCase):

    def setUp(self):
        self.elec = ElectricCar()

	## testing the ElectricCar functionality
    def test_getNumberFuelCells(self):
        self.assertTrue(self.elec.getNumberFuelCells())

    def test_setNumberFuelCells(self):
        self.assertFalse(self.elec.setNumberFuelCells(1))

class TestPetrolCar(unittest.TestCase):

    def setUp(self):
        self.petr = PetrolCar()

	## testing the PetrolCar functionality
    def test_getNumberCylinders(self):
        self.assertTrue(self.petr.getNumberCylinders())

    def test_setNumberCylinders(self):
        self.assertFalse(self.petr.setNumberCylinders(1))

class TestDieselCar(unittest.TestCase):

    def setUp(self):
        self.dies = DieselCar()

	## testing the DieselCar functionality
    def test_getNumberFuelCells(self):
        self.assertTrue(self.dies.getNumberCylinders())

    def test_setNumberFuelCells(self):
        self.assertFalse(self.dies.setNumberCylinders(1))

class TestHybridCar(unittest.TestCase):

    def setUp(self):
        self.hybr = HybridCar()

	# testing the HybridCar functionality
    def test_getNumberFuelCells(self):
        self.assertTrue(self.hybr.getNumberCylinders())

    def test_setNumberFuelCells(self):
        self.assertFalse(self.hybr.setNumberCylinders(1))


## testing the car class functionality
class TestCar(unittest.TestCase):

    def test_car_mileage(self):
        self.car = Car()
        self.assertEqual(0, self.car.getMileage())
        self.car.move(15)
        self.assertEqual(15, self.car.getMileage())
        self.car.setMileage(45)
        self.assertEqual(45, self.car.getMileage())

    def test_car_make(self):
        self.car = Car()
        self.assertEqual('', self.car.getMake())
        self.car.setMake('Ferrari')
        self.assertEqual('Ferrari', self.car.getMake())

    def test_car_colour(self):
        self.car = Car()
        self.assertEqual('', self.car.getColour())
        self.car.paint('red')
        self.assertEqual('red', self.car.getColour())
        self.car.setColour('yellow')
        self.assertEqual('yellow', self.car.getColour())

    def test_car_engine_size(self):
        self.car = Car()
        self.assertEqual('', self.car.engineSize)
        self.car.engineSize = '2.0tdi'
        self.assertEqual('2.0tdi', self.car.engineSize)

    def test_electric_car_fuel_cells(self):
		electric_car = ElectricCar()
		self.assertEqual(1, electric_car.getNumberFuelCells())
		electric_car.setNumberFuelCells(4)
		self.assertEqual(4, electric_car.getNumberFuelCells())

if __name__ == '__main__':
    unittest.main()
