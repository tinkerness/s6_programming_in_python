''' python program to convert numbers to & from bin,oct,dec,hex '''
#binary to decimal
def binToDec():
    bin = input("enter binary number : ")
    l=len(bin)
    num=0

    for b in bin:
        l=l-1
        num = num + int(b)*2**l
    print("the decimal number is ", num)


#decimal to binary
def decToBin():
    num = int(input("enter decimal number : "))
    bin=""
    while num>0 :
        rem = num % 2
        num = num // 2
        bin = str(rem) + bin
    print("the binary num is ", bin)
    

#octal to binary
def octToBin():
    oct = input("enter octal number : ")
    bin=''
    
    for o in oct:
        if o=='0':
            bin = bin+'000'
        elif o=='1':
            bin = bin+'001'
        elif o=='2':
            bin = bin+'010'
        elif o=='3':
            bin = bin+'011'
        elif o=='4':
            bin = bin+'100'
        elif o=='5':
            bin = bin+'101'
        elif o=='6':
            bin = bin+'110'
        elif o=='7':
            bin = bin+'111'
    print("the binary number is ", bin)

#menu
print('Number Conversion')
print('bd : binToDec')
print('db : decToBin')
print('ob : octToBin')
#print('4. more')

op = str(input('\ninput the suitable option : '))
match op:
    case 'bd':
        binToDec()
    case 'db':
        decToBin()
    case 'ob':
        octToBin()
    case _:
        print("enter valid option !\n")
