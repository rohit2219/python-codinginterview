##classprog
## a simple class program with list comprehension example 
class pyclass(object):

	def __init__(self,passvar):
		self.__hiddenvariable=0
		self.testvar="hello"
	def  printfn (self,passvar):
		print (self.testvar)
		print (self.__hiddenvariable)
		print (passvar)
		list1=[1,2,3,4]
		list2=[3,4,5,9]
		y=[x*2 for x in list1]
		t=[k**k for k in list2]
		print (y)
		print(t)
		
class MyClass:
 
    # Hidden member of MyClass
    __hiddenVariable = 0
   
    # A member method that changes 
    # __hiddenVariable 
    def add(self, increment):
        self.__hiddenVariable += increment
        print (self.__hiddenVariable)
  
# Driver code
myObject = MyClass()     
myObject.add(2)
myObject.add(5)

py=pyclass("testprog")
py.printfn("testing start")

# singleton implementation
class OnlyOne:
    class __OnlyOne:
        def __init__(self, arg):
            self.val = arg
        def __str__(self):
            return repr(self) + self.val
    instance = None
    def __init__(self, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg
    def __getattr__(self, name):
        return getattr(self.instance, name)

x = OnlyOne('sausage')
print(x)