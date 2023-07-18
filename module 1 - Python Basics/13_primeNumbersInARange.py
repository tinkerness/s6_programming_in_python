'''Display Prime Numbers In A Range'''

low = int(input("enter lower range : "))
high = int(input("enter higher range : "))

print("prime numbers are :\n")
for n in range(low,high+1):
    if n>1:
        for f in range(2,(n//2)+1):
            if n%f == 0:
                break
        else:
            print(n,end=" ")