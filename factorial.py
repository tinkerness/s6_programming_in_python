# simple program to find factorial of a number

limit = int(input("enter num: "))
p = 1
for i in range(1, limit + 1):
    p = p * i
print(p)
