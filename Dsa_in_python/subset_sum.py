class Solution:
	def subsetSums(self, arr):
	    a=[]
	    def f(i,s):
	        if i==len(arr):
	            a.append(s)
	            return
	        f(i+1,s+arr[i])
	        f(i+1,s)
	    f(0,0)
	    return a