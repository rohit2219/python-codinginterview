#interview questions page 90 q1.1
def PermChecker(MasterStr,ChildStr)
	MasterStrDict={}
	PermFlag=False
	#convert the master string into a dict
	for i in range(len(MasterStr)):
		MasterStrDict[i]=i
		
	for i in range(len(ChildStr)):
		if ChildStr[i] in MasterStrDict:
			PermFlag=True
		else:
			PermFlag=False
			break
	retunr PermFlag
	





