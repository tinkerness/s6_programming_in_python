class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self,name,age):
        self.name=name
        self.age=age


# instantiate a new Dog object 

# Dog() #Dog.__init__() missing 2 required positional arguments: 'name' and 'age'
buddy = Dog("Buddy", 3)
miles = Dog("Miles",4)

# access instance attributes using dot notation
print(Dog.species)
print(buddy.name,buddy.age)
print(buddy.species)
print(miles.name,miles.age)
# values of the attributes can be changed dynamically
buddy.age  = 5
print(buddy.age)
miles.species = "Felis silvestris"
print(miles.species)