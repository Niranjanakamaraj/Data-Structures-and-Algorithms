class Solution:
    def upperBound(self, arr, target):
        l,r,hold=0,len(arr)-1,len(arr)
        while l<=r:
            m=(l+r)//2
            if arr[m]>target:
                hold=m
                r=m-1
            else:
                l=m+1
        return hold