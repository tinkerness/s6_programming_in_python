'''Python program to check if a string is palindrome
'''
word = input("enter the desired string : ")
word_copy = word.lower()
rev_word = word_copy[::-1]

if (rev_word == word_copy):
    print(word, "is a palindrome.")
else:
    print(word, "is not a palindrome.")

'''
sample output:-
enter the desired string : malayalam
malayalam is a palindrome.
'''