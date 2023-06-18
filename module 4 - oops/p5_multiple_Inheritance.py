# Parent class 1
class Person:
	def person_info(self,name,age):
		print('inside person class')
		print('Name : ',name,'Age : ',age)
# Parent class 2
class Company:
	def company_info(self,company_name,location):
		print('inside company class')
		print('Name : ',company_name,'Location : ',location)
# Child class
class Employee(Person,Company):
	def employee_info(self,salary,skill):
		print('inside employee class')
		print('Salary : ',salary,'skill : ',skill)

emp = Employee()
emp.person_info('Jessa',28)
emp.company_info('Google','Atlanta')
emp.employee_info(120001,'Machine Learning')