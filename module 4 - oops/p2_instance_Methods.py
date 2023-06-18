# functions defined inside a class
# can only be called from an instance of that class

class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
	
    def speak(self, sound):
        return f"{self.name} says {sound}"

miles = Dog("Miles",4)
print(miles.description())
print(miles.speak("woof woof"))