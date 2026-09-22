def findCeil(self, arr, x):
        l,r,hold=0,len(arr)-1,-1
        while l<=r:
            m=(l+r)//2
            if arr[m]>=x:
                hold=m
                r=m-1
            else:
                l=m+1
        return hold
