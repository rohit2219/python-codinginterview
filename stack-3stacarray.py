#/usr/bin/python3

#Space (not time) efficient. You could:

#1) Define two stacks beginning at the array endpoints and growing in opposite directions.

#2) Define the third stack as starting in the middle and growing in any direction you want.

#3) Redefine the Push op, so that when the operation is going to overwrite other stack, you shift the whole middle stack in the opposite direction before Pushing.

#You need to store the stack top for the first two stacks, and the beginning and end of the third stack in some structure.

class stack3(object):
	def __init__(self,object):
		self.intendArrLen=10
		self.stackArr=[0 for i in range(self.intendArrLen)]
		self.lenstackArr=len(self.stackArr)
		self.startstackArr=0
		self.endstackArr=0
		self.midstackArr=int(self.intendArrLen/2)
		## top of each stack
		self.begStack=0
		self.endStack=self.lenstackArr-1
		self.midStack=self.midstackArr
	def push(self,x,stackTyp):
		if stackTyp=="begin":
			self.stackArr[self.begStack]=x
			self.begstack=self.begStack+1
			
		elif stackTyp=="end":
			self.stackArr[self.endStack]=x
			self.endStack=self.endStack-1
		elif stackTyp=="mid":
			self.stackArr[self.midStack]=x
			self.endStack=self.midStack-1
		else:
			return
	def pop(self,stackTyp):
		if stackTyp=="begin":
			self.stackArr[self.begStack]=0
			self.begstack=self.begStack-1
			
		elif stackTyp=="end":
			self.stackArr[self.endStack]=0
			self.endStack=self.endStack+1
		elif stackTyp=="mid":
			self.stackArr[self.midStack]=0
			self.endStack=self.midStack+1
		else:
			return