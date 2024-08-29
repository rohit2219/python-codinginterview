#interview questions page 90 q1.1
'''
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
	'''

def permutations():
	inp = [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]
	points = inp
	initRect=tuple(map(tuple,inp[:4]))
	rectSet=set()
	rectSet.add(initRect)

	for j in range(len(initRect)):
		print('substituting:',j)
		for i in range(len((inp))):

			p1=tuple(points[i])
			print('each pt', p1)
			if p1 != initRect[j]:
				tempRect=list(initRect)
				tempRect[j]=p1
				print('add',tempRect)
				rectSet.add(tuple(tempRect))

	print(len(rectSet),rectSet)
	return
permutations()
