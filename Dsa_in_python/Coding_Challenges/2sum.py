class Solution:
	def twoSum(self, arr, target):
	    i,j=0,len(arr)-1
		arr.sort()
	    while i<j:
	        sum=arr[i]+arr[j]
	        if sum==target:
	            return True
	        elif sum>target:
	            j-=1
	        elif sum<target:
	            i+=1
	    return False