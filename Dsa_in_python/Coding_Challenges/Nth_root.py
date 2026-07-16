class Solution:
    def nthRoot(self, n, m):
        l,r=0,m
        while l<=r:
            mid=l+(r-l)//2
            if (mid**n)==m:
                return mid
            elif (mid**n)<m:
                l=mid+1
            else:
                r=mid-1
        return -1