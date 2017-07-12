## student number: 10366826
## student name: Alan Kirwan

from test_DBS_car_rental import Dealership

print "\n"
for ch in "WELCOME TO DBS CAR RENTAL".center(35):
    print ch,

print "\n\n","Ireland's No.1 Car Rental Company!".center(65),"\n"
print "\n\n","We specialise in the following car types:".center(65),"\n"

carlist = ['Petrol [1]','Diesel [2]','Electric [3]','Hybrid [4]']
for op in carlist:
    print op.rjust(38)

dealership = Dealership()
dealership.create_current_stock()
proceed = 'y'
while proceed == 'y':
    dealership.process_rental()
    proceed = raw_input('\nAnything else we can help you with today? y/n ')
