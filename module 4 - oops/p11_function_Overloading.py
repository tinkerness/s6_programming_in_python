# Python does not support function overloading 

# class sumClass:
#     def sum(self, a, b):
#         print("First method:",a+b)
#     def sum(self, a, b, c):
#         print("Second method:", a + b + c)
        
# obj=sumClass()
# obj.sum(19, 8, 77) #correct output
# obj.sum(18, 20) #throws error

class SumClass:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("Function with three arguments")
            print("Sum=", a+b+c)
        elif a!=None and b!=None:
            print("Function with two arguments")
            print("Sum=",a+b)
        else:
            print("Provide more numbers")
obj = SumClass()
obj.sum(19, 8, 77)
obj.sum(18, 20) 
