def salutation(name):
	salutation = 'Hello ' + name
	return salutation
	
def average(first, second):
	averageValue = (first  + second)/2.0
	return averageValue
	
print salutation('Alan')

print(average(5, 6))

print [1,2,3,]

print range(1,10)

mylist = [1,2,3,4,5]
mylistlength = len(mylist)
print mylistlength

print min(mylist)
print max(mylist)
print sum(mylist)
myaverage = sum(mylist)/float(len(mylist))
print myaverage
mylist = range(1,11)
print mylist
#first parameter to slice is index, 
#second parameter is element number
print mylist[5:10]

import random
random.shuffle(mylist)
print mylist

mylist1 = [1,2,3]
mylist2 = [4,5,6]
print mylist1 + mylist2
print 1 * mylist1
print 1 in mylist1
print 10 in mylist1
print 3 in mylist1
print 3 not in mylist1

print mylist1
mylist1.append(4)
print mylist1
mylist1.insert(1,50)
print mylist1
mylist1.remove(50)
print mylist1
mylist1.pop()
print mylist1

print mylist1.index(3)
print mylist1.count(3)
mylist1.reverse()
print mylist1
mylist1.sort()
print mylist1

from array import *
my_array = array('i', [1,2,3,4,5])
for i in my_array:
	print i
my_array.append(6)
my_array.append('Hi')
