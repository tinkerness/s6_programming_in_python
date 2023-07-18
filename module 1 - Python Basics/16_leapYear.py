'''Write a Python code to check whether a given year is a leap year or not [An year is a leap year if it's divisible by 4 but not divisible by 100 except for those divisible by 400]'''

year = int(input("Enter the year : "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year,"is a leap year.")
else:
    print(year, "is not a leap year.")