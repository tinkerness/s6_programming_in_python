'''Write a Python program to reverse a number and also find the sum of digits of the number. Prompt the user for input'''

number = int(input("Enter a number: "))
num = number
sum,rev = 0,0

while num>0:
    sum += num%10
    rev = rev*10 + num%10
    num //= 10
print("the reverse of ",number," is ",rev)
print("the sum of digits of ",number," is ",sum)