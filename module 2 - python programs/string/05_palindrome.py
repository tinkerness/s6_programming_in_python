'''Write a Python code to determine whether the given string is a Palindrome or not using slicing. Do not use any string function'''

string = input("Enter a string: ")

# Remove any spaces and convert the string to lowercase
string = string.replace(" ", "").lower()
if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")