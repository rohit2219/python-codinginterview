
class fiboClass:
    def __init__(self):
        self.fiboList = []
        self.fiboDict = {0:0, 1:1}
        self.fiboNumDict = {0:0, 1:1}
        ### below are all counts to show how many times recursion has happened.
        self.retcount = 0
        self.notrecount = 0
        self.loopcount = 0
        self.fibooldcnt = 0
        self.fibodyncnt = 0
    def fibo( self, n):
        ### LOGIC USING Memoization
            self.loopcount = self.loopcount + 1
            if n in self.fiboDict:
                print("returning at found:",n)
                self.retcount = self.retcount + 1
                return self.fiboDict[n]
            else:
                self.fiboDict[n] = self.fibo(n - 2) + self.fibo(n - 1)
                self.notrecount = self.notrecount + 1
                return self.fiboDict[n]
    def fiboold(self,n):
        ## USING RECURSION - normal
        self.fibooldcnt = self.fibooldcnt + 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fiboold(n -1 ) + self.fiboold(n -2 )
    def fibodynamic(self,n):
        ## Dynamic programming
        first = self.fiboNumDict[0]
        second = self.fiboNumDict[1]
        fiboSum = 0
        for i in range(n-1):
            self.fibodyncnt = self.fibodyncnt + 1
            fiboNum = first + second
            fiboSum = fiboSum + fiboNum
            first = second
            second = fiboNum
        return fiboNum

obj = fiboClass()

x=obj.fibo(10)

print ("##RECURSION - simple to write and understand, high time complexity , less space complexity##")
print (obj.fiboold(10))
print (obj.fibooldcnt)
print ("##MEMOIZATION, simple to write, better than recursion , less time complexity, more space complexity##")
print (x)
print(obj.fiboList)
print(obj.notrecount)
print(obj.retcount)
print(obj.loopcount)
print("## DYNAMIC PROGRAMMING##")
print (obj.fibodynamic(2))
print (obj.fibodyncnt)