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

	
#	list1=list(range(0,25196,2)),,16021
#	list1=[0, 2, 4, 6, 8, 10, 12,30, 14, 16, 19]
#	list1=[2, 7, 11, 15]
#list1=[3,3],6
#list1[3,2,4],6
