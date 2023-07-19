'''
program to print the pattern:-
A
A B
A B C
A B C D
A B C D E
'''

value = 5

for i in range (65,64+value+1):
    for j in range (65,i+1):
        print(chr(j), end=' ')
    print('')

# # else -
# l = ord('A')
# for i in range (l,l-1+value+1):
#     for j in range (l,i+1):
#         print(chr(j), end=' ')
#     print('')