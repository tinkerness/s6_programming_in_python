''' Function to find lcm of two numbers

formula for lcm :-
    a*b = lcm(a,b) * gcd(a,b)
    lcm(a,b) = a*b // gcd(a,b)
'''

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b):
    return (a*b//gcd(a,b))

n1 = int(input("enter num1 : "))
n2 = int(input("enter num2 : "))
print(f"The lcm of {n1} and {n2} is {lcm(n1,n2)}")