'''nth power of a number'''

number = int(input("enter the number : "))
exp = int(input("enter the exponent : "))
product = 1

for eachPass in range(exp):
    product *= number
print(number,"^",exp," = ",product)