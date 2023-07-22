name = "Alan Turing"
print("length = ",len(name))
# print(name[0])
# print(name[6])
# print(name[-1])
# print(name[-11])
# print(name[-len(name)])
# print()
for i in range(-1,-(len(name)+1),-1):
    print(i,name[i])