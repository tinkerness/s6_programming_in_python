'''
Program to display the Fibonacci sequence
'''
n=int(input("enter number of terms required : "))

n1,n2 = 0,1

if n <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(n1, end=' ')
        n3=n1+n2
        n1=n2
        n2=n3
    
