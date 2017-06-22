from oop import Car,ElectricCar

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

electric_car = ElectricCar()
print electric_car.getnumberfuelcells()

electric_car.move(20)
print electric_car.getmileage()
		
