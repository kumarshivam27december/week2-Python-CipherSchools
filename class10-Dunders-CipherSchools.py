class Person:
    def  __init__(self,name):
        self.name=name
        
    def say_hi(self):
        print('hello, my name is ',self.name)
        
p=Person("Shivam or  loveu or saurav or or or ......")
p.say_hi()




class A:
    def __init__(self):
        print(self)
        print('initialized')
        
    def __del__(self):
        print(self)
        print("I am genious and i am not dying for you")    
a=A()




del a 
a=1
print(type(a))
print(a+5)
print(a.__add__(5))
print("shivam kumar or loveu singh or sourav kumar mahto or " * 20)
print("shivam or saurav or loveu or ".__mul__(20))


# class Person:
#     name="shivam or loveu or saurav"
#     def __add__(self,a):
        
class B:
    a=1
    b=2
    def __add__(self,x):
        return a+b+x
            
        
