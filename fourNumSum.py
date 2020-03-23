'''
class Solution(object):
	def twoSum(self,nums,target):
		counti=0
		countj=0
		result=[0,0]
		init_len=len(nums)
		diff_len=0
		result=[]
		for i in nums:
			if (result != []):
				print("exiting i loop")
				break
			
			countj=0
			result_found=0
			for j in nums:
					
					if  (countj != 0):
						try:
							if ( (i+j) == target ):
#									
								result=[counti,countj+diff_len]
								result_found=1
								break
						except:
							print ("Error in adding, breaking")
							break
					
					countj=countj+1
			if result_found==1:
				break
			counti=counti+1	
			nums=nums[1:]
			new_len=len(nums)
			diff_len=init_len-new_len			
		return result
	
	
def main():
	import time
	print("python program begins")
	sol=Solution()
	localtime = time.asctime( time.localtime(time.time()) )
	print(localtime)
	list1=list(range(0,25196,2))
	x=sol.twoSum(list1,16021)	
	print(x)
	
	localtime = time.asctime( time.localtime(time.time()) )
	print(localtime)

	return 0

if __name__ == "__main__":
    main()
'''
	
#	list1=list(range(0,25196,2)),,16021
#	list1=[0, 2, 4, 6, 8, 10, 12,30, 14, 16, 19]
#	list1=[2, 7, 11, 15]
#list1=[3,3],6
#list1[3,2,4],6

0
20
9
11


def fourSum(arr, Sum):
	for i in range(Sum):
		firstSum = i
		seconSum = Sum - i
		res1 = twoSum(arr, firstSum,[])
		res2 = twoSum(arr, seconSum,res1)
		print(firstSum,seconSum,' : ',res1,res2,arr)
		print(len(res1),len(res2),set(res1) - set(res2))
		if len(res1) == 2 and len(res2) == 2 and len(set(res1) - set(res2)) == 2 :
			print('result',res1,res2)
			res1.extend(res2)
			break

	return res1 if len(res1) == 4 else []

def twoSum(arr, Sum,notInArr):
	arrMap = {}
	notinSet=set(notInArr)
	for i in range(len(arr)):
		arrMap[arr[i]] = i
	for i in range(len(arr)):
		if (Sum - arr[i] in arrMap)  and (arrMap[arr[i]] != arrMap[Sum - arr[i]]) \
			and (arr[i] not in notinSet) and (Sum-arr[i] not in notinSet):
			return ([arrMap[arr[i]], arrMap[Sum - arr[i]]])
	return []


arr = [2, 7, 4, 0, 9, 5, 1, 3]
s = 20
print(fourSum(arr,20))