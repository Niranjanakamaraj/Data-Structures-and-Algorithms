class Solution:
    def lowerBound(self, arr, target):
        l,r=0,len(arr)-1
        hold=len(arr)
        while l<=r:
            m=(l+r)//2
            if arr[m]>=target:
                hold=m
                r=m-1
            else:
                l=m+1
        return hold