#Person.py
#7.1
#Opret fil og definer person


class Person():
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
        
        def beskrivelse(self)
        print("%s is %d years old and is from %s." %(self.name, self.age, self.country))
    
#7.2
# I main.py

"""

from person import Person
"""

#oprettelse af tre objekter

person1 = Person("Nicolai", 21, "Danmark")

person2 = Person("Trump", 78, "USA")

person3 = Person("John", 36, "Danmark")

#opdater enskaberne

person1.age = 31

person2.name = "Anton"

person3.country = "Tyskland"

#7.3

print(person1.beskrivelse())
print(person2.beskrivelse())
print(person3.beskrivelse())

#7.4
    
class Person():
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
        
        def beskrivelse(self)
        print("%s is %d years old and is from %s." %(self.name, self.age, self.country))
    
    
person1 = Person("Nicolai", 21, "Danmark")

person2 = Person("Trump", 78, "USA")

 
    