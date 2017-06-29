#define my car class
class Car(object):

	def __init__(self):
		self.__make = "Ferrari"
		self.__colour = "Red"
		self.__mileage = 10
		self.enginesize = "5.4l"
	
	def getcolour(self):
		return self.__colour
	
	def getMake(self):
		return self.__make
	
	def getmileage(self):
		return self.__mileage
	
	def setmake(self, make):
		self.__make = make
		
	def setcolour(self, colour):
		self.__colour = colour
		
	def setmileage(self, mileage):
		self.__mileage = mileage
		
	def move(self, distance):
		print('Moved ' + str(distance) + "kms. ")
		self.__mileage = self.__mileage + distance
		
	def paint(self, colour):
		print("Getting a paint job - new colour is: " + colour)
		self.__colour = colour
		
class ElectricCar(Car):
	def __init__(self):
		Car.__init__(self)
		self.__numberfuelcells = 1
		
	def getnumberfuelcells(self):
		return self.__numberfuelcells
		
	def setnumberfuelcells(self,value):
		self.__numberfuelcells = value
	
	
my_car = Car()
#Engine size is public and will be printed
print my_car.enginesize

print my_car.getMake()
print my_car.getcolour()
print my_car.getmileage()

my_car.enginesize = "5.4l"
print my_car.enginesize

my_car.setmake("BMW")
print my_car.getMake()

my_car.setmileage(100)

my_car.move(10)
print my_car.getmileage()
my_car.paint("Blue")
print my_car.getcolour()


#Make is private and will cause an error when run
#print my_car.__make