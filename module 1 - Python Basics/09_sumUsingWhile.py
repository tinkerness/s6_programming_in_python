'''sum of numbers from 1 to n using while loop'''

sum = 0
count = 1
number = int(input("enter the number : "))

while count <= number:
    sum += count
    count+=1
print(sum)