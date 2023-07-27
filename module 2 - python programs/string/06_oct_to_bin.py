oct = input("enter num : ")
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
print(bin)