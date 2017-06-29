#student number: 10366826
#student name: alan kirwan

from test_calculator import Calculator

my_calc = Calculator()

for ch in "CALCULATOR".center(35):
    print ch,

print "\n\n","List of Operations:".rjust(45),"\n"

calclist = ['Add [1]','Subtract [2]','Multiply [3]','Divide [4]','Exponent [5]','Square [6]','Square Root [7]','Cube [8]','Sine [9]','Cosine [10]']
for op in calclist:
    print op.rjust(45)

opselect = raw_input("\nSelect Operation(1-10): ")

if opselect == "1":
    a = float(raw_input("Input First Operator: "))
    b = float(raw_input("Input Second Operator: "))
    print my_calc.add(a,b)

elif opselect == "2":
    a = float(raw_input("Input First Operator: "))
    b = float(raw_input("Input Second Operator: "))
    print my_calc.subtract(a,b)

elif opselect == "3":
    a = float(raw_input("Input First Operator: "))
    b = float(raw_input("Input Second Operator: "))
    print my_calc.multiply(a,b)

elif opselect == "4":
    a = float(raw_input("Input First Operator: "))
    b = float(raw_input("Input Second Operator: "))
    print my_calc.divide(a,b)

elif opselect == "5":
    a = float(raw_input("Input First Operator: "))
    b = float(raw_input("Input Second Operator: "))
    print my_calc.exponent(a,b)

elif opselect == "6":
    a = float(raw_input("Input Operator: "))
    print my_calc.square(a)

elif opselect == "7":
    a = float(raw_input("Input Operator: "))
    print my_calc.squareroot(a)

elif opselect == "8":
    a = float(raw_input("Input Operator: "))
    print my_calc.cube(a)

elif opselect == "9":
    a = raw_input("Input Degree of Angle: ")
    b = float(raw_input("Input Slope of Opposite: "))
    c = float(raw_input("Input Slope of Hypotenuse: "))
    print "sin",a,"deg =",my_calc.sine(b,c)

elif opselect == "10":
    a = raw_input("Input Degree of Angle: ")
    b = float(raw_input("Input Slope of Adjacent: "))
    c = float(raw_input("Input Slope of Hypotenuse: "))
    print "cos",a,"deg =",my_calc.cosine(b,c)

else:
    print "Invalid Input(select 1-10)"
