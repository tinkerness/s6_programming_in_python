# # Python code to illustrate working of try()
def divide(x, y):
	try:
		result = x // y
		print("Yes! Your answer is :", result)
	except ZeroDivisionError:
		print("Sorry! You are dividing by zero ")
	except Exception as e:
			print("The error is: ",e)

divide(3, 2)
# Yes! Your answer is : 1
divide(3, 0)
# Sorry! You are dividing by zero 
divide(3, "2")
# The error is:  unsupported operand type(s) for //: 'int' and 'str'