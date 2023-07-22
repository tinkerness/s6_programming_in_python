''' Function to find lcm of two numbers

formula for lcm :-
    a=large,b=small
    if large%small == 0, return large
    else return large+a
'''

def lcm(a,b,large):
    # print(f"a={a},b={b},large={large}")
    if large%b == 0:
        return large
    return lcm(a,b,large+a)

n1 = int(input("enter num1 : "))
n2 = int(input("enter num2 : "))
large = max(n1,n2)
small = min(n1,n2)

print(f"The lcm of {n1} and {n2} is {lcm(large,small,large)}")
    