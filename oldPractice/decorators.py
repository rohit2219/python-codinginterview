'''
decorator are basically  functions which alter the behaviour/wrap the origonal functions and use the original functions
output to add other behavious to it
'''
def add20ToaddFn(inp):
    def addval(a,b):
        return inp(a,b) + 20
    addval.unwrap=inp # this is how you unwrap
    return addval

@add20ToaddFn
def addFn(x,y):
    return x+y

d = {}
def decorFn(addFn):
    def decorInnerFn(a,b):
        if (a,b) in d:
            print('return from cache')
            return d((a,b))
        else:
            print('return from fn')
            d[(a,b)]= addFn(a,b)
            return addFn(a,b)
    return decorInnerFn

@decorFn
def add(x,y):
    return x+y
print(add(7,2))
#print(addFn(2,3),addFn.unwrap(2,3))

#generators
def numberGen(x):
    for i in range(x):
        yield  i

for i in numberGen(5):
    print(i)

file="./data.txt"
try:
    fileObj=open(file,'r')
except FileNotFoundError:
    print('File not found')
else:
    i=file.readline()
    print(i)
    fileObj.close()
finally:
    print('The above set of statemnets done with/without erro')