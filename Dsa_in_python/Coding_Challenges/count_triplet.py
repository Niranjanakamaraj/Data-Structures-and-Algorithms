class Solution:
	def countTriplet(self, arr):
		count=0
		arr.sort()
		for k in range(len(arr)-1,0,-1):
			i=0
			j=k-1
			while i<j:
				if arr[i]+arr[j]==arr[k]:
					count+=1
					i+=1
					j-=1
				elif arr[i]+arr[j]<arr[k]:
					i+=1
				else:
					j-=1
	    return count