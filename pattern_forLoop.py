'''
program to print the pattern:-
1

1 2

1 2 3

1 2 3 4
'''

for i in range (1,5):
    #print("\ni = ", i)
    for j in range (1,i+1):
        print(j, end=' ')
    print('\n')
