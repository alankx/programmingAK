import operator

class Person:
    races = ['caucasoid', 'negroid', 'mongoloid']

    def __init__(self, name, race):
        self.name = name
        self.arms = ['left', 'right']
        self.legs = ['left', 'right']
        self.tears = []
        if (race in Person.races):
            self.race = race

    def amputate(self, arm):
        self.arms.remove(arm)

    def tear_meniscus(self, leg):
        self.tears.append(leg)

    def write(self, file):
        file.write(str(self))
    
    def __str__(self):
        return '%s,%s,%s,%s,%s\n' % (self.name,self.legs,self.arms,self.tears,self.race)
    
races = ['caucasoid', 'negroid', 'mongoloid']

gaurav = Person('Gaurav', 'caucasoid')
print gaurav.arms

ruggiero = Person('Ruggiero', 'caucasoid')
print ruggiero.arms

gaurav.amputate('left')
print gaurav.arms

print ruggiero.arms

ruggiero.tear_meniscus('left knee')
print ruggiero.tears

print gaurav.tears

people_file = open('people.csv', 'w')
people_file.write('name,legs,arms,tears,race\n')
gaurav.write(people_file)
ruggiero.write(people_file)
people_file.close()

people = []#[gaurav, ruggiero]
people.append(gaurav)
people.append(ruggiero)

for person in people:
	print str(person)

	
gaurav = {'name': 'Gaurav', 'race': 'causasian',
		'arms': ['left', 'right'], 'legs': ['left', 'right'], 'tears': []}
print gaurav['arms']

ruggiero = {'name': 'Ruggiero', 'race': 'causasian',
		'arms': ['left', 'right'], 'legs': ['left', 'right'], 'tears': []}
print ruggiero['arms']

gaurav['arms'].remove('left')
print gaurav['arms']

print ruggiero['arms']

ruggiero['tears'].append('left knee')
print ruggiero['tears']

print gaurav['tears']

people = []#[gaurav, ruggiero]
people.append(gaurav)
people.append(ruggiero)

for person in people:
	print str(person)

newlist = sorted(people, key=lambda k: k['name'], reverse=True)
print newlist
