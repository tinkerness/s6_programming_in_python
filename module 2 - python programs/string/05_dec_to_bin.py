num = 7
bin=""
while num>0 :
    rem = num % 2
    num = num // 2
    bin = str(rem) + bin
print("binary num = ", bin)