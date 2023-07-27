bin = input("enter binary num : ")
l=len(bin)
num=0

for b in bin:
    l=l-1
    num = num + int(b)*2**l
print(num)