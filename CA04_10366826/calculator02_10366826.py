## student number: 10366826
## student name: alan kirwan

## "You will need to use lambda, map, filter, reduce and
##  list comprehension in any manner you deem necessary to achieve this."

## I only deemed Map necessary to achieve the aim
## of modifying the calculator to handle lists in conjunction with an
## infinite "while true" loop to take in lists of numbers from the user.
## You can see the first instance of where/how I used the map functionality
## at line 55

## Calling the calculator class from the test_calculator file
from test_calculator02_10366826 import Calculator

## Assigning the calculator class to a variable
my_calc = Calculator()

## Designing and formatting the user interface
print "\n"
for ch in "CALCULATOR".center(35):
    print ch,
print "\n","[v2:List Edition]".rjust(44)

print "\n\n","List of Operations:".rjust(45),"\n"

calclist = ['Add [1]','Subtract [2]','Multiply [3]','Divide [4]','Exponent [5]','Square [6]','Square Root [7]','Cube [8]','Sine [9]','Cosine [10]']
for op in calclist:
    print op.rjust(45)

opselect = raw_input("\nSelect Operation(1-10): ")
print "\n"

## If user selects addition
if opselect == "1":
    numsA = []
    i = 0
    while 1:
        i += 1
        numA = raw_input("[1]Input number %d (press Enter twice when finished):"%i)
        if numA == "":
            break
        numsA.append(float(numA))
    print "\n1st sequence: ",numsA,"\n"

    numsB = []
    i = 0
    while 1:
        i += 1
        numB = raw_input("[2]Input number %d (press Enter twice when finished):"%i)
        if numB == "":
            break
        numsB.append(float(numB))
    print "\n2nd sequence: ",numsB,"\n"
    print map(my_calc.add,numsA,numsB),"\n"

## If user selects subtraction
elif opselect == "2":
    numsA = []
    i = 0
    while 1:
        i += 1
        numA = raw_input("[1]Input number %d (press Enter twice when finished):"%i)
        if numA == "":
            break
        numsA.append(float(numA))
    print "\n1st sequence: ",numsA,"\n"

    numsB = []
    i = 0
    while 1:
        i += 1
        numB = raw_input("[2]Input number %d (press Enter twice when finished):"%i)
        if numB == "":
            break
        numsB.append(float(numB))
    print "\n2nd sequence: ",numsB,"\n"
    print map(my_calc.subtract,numsA,numsB),"\n"

## If user selects multiplication
elif opselect == "3":
    numsA = []
    i = 0
    while 1:
        i += 1
        numA = raw_input("[1]Input number %d (press Enter twice when finished):"%i)
        if numA == "":
            break
        numsA.append(float(numA))
    print "\n1st sequence: ",numsA,"\n"

    numsB = []
    i = 0
    while 1:
        i += 1
        numB = raw_input("[2]Input number %d (press Enter twice when finished):"%i)
        if numB == "":
            break
        numsB.append(float(numB))
    print "\n2nd sequence: ",numsB,"\n"
    print map(my_calc.multiply,numsA,numsB),"\n"

## If user selects division
elif opselect == "4":
    numsA = []
    i = 0
    while 1:
        i += 1
        numA = raw_input("[1]Input number %d (press Enter twice when finished):"%i)
        if numA == "":
            break
        numsA.append(float(numA))
    print "\n1st sequence: ",numsA,"\n"

    numsB = []
    i = 0
    while 1:
        i += 1
        numB = raw_input("[2]Input number %d (press Enter twice when finished):"%i)
        if numB == "":
            break
        numsB.append(float(numB))
    print "\n2nd sequence: ",numsB,"\n"
    print map(my_calc.divide,numsA,numsB),"\n"

## If user selects exponent
elif opselect == "5":
    numsA = []
    i = 0
    while 1:
        i += 1
        numA = raw_input("[1]Input number %d (press Enter twice when finished):"%i)
        if numA == "":
            break
        numsA.append(float(numA))
    print "\n1st sequence: ",numsA,"\n"

    numsB = []
    i = 0
    while 1:
        i += 1
        numB = raw_input("[2]Input number %d (press Enter twice when finished):"%i)
        if numB == "":
            break
        numsB.append(float(numB))
    print "\n2nd sequence: ",numsB,"\n"
    print map(my_calc.exponent,numsA,numsB),"\n"

## If user selects square
elif opselect == "6":
    numsA = []
    i = 0
    while 1:
        i += 1
        numA = raw_input("[1]Input number %d (press Enter twice when finished):"%i)
        if numA == "":
            break
        numsA.append(float(numA))
    print "\n1st sequence: ",numsA,"\n"
    print map(my_calc.square,numsA),"\n"

## If user selects squareroot
elif opselect == "7":
    numsA = []
    i = 0
    while 1:
        i += 1
        numA = raw_input("[1]Input number %d (press Enter twice when finished):"%i)
        if numA == "":
            break
        numsA.append(float(numA))
    print "\n1st sequence: ",numsA,"\n"
    print map(my_calc.squareroot,numsA),"\n"

## If user selects cube
elif opselect == "8":
    numsA = []
    i = 0
    while 1:
        i += 1
        numA = raw_input("[1]Input number %d (press Enter twice when finished):"%i)
        if numA == "":
            break
        numsA.append(float(numA))
    print "\n1st sequence: ",numsA,"\n"
    print map(my_calc.cube,numsA),"\n"

## If user selects sine
elif opselect == "9":
    Angles = []
    i = 0
    while 1:
        i += 1
        Ang = raw_input("Input Degree of Angle no.%d (press Enter twice when finished): "%i)
        if Ang == "":
            break
        Angles.append(float(Ang))
    print "\nAngles to be calculated: \n",Angles,"\n"

    numsA = []
    i = 0
    while 1:
        i += 1
        numA = raw_input("[1]Input Opposite Slope no.%d (press Enter twice when finished): "%i)
        if numA == "":
            break
        numsA.append(float(numA))
    print "\n1st sequence of opposite slopes: \n",numsA,"\n"

    numsB = []
    i = 0
    while 1:
        i += 1
        numB = raw_input("[2]Input Hypotenuse Slope no.%d (press Enter twice when finished): "%i)
        if numB == "":
            break
        numsB.append(float(numB))
    print "\n2nd sequence of hypotenuse slopes: \n",numsB,"\n"
    print "sin",Angles,"\ndeg =",map(my_calc.sine,numsA,numsB),"\n"

## If user selects cosine
elif opselect == "10":
    Angles = []
    i = 0
    while 1:
        i += 1
        Ang = raw_input("Input Degree of Angle no.%d (press Enter twice when finished): "%i)
        if Ang == "":
            break
        Angles.append(float(Ang))
    print "\nAngles to be calculated: \n",Angles,"\n"

    numsA = []
    i = 0
    while 1:
        i += 1
        numA = raw_input("[1]Input Adjacent Slope no.%d (press Enter again when finished): "%i)
        if numA == "":
            break
        numsA.append(float(numA))
    print "\n1st sequence of adjacent slopes: \n",numsA,"\n"

    numsB = []
    i = 0
    while 1:
        i += 1
        numB = raw_input("[2]Input Hypotenuse Slope no.%d (press Enter again when finished): "%i)
        if numB == "":
            break
        numsB.append(float(numB))
    print "\n2nd sequence of hypotenuse slopes: \n",numsB,"\n"
    print "cos",Angles,"\ndeg =",map(my_calc.cosine,numsA,numsB),"\n"

## Error handling in case user selects an invalid operation number
else:
    print "Invalid Input(select 1-10)"
