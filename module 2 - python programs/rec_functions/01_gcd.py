''' Function to find gcd of two numbers'''

def gcd(a,b):
    # a = max(n1,n2)   # not necessary
    # b = min(n1,n2)
    
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

n1 = int(input("enter num1 : "))
n2 = int(input("enter num2 : "))
print(f"The gcd of {n1} and {n2} is {gcd(n1,n2)}")