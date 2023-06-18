# Base class
class Person:
	def person_info(self):
		print('inside person class')
# Child class
class Employee(Person):
	def employee_info(self):
		print('inside employee class')
# Child class of Child class
class Emp2(Employee):
	def emp2_info(self):
		print('inside emp2 class')

emp = Emp2()
emp.person_info()
emp.employee_info()
emp.emp2_info()