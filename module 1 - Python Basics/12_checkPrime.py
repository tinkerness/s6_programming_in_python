'''check whether given number is prime'''

n = int(input("enter the number : "))

if n>1:
    for f in range(2,(n//2)+1):
        if n%f == 0:
            print(n,"is not prime")
            break
    else:
        print(n,"is prime")
else:
    print(n,"is not prime")