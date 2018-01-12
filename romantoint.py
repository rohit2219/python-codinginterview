class Solution(object):
	def __init__(self):
		## declare any inits
		self.RomanDict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
	def romanToInt(self, Roman):
	
		if  isinstance (Roman,str) is False:
			return 0
		Int_Roman=0
		start=len(Roman)-1
		pointer=start
		DecimalPl=1
		while pointer >= 0:
			print(pointer)
			print (Roman[pointer])
			if ( ( pointer < start ) and self.RomanDict[Roman[pointer]] < self.RomanDict[Roman[pointer+1]] ) is True:
				Int_Roman= Int_Roman  - self.RomanDict[Roman[pointer]] 
			else:
				Int_Roman= Int_Roman  + self.RomanDict[Roman[pointer]] 
				
			pointer = pointer - 1
			
		return Int_Roman

x=Solution()
print(x.romanToInt("XXXIX"))