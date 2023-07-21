'''
program to print the pattern:-
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5
'''
num = 1
for i in range (5,0,-1):
    for j in range (1,i+1):
        print(num, end=' ')
    print('')
    num += 1