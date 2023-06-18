# Base class
class vehicle:
	def vehicle_info(self):
		print('inside vehicle class')
# Child class
class Car(vehicle):
	def car_info(self):
		print('inside car class')
car = Car()
car.vehicle_info()
car.car_info()