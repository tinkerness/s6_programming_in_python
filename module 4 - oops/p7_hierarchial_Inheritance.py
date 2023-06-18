class vehicle:
	def info(self):
		print('inside vehicle class')
class Car(vehicle):
	def car_info(self,name):
		print('car name:',name)
class Truck(vehicle):
	def truck_info(self,name):
		print('truck name : ',name)

car = Car()
car.info()
car.car_info('Bmw')

truck = Truck()
truck.info()
truck.truck_info('Tata')