'''Basic Data Types in Python'''

# integers - dec,bin,oct,hex
print("Number \t equals \t interpretation \t type")
print("10   \t",10," \t\t dec \t\t\t ",type(10))
print("0b10 \t",0b10," \t\t bin \t\t\t ",type(0b10))
print("0o10 \t",0o10," \t\t oct \t\t\t ",type(0o10))
print("0x10 \t",0x10," \t\t hex \t\t\t ",type(0x10))

# floating point numbers - decimal point, e followed by +/- number
print("\nNumber \t equals \t\t type")
print("4.2   \t",4.2," \t\t\t",type(4.2))
print("4.   \t",4.," \t\t\t",type(4.))
print(".2   \t",.2," \t\t\t",type(.2))
print(".4e7   \t",.4e7," \t",type(.4e7))
print(".42e-2   \t",.42e-2," \t",type(.42e-2))

# complex numbers - ai+bj
print("\nNumber \t equals \t type")
print("4+2j   \t",4+2j," \t",type(4+2j))

# strings
print("\nstring \t type")
print("'hii' \t",type('hii'))
print('"hii" \t',type("hii"))

# boolean
print("\nvalue \t type")
print("True \t",type(True))
print("False \t",type(False))