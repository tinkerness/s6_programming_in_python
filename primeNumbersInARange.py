'''program to print all prime numbers within a range
'''

l=int(input("enter lower limit: "))
h=int(input("enter upper limit: "))

print("\nthe prime numbers between ", l, " and ", h, " are :")
for n in range(l,h+1):
    if n>1:
        for i in range(2,(n//2)+1):
            if (n%i) == 0:
                #print(n, "is not prime")
                break
        else :
            print(n, end=' ')

'''
Sample Output :-

enter lower limit: 1
enter upper limit: 10

the prime numbers between  1  and  10  are :
2 3 5 7
'''
