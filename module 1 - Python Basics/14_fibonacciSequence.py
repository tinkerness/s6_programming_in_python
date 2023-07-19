'''fibonacci sequence upto n'''

n = int(input("enter number of terms required : "))
n1,n2 = 0,1

if n<=0:
    print("enter positive integer")
else:
    print("fibonacci sequence :\n")
    for count in range(n):
        print(n1,end=" ")
        n3 = n1+n2
        n1=n2
        n2=n3