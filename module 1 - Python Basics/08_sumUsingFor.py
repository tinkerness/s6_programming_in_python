'''sum of numbers from 1 to n using for loop'''

sum = 0
number = int(input("enter the number : "))

for count in range(1,number+1):
    sum += count
print(sum)