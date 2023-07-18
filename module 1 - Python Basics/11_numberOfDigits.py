'''count number of digits in a number'''

number = 123060
count = 0

while (number > 0):
    number //=10
    count +=1
print("number of digits = ",count)