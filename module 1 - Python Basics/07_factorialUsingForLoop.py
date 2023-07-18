'''factorial of a number'''

number = int(input("enter number : "))
product = 1

for count in range(1,number+1):
    product *= count
print("factorial of ",number," = ",product)