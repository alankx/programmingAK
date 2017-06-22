# define functions
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def exponent(x,y):
    return x**y

def square(x):
    return x**2.0

def squareroot(x):
    return x**0.5

def cube(x):
    return x**3.0
	
def sine(x,y,z):
	return x,y/z
	
def cosine(x,y,z):
	return x,y/z


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
    print add(a,b)

elif opselect == "2":
    a = float(raw_input("Input First Operator: "))
    b = float(raw_input("Input Second Operator: "))
    print subtract(a,b)

elif opselect == "3":
    a = float(raw_input("Input First Operator: "))
    b = float(raw_input("Input Second Operator: "))
    print multiply(a,b)

elif opselect == "4":
    a = float(raw_input("Input First Operator: "))
    b = float(raw_input("Input Second Operator: "))
    print divide(a,b)

elif opselect == "5":
    a = float(raw_input("Input First Operator: "))
    b = float(raw_input("Input Second Operator: "))
    print multiply(a,b)

elif opselect == "6":
    a = float(raw_input("Input Operator: "))
    print square(a)

elif opselect == "7":
    a = float(raw_input("Input Operator: "))
    print squareroot(a)

elif opselect == "8":
    a = float(raw_input("Input Operator: "))
    print cube(a)
	
elif opselect == "9":
	a = raw_input("Input Angle: ")
	b = float(raw_input("Input Opposite Slope: "))
	c = float(raw_input("Input Hypotenuse Slope: "))
	print sine(a,b,c)

elif opselect == "10":
	a = raw_input("Input Angle: ")
	b = float(raw_input("Input Adjacent Slope: "))
	c = float(raw_input("Input Hypotenuse Slope: "))
	print cosine(a,b,c)
