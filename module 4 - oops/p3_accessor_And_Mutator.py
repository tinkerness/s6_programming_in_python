class Dog:
    def __init__(self, name):
        self.__name = name

	# Defining Mutator Method
    def set_name(self, name):
        self.__name = name
	# Defining Accessor Method
    def get_name(self):
        return self.__name
        
myDog = Dog('Jackie')
# Access the value using Accessor method
print (myDog.get_name())
# Modify the value using Mutator method
myDog.set_name('Bruno')
print (myDog.get_name())